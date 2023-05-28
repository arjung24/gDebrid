from discord.ext import tasks
from discord.ext.pages import Paginator, Page
from io import BytesIO
import env
import rd
import time
import utils
import discord
import datetime
import pickledb

bot = discord.Bot(intents=discord.Intents.all())
db = pickledb.load("db.json", True)
green = 5956228
blue = 6868735
red = 16741752


class DebridModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="Enter your links here (One link per line)", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        input_lines = self.children[0].value.split("\n")
        unrestricted_links = []
        embeds = []
        for input_line in input_lines:
            if input_line:
                if ":http" in input_line:
                    password = input_line.split(":http")[0]
                    restricted_link = f'http{input_line.split(":http")[1]}'
                    unrestricted_link = rd.unrestrict(link=restricted_link, password=password)
                else:
                    restricted_link = input_line
                    unrestricted_link = rd.unrestrict(restricted_link)

                if unrestricted_link.status_code != 200:
                    embed = discord.Embed(description=restricted_link, color=red)
                    embed.add_field(name="error", value=unrestricted_link.data["error"], inline=False)
                    embed.add_field(name="error code", value=unrestricted_link.data["error_code"], inline=False)
                    embed.add_field(name="status code", value=unrestricted_link.status_code, inline=False)
                    unrestricted_links.append(Page(embeds=[embed]))
                else:
                    download_link = unrestricted_link.data["download"]
                    download_link = utils.g_debrid(download_link)
                    unrestricted = db.get("unrestricted")
                    db.set("unrestricted", unrestricted + unrestricted_link.data["filesize"])
                    unrestricted_links.append(Page(embeds=[success_unrestrict_embed(unrestricted_link.data, download_link, False)]))
                    embeds.append(success_unrestrict_embed(unrestricted_link.data, unrestricted_link.data["link"], True, interaction.user))
                    if len(embeds) == 10:
                        await bot.get_channel(env.log_channel_id()).send(embeds=embeds)
                        embeds = []
        if len(embeds) >= 1:
            await bot.get_channel(env.log_channel_id()).send(embeds=embeds)
        paginator = Paginator(pages=unrestricted_links, timeout=300)
        paginator.remove_button("first")
        paginator.remove_button("last")
        await paginator.respond(interaction, ephemeral=True)


class TorrentModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="Enter your magnet link", style=discord.InputTextStyle.short))

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        torrent = rd.torrents_add_magnet(self.children[0].value)
        if torrent.status_code == 201:
            id = torrent.data["id"]
            torrent_info = rd.torrents_info(id)
            if torrent_info.status_code == 200:
                if torrent_info.data["status"] == "magnet_conversion":
                    time.sleep(1)
                    torrent_info = rd.torrents_info(id)
                if torrent_info.data["status"] == "waiting_files_selection":
                    rd.torrents_select_files(id, "all")
                    torrent_info = rd.torrents_info(id)
                msg = await bot.get_channel(env.torrent_channel_id()).send(embeds=[torrent_info_msg(torrent_info.data)])
                await interaction.followup.send(embeds=[discord.Embed(description=f"The torrent with the hash `{torrent_info.data['hash']}` has been added to the queue. Watch the progress here: {msg.jump_url}\nAs soon as it is ready, I will send you the download link via direct message.", color=green)], ephemeral=True)
                if torrent_info.data["status"] == "downloaded":
                    dm = ""
                    embeds = []
                    for link in torrent_info.data['links']:
                        unrestricted_link = rd.unrestrict(link)
                        if str(unrestricted_link.status_code).startswith("2"):
                            download_link = unrestricted_link.data["download"]
                            download_link = utils.g_debrid(download_link)
                            unrestricted = db.get("unrestricted")
                            db.set("unrestricted", unrestricted + unrestricted_link.data["filesize"])
                            dm += f"{download_link}\n"
                            embeds.append(success_unrestrict_embed(unrestricted_link.data, "", True, interaction.user))
                            if len(embeds) == 10:
                                await bot.get_channel(env.log_channel_id()).send(embeds=embeds)
                                embeds = []
                    if len(embeds) >= 1:
                        await bot.get_channel(env.log_channel_id()).send(embeds=embeds)
                    try:
                        await interaction.user.send(content=torrent_info.data["filename"], file=discord.File(BytesIO(str.encode(dm)), filename=f"{torrent_info.data['filename']}.txt"))
                    except:
                        await bot.get_channel(env.general_channel_id()).send(interaction.user.mention, embeds=[discord.Embed(description="You are blocking direct messages. I cannot send you the download link for your torrent.", color=red)])
                else:
                    db.dadd("torrents", (msg.id, f"{interaction.user.id}|{id}"))
            else:
                embed = discord.Embed(color=red)
                embed.add_field(name="error", value=torrent_info.data["error"], inline=False)
                embed.add_field(name="error code", value=torrent_info.data["error_code"], inline=False)
                embed.add_field(name="status code", value=torrent_info.status_code, inline=False)
                await interaction.followup.send(embeds=[embed], ephemeral=True)
        else:
            embed = discord.Embed(color=red)
            embed.add_field(name="error", value=torrent.data["error"], inline=False)
            if "error_details" in torrent.data:
                embed.add_field(name="error details", value=torrent.data["error_details"], inline=False)
            embed.add_field(name="error code", value=torrent.data["error_code"], inline=False)
            embed.add_field(name="status code", value=torrent.status_code, inline=False)
            await interaction.followup.send(embeds=[embed], ephemeral=True)


class KeyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="Enter the key you got from the admin here", style=discord.InputTextStyle.short))

    async def callback(self, interaction: discord.Interaction):
        if db.lexists("keys", self.children[0].value):
            db.lremvalue("keys", self.children[0].value)
            db.dump()
            await interaction.user.add_roles(interaction.guild.get_role(env.leecher_role_id()))
            await bot.get_channel(env.general_channel_id()).send(f"Welcome {interaction.user.mention} 🥳")
            await interaction.response.defer()
        else:
            await interaction.response.send_message(embeds=[discord.Embed(description="Invalid key!", color=red)], ephemeral=True, delete_after=10)


class ApplicationModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="How did you find the server?", style=discord.InputTextStyle.short, max_length=1024))
        self.add_item(discord.ui.InputText(label="Who do you know from the server?", style=discord.InputTextStyle.short, max_length=1024))
        self.add_item(discord.ui.InputText(label="Why should we accept your application?", style=discord.InputTextStyle.long, max_length=1024))

    async def callback(self, interaction: discord.Interaction):
        db.ladd("applications", interaction.user.id)
        embed = discord.Embed(color=blue, timestamp=datetime.datetime.now())
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar)
        embed.add_field(name="How did you find the server?", value=self.children[0].value, inline=False)
        embed.add_field(name="Who do you know from the server?", value=self.children[1].value, inline=False)
        embed.add_field(name="Why should we accept your application?", value=self.children[2].value, inline=False)
        application_message = await bot.get_channel(env.applications_channel_id()).send(embeds=[embed])
        await application_message.add_reaction("👍")
        await application_message.add_reaction("👎")
        db.set(str(application_message.id), interaction.user.id)
        await interaction.response.send_message(embeds=[discord.Embed(description="The application has been sent. We will inform you as soon as we have news. However, do not leave the server. Otherwise, the role cannot be assigned to you.", color=green)], ephemeral=True)


class DebridButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="gDebrid", custom_id="debrid-btn", style=discord.ButtonStyle.green)
    async def debrid_button_callback(self, button, interaction):
        await interaction.response.send_modal(DebridModal(title="gDebrid"))

    @discord.ui.button(label="gTorrent", custom_id="torrent-btn", style=discord.ButtonStyle.green)
    async def torrent_button_callback(self, button, interaction):
        await interaction.response.send_modal(TorrentModal(title="gTorrent"))


class InfoButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="apply", custom_id="apply-btn", style=discord.ButtonStyle.blurple)
    async def first_button_callback(self, button, interaction):
        if db.lexists("applications", interaction.user.id):
            await interaction.response.send_message(embeds=[discord.Embed(description="You have already applied!", color=red)], ephemeral=True, delete_after=10)
        else:
            await interaction.response.send_modal(ApplicationModal(title="Write your application"))

    @discord.ui.button(label="key", custom_id="key-btn", style=discord.ButtonStyle.blurple)
    async def second_button_callback(self, button, interaction):
        await interaction.response.send_modal(KeyModal(title="Join via invite key"))


def success_unrestrict_embed(unrestricted_link_data: dict, link: str, inline: bool, author: discord.User = None):
    embed = discord.Embed(title=unrestricted_link_data["filename"], url=link, color=green)
    if author:
        embed.set_author(name=author.name, icon_url=author.display_avatar)
        embed.timestamp = datetime.datetime.now()
    embed.add_field(name="file size", value=utils.format_bytes(unrestricted_link_data["filesize"]), inline=inline)
    embed.add_field(name="chunks", value=unrestricted_link_data["chunks"], inline=inline)
    embed.add_field(name="mime type", value=unrestricted_link_data["mimeType"], inline=inline)
    if unrestricted_link_data["host"] == "real-debrid.com":
        embed.set_footer(text="Torrent", icon_url="https://img.icons8.com/?size=512&id=tjsWQ7hPnW7V&format=png")
    else:
        embed.set_footer(text=unrestricted_link_data["host"], icon_url=unrestricted_link_data["host_icon"])
    return embed


def torrent_info_msg(data):
    if data["status"] == "downloaded":
        color = green
    elif data["status"] in ["queued", "downloading", "compressing", "uploading", "magnet_conversion", "waiting_files_selection"]:
        color = blue
    else:
        color = red
    embed = discord.Embed(title=data["filename"], color=color)
    embed.add_field(name="hash", value=data["hash"], inline=False)
    embed.add_field(name="size", value=utils.format_bytes(data["bytes"]), inline=True)
    embed.add_field(name="progress", value=f'{data["progress"]}%', inline=True)
    embed.add_field(name="status", value=data["status"], inline=True)
    if "seeders" in data:
        embed.add_field(name="seeders", value=data["seeders"], inline=True)
    if "speed" in data:
        speed = utils.format_bytes(data["speed"])
        if speed == "N/A":
            speed = "0B"
        embed.add_field(name="speed", value=f"{speed}/s", inline=True)
    embed.timestamp = datetime.datetime.now()
    return embed


@bot.slash_command(name="init_debrid", description="initiate debrid button")
@discord.default_permissions(administrator=True)
async def init_debrid(ctx):
    debrid_button_description = f"""Click the green `gDebrid` button at the bottom of this message.
    A window with an input field will open. Enter each link in a new line of the input field.
    If the restricted link is protected with a password, write it in front of the link and separate it with a simple colon.
    Attention, before and after the colon, do not put a space. Example: `mysecpw:https://filehoster.tld/file`.
    I will reply shortly with the unrestricted links. Do not panic if it takes a while. Expect 3 seconds per link.
    Additionally you can watch my progress in <#{env.log_channel_id()}>.""".replace("  ", "")
    await ctx.send(debrid_button_description, view=DebridButtons())
    await ctx.respond("done", ephemeral=True, delete_after=3)


@bot.slash_command(name="init_info", description="initiate info buttons")
@discord.default_permissions(administrator=True)
async def init_info(ctx):
    debrid_button_description = f"""Signups are closed!
    You can't use gDebrid right now. However, you can write an application why we should admit you anyway.
    Click the blurple `apply` button at the bottom of this message and fill in the fields with your answers.
    All members of gDebrid can then vote if we let you join or not.
    If you have received a key from the admin or another member you can click the blurple `key` button at the bottom of this message to get direct access.""".replace("  ", "")
    await ctx.send(debrid_button_description, view=InfoButtons())
    await ctx.respond("done", ephemeral=True, delete_after=3)


@bot.slash_command(name="gen_key", description="generates a key")
@discord.default_permissions(administrator=True)
async def gen_key(ctx, amount: discord.Option(int) = 1):
    keys = "```"
    for _ in range(amount + 1):
        key = utils.gen_key()
        db.ladd("keys", key)
        keys += f"{key}\n"
    keys += "```"
    await ctx.respond(keys, ephemeral=True, delete_after=10)


@bot.slash_command(name="set_rd_token", description="set real-debrid token")
@discord.default_permissions(administrator=True)
async def set_rd_token(ctx, token: discord.Option(str)):
    env.set_rd_token(token)
    rd.headers = {"Authorization": f"Bearer {token}"}
    await ctx.respond("done", ephemeral=True, delete_after=10)


@bot.message_command(name="accept application")
@discord.default_permissions(administrator=True)
async def accept_application(ctx, message: discord.Message):
    await answer_application(True, ctx, message)


@bot.message_command(name="reject application")
@discord.default_permissions(administrator=True)
async def reject_application(ctx, message: discord.Message):
    await answer_application(False, ctx, message)


async def answer_application(accepted: bool, ctx, message: discord.Message):
    if db.exists(str(message.id)):
        applicant = db.get(str(message.id))
        db.rem(str(message.id))
        if db.lexists("applications", applicant):
            db.lremvalue("applications", applicant)
        db.dump()
        if accepted:
            color = green
        else:
            color = red
        embed = discord.Embed(color=color)
        embed.set_author(name=message.embeds[0].author.name, icon_url=message.embeds[0].author.icon_url)
        embed.add_field(name="How did you find the server?", value=message.embeds[0].fields[0].value, inline=False)
        embed.add_field(name="Who do you know from the server?", value=message.embeds[0].fields[1].value, inline=False)
        embed.add_field(name="Why should we accept your application?", value=message.embeds[0].fields[2].value, inline=False)
        await message.edit(embeds=[embed])
        if applicant:
            member = ctx.guild.get_member(applicant)
            if member:
                if accepted:
                    await member.add_roles(ctx.guild.get_role(env.leecher_role_id()))
                    await bot.get_channel(env.general_channel_id()).send(f"Welcome {member.mention} 🥳")
                    await ctx.response.send_message(embeds=[discord.Embed(description="User got accepted.", color=green)], ephemeral=True, delete_after=5, allowed_mentions=discord.AllowedMentions(users=False))
                else:
                    await member.ban(reason="Your application was rejected")
                    await ctx.response.send_message(embeds=[discord.Embed(description="User got banned.", color=green)], ephemeral=True, delete_after=5, allowed_mentions=discord.AllowedMentions(users=False))
            else:
                await ctx.response.send_message(embeds=[discord.Embed(description="Error: applicant left guild!", color=red)], ephemeral=True, delete_after=5, allowed_mentions=discord.AllowedMentions(users=False))
        else:
            await ctx.response.send_message(embeds=[discord.Embed(description="Error: applicant not found!", color=red)], ephemeral=True, delete_after=5, allowed_mentions=discord.AllowedMentions(users=False))
    else:
        await ctx.response.send_message(embeds=[discord.Embed(description="Application already answered", color=red)], ephemeral=True, delete_after=5, allowed_mentions=discord.AllowedMentions(users=False))


@bot.event
async def on_ready():
    if not db.exists("keys"):
        db.lcreate("keys")
    if not db.exists("applications"):
        db.lcreate("applications")
    if not db.exists("torrents"):
        db.dcreate("torrents")
    bot.add_view(DebridButtons())
    bot.add_view(InfoButtons())
    try:
        status_message = await bot.get_channel(env.status_channel_id()).fetch_message(env.status_message_id())
    except:
        status_message = await bot.get_channel(env.status_channel_id()).send(embeds=[discord.Embed(description="initiate status message", timestamp=datetime.datetime.now())])
        env.set_status_message_id(status_message.id)
    host_status_task.start(status_message)
    stats_task.start()
    torrent_task.start()
    print(f"{bot.user} is ready and online!")


@tasks.loop(minutes=5)
async def host_status_task(status_message: discord.Message):
    description = ""
    hosts_status = rd.hosts_status()
    if hosts_status.status_code != 200:
        await status_message.edit(embeds=[discord.Embed(description="failed to fetch hosts status", color=red, timestamp=datetime.datetime.now())])
        return
    hosts = rd.hosts_status().data
    for host in hosts:
        if bool(hosts[host]["supported"]):
            if hosts[host]["status"] == "up":
                status = ":green_circle:"
            else:
                status = ":red_circle:"
            if host == "clicknupload.me":
                description += f'{status} [{hosts[host]["name"]}](https://clicknupload.click)\n'
            elif host == "gigapeta.com" or "sky.fm":
                description += f'{status} [{hosts[host]["name"]}](http://{host})\n'
            elif host == "easybytez.com":
                description += f'{status} [{hosts[host]["name"]}](https://easybytez.net)\n'
            else:
                description += f'{status} [{hosts[host]["name"]}](https://{host})\n'
    await status_message.edit(embeds=[discord.Embed(description=description, color=blue, timestamp=datetime.datetime.now())])


@tasks.loop(minutes=10)
async def stats_task():
    unrestricted = db.get("unrestricted")
    x = f"unrestricted {utils.format_bytes(unrestricted)}"
    await bot.get_channel(env.stats_channel_id()).edit(name=x)


@tasks.loop(minutes=2)
async def torrent_task():
    torrents = db.get("torrents")
    for msg_id in list(torrents):
        torrent = db.dget("torrents", msg_id)
        torrent_info = rd.torrents_info(torrent.split("|")[1])
        if torrent_info.data["status"] == "waiting_files_selection":
            rd.torrents_select_files(torrent.split("|")[1], "all")
            torrent_info = rd.torrents_info(torrent.split("|")[1])
        msg = await bot.get_channel(env.torrent_channel_id()).fetch_message(int(msg_id))
        await msg.edit(embeds=[torrent_info_msg(torrent_info.data)])
        if torrent_info.data["status"] == "downloaded":
            user = await bot.fetch_user(torrent.split("|")[0])
            db.dpop("torrents", msg_id)
            dm = ""
            embeds = []
            for link in torrent_info.data['links']:
                unrestricted_link = rd.unrestrict(link)
                if str(unrestricted_link.status_code).startswith("2"):
                    download_link = unrestricted_link.data["download"]
                    download_link = utils.g_debrid(download_link)
                    unrestricted = db.get("unrestricted")
                    db.set("unrestricted", unrestricted + unrestricted_link.data["filesize"])
                    dm += f"{download_link}\n"
                    embeds.append(success_unrestrict_embed(unrestricted_link.data, "", True, user))
                    if len(embeds) == 10:
                        await bot.get_channel(env.log_channel_id()).send(embeds=embeds)
                        embeds = []
            if len(embeds) >= 1:
                await bot.get_channel(env.log_channel_id()).send(embeds=embeds)
            try:
                await user.send(content=torrent_info.data["filename"], file=discord.File(BytesIO(str.encode(dm)), filename=f"{torrent_info.data['filename']}.txt"))
            except:
                await bot.get_channel(env.general_channel_id()).send(user.mention, embeds=[discord.Embed(description="You are blocking direct messages. I cannot send you the download link for your torrent.", color=red)])
        elif torrent_info.data["status"] in ["magnet_error", "error", "virus", "dead"]:
            db.dpop("torrents", msg_id)


bot.run(env.discord_token())

import discord
from discord.ext import tasks
from discord.ext.pages import Paginator, Page
import env
import rd
import utils
import datetime
import pickledb

bot = discord.Bot()
db = pickledb.load("db.json", True)


class DebridModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="Enter your links here (One link per line)", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        input_lines = self.children[0].value.split("\n")
        unrestricted_links = []
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
                    embed = discord.Embed(description=restricted_link, color=16741752)
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
                    await bot.get_channel(env.log_channel_id()).send(
                        embeds=[success_unrestrict_embed(unrestricted_link.data, unrestricted_link.data["link"], True, interaction.user)])
        paginator = Paginator(pages=unrestricted_links, timeout=300)
        paginator.remove_button("first")
        paginator.remove_button("last")
        await paginator.respond(interaction, ephemeral=True)


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
            await interaction.response.send_message(embeds=[discord.Embed(description="Invalid key!", color=16741752)], ephemeral=True, delete_after=10)


class ApplicationModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="How did you find the server?", style=discord.InputTextStyle.short, max_length=1024))
        self.add_item(discord.ui.InputText(label="Who do you know from the server?", style=discord.InputTextStyle.short, max_length=1024))
        self.add_item(discord.ui.InputText(label="Why should we accept your application?", style=discord.InputTextStyle.long, max_length=1024))

    async def callback(self, interaction: discord.Interaction):
        db.ladd("applications", interaction.user.id)
        embed = discord.Embed(color=6868735, timestamp=datetime.datetime.now())
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar)
        embed.add_field(name="How did you find the server?", value=self.children[0].value, inline=False)
        embed.add_field(name="Who do you know from the server?", value=self.children[1].value, inline=False)
        embed.add_field(name="Why should we accept your application?", value=self.children[2].value, inline=False)
        application_message = await bot.get_channel(env.applications_channel_id()).send(embeds=[embed])
        await application_message.add_reaction("👍")
        await application_message.add_reaction("👎")
        db.set(str(application_message.id), interaction.user.id)
        await interaction.response.send_message(embeds=[discord.Embed(description="The application has been sent. We will inform you as soon as we have news. However, do not leave the server. Otherwise, the role cannot be assigned to you.", color=5956228)], ephemeral=True)


class DebridButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="gDebrid", custom_id="debrid-btn", style=discord.ButtonStyle.green)
    async def button_callback(self, button, interaction):
        await interaction.response.send_modal(DebridModal(title="gDebrid"))


class InfoButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="apply", custom_id="apply-btn", style=discord.ButtonStyle.blurple)
    async def first_button_callback(self, button, interaction):
        if db.lexists("applications", interaction.user.id):
            await interaction.response.send_message(embeds=[discord.Embed(description="You have already applied!", color=16741752)], ephemeral=True, delete_after=10)
        else:
            await interaction.response.send_modal(ApplicationModal(title="Write your application"))

    @discord.ui.button(label="key", custom_id="key-btn", style=discord.ButtonStyle.blurple)
    async def second_button_callback(self, button, interaction):
        await interaction.response.send_modal(KeyModal(title="Join via invite key"))


def success_unrestrict_embed(unrestricted_link_data: dict, link: str, inline: bool, author: discord.User = None):
    embed = discord.Embed(title=unrestricted_link_data["filename"], url=link, color=5956228)
    if author:
        embed.set_author(name=author.name, icon_url=author.display_avatar)
        embed.timestamp = datetime.datetime.now()
    embed.add_field(name="file size", value=utils.format_bytes(unrestricted_link_data["filesize"]), inline=inline)
    embed.add_field(name="chunks", value=unrestricted_link_data["chunks"], inline=inline)
    embed.add_field(name="mime type", value=unrestricted_link_data["mimeType"], inline=inline)
    embed.set_footer(text=unrestricted_link_data["host"], icon_url=unrestricted_link_data["host_icon"])
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
    await ctx.send(debrid_button_description, view=DebridButton())
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
async def gen_key(ctx):
    key = utils.gen_key()
    db.ladd("keys", key)
    await ctx.respond(f"```{key}```", ephemeral=True, delete_after=10)


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
            color = 5956228
        else:
            color = 16741752
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
                    await ctx.response.send_message(embeds=[discord.Embed(description="User got accepted.", color=5956228)], ephemeral=True, delete_after=5)
                else:
                    await member.ban(reason="Your application was rejected")
                    await ctx.response.send_message(embeds=[discord.Embed(description="User got baned.", color=5956228)], ephemeral=True, delete_after=5)
            else:
                await ctx.response.send_message(embeds=[discord.Embed(description="Error: applicant left guild!", color=16741752)], ephemeral=True, delete_after=5)
        else:
            await ctx.response.send_message(embeds=[discord.Embed(description="Error: applicant not found!", color=16741752)], ephemeral=True, delete_after=5)
    else:
        await ctx.response.send_message(embeds=[discord.Embed(description="Application already answered", color=16741752)], ephemeral=True, delete_after=5)


@bot.event
async def on_ready():
    if not db.exists("keys"):
        db.lcreate("keys")
    if not db.exists("applications"):
        db.lcreate("applications")
    bot.add_view(DebridButton())
    bot.add_view(InfoButtons())
    try:
        status_message = await bot.get_channel(env.status_channel_id()).fetch_message(env.status_message_id())
    except:
        status_message = await bot.get_channel(env.status_channel_id()).send(embeds=[discord.Embed(description="initiate status message", timestamp=datetime.datetime.now())])
        env.set_status_message_id(status_message.id)
    host_status_task.start(status_message)
    stats_task.start()
    print(f"{bot.user} is ready and online!")


@tasks.loop(minutes=5)
async def host_status_task(status_message: discord.Message):
    description = ""
    hosts_status = rd.hosts_status()
    if hosts_status.status_code != 200:
        await status_message.edit(embeds=[discord.Embed(description="failed to fetch hosts status", color=16741752, timestamp=datetime.datetime.now())])
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
    await status_message.edit(embeds=[discord.Embed(description=description, color=6868735, timestamp=datetime.datetime.now())])


@tasks.loop(minutes=10)
async def stats_task():
    unrestricted = db.get("unrestricted")
    x = f"unrestricted {utils.format_bytes(unrestricted)}"
    await bot.get_channel(env.stats_channel_id()).edit(name=x)


bot.run(env.discord_token())

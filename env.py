import json
from dotenv import load_dotenv, set_key, get_key


load_dotenv()


def discord_token():
    return get_key(".env", "discord_token")


def log_channel_id():
    return int(get_key(".env", "log_channel_id"))


def torrent_channel_id():
    return int(get_key(".env", "torrent_channel_id"))


def status_channel_id():
    return int(get_key(".env", "status_channel_id"))


def applications_channel_id():
    return int(get_key(".env", "applications_channel_id"))


def general_channel_id():
    return int(get_key(".env", "general_channel_id"))


def stats_channel_id():
    return int(get_key(".env", "stats_channel_id"))


def set_status_message_id(status_message_id: int):
    set_key(".env", "status_message_id", str(status_message_id))


def status_message_id():
    return int(get_key(".env", "status_message_id"))


def leecher_role_id():
    return int(get_key(".env", "leecher_role_id"))


def rd_token():
    return get_key(".env", "rd_token")


def set_rd_token(token):
    set_key(".env", "rd_token", token)


def g_debrid_password():
    return bytes(json.loads(get_key(".env", "g_debrid_password")))


def g_debrid_iv():
    return bytes(json.loads(get_key(".env", "g_debrid_iv")))

import base64
from io import BytesIO
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import urllib.parse
import env
import random
import string
import time
import torf


def format_bytes(size: int):
    if size == 0:
        return "N/A"
    power = 2**10
    n = 0
    power_labels = {0: '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return f"{float(round(size, 2)):g} {power_labels[n]}B"


def g_debrid(link: str):
    data = link.split(".download.real-debrid.com/d/")[1].split("/")[0]
    file = link.split(f"{data}/")[1]
    data += f':{str(round(int(time.time())))}:{link.split("https://")[1].split(".download.real-debrid.com/d/")[0]}'
    password = env.g_debrid_password()
    iv = env.g_debrid_iv()
    out = base64.b64encode(AES.new(password, AES.MODE_CBC, iv).encrypt(pad(data.encode(), AES.block_size))).decode('utf-8')
    if out.endswith("="):
        out = out[:-1]
    out = base64.b64encode(bytes(out, 'utf-8')).decode('utf-8')
    if out.endswith("=="):
        out = out[:-2]

    return f"https://debrid.gookie.dev/{urllib.parse.quote(out, safe='')}/{file}"


def gen_key():
    characters = string.ascii_letters + string.digits
    key = ""
    for index in range(32):
        key = key + random.choice(characters)
    return key


def torrent2magnet(torrent):
    try:
        return torf.Torrent().read_stream(BytesIO(requests.get(torrent.url).content)).magnet()
    except:
        return "failed"

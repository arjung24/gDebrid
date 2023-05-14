import env
import requests

base_url = "https://api.real-debrid.com/rest/1.0"
headers = {"Authorization": f"Bearer {env.rd_token()}"}


class RData:
    def __init__(self, status_code: int, data: dict):
        self.status_code = status_code
        self.data = data


def traffic():
    r = requests.get(url=f"{base_url}/traffic/details", headers=headers)
    return r.json()


def unrestrict(link: str, password: str = None):
    data = {"link": link}
    if password:
        data["password"] = password
    r = requests.post(url=f"{base_url}/unrestrict/link", data=data, headers=headers)
    return RData(status_code=r.status_code, data=r.json())


def hosts_status():
    r = requests.get(url=f"{base_url}/hosts/status", headers=headers)
    return RData(status_code=r.status_code, data=r.json())

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
    if r.headers.get('Content-Type').startswith('application/json'):
        return RData(status_code=r.status_code, data=r.json())
    else:
        return RData(status_code=r.status_code, data=None)


def hosts_status():
    r = requests.get(url=f"{base_url}/hosts/status", headers=headers)
    return RData(status_code=r.status_code, data=r.json())


def torrents_add_magnet(magnet: str):
    data = {"magnet": magnet}
    r = requests.post(url=f"{base_url}/torrents/addMagnet", data=data, headers=headers)
    return RData(status_code=r.status_code, data=r.json())


def torrents_info(id: str):
    r = requests.get(url=f"{base_url}/torrents/info/{id}", headers=headers)
    return RData(status_code=r.status_code, data=r.json())


def torrents_select_files(id: str, files: str):
    data = {"files": files}
    r = requests.post(url=f"{base_url}/torrents/selectFiles/{id}", data=data, headers=headers)
    return RData(status_code=r.status_code, data={})


text = """AVATAR Series (2005-2014) - COMPLETE The Last Airbender, 2010 Movie, Legend of Korra - 1080p BluRay x264
```https://debrid.gookie.dev/Ti9pREZDYnJZUkc4Z0tERDcxUmpYKzZiQlpFQ1B6MEIxU04xUzBhbTZ5WQ/Avatar%20%28TLA%29%20-%20S01%20E01%20-%20The%20Boy%20in%20the%20Iceberg%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/ZDNJL1J2ZGNPOXhVdnhLY3F5S09tdnEyNmJNL1JDV0dpYUFCZHVSTG5Pdw/Avatar%20%28TLA%29%20-%20S01%20E02%20-%20The%20Avatar%20Returns%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/RDhVRUw5QlN0Znc3M2M4bTZWZCtJdnM0aUJQY1ZPbi8vWDlFSnZTQmU0MA/Avatar%20%28TLA%29%20-%20S01%20E03%20-%20The%20Southern%20Air%20Temple%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/am1PbkRoVSthRVo0UTJnZ01BV1Z1cmNwdUdzTUIxY0IwT0ZZZDRYSFF2bw/Avatar%20%28TLA%29%20-%20S01%20E04%20-%20The%20Warriors%20of%20Kyoshi%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/N1U1cVZveHN5K1VLNUVBSldXLzNzS1FTRmdEM2YvZVhVZnk0ZWljRzR6SQ/Avatar%20%28TLA%29%20-%20S01%20E05%20-%20The%20King%20of%20Omashu%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/QXYvVkVuT1ovQUpVOEg3VmhUc0NZejFTZFFXVDJ5bnlQUFZoeE1lL0J4OA/Avatar%20%28TLA%29%20-%20S01%20E06%20-%20Imprisoned%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/eXpzK2FMUVliWTltS1pOR055N1lGMmg5VkkzY0dSQkluLzUxUzBRRjFiMA/Avatar%20%28TLA%29%20-%20S01%20E07%20-%20Winter%20Solstice%201%2C%20The%20Spirit%20World%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/cmFyMFNJQU5rSDlYeGVBV0xnRVVpZzhXT3FvRUpMc2RNZWRsODNDdFM4RQ/Avatar%20%28TLA%29%20-%20S01%20E08%20-%20Winter%20Solstice%202%2C%20Avatar%20Roku%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/QldyUnVWdmpiZmZGU05MVWJNTVd3cE5JZGNRNlVDY1NMWXlJK1Vrb1NTRQ/Avatar%20%28TLA%29%20-%20S01%20E09%20-%20The%20Waterbending%20Scroll%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/RmM0Q1huK0VUcjJrbVdpY05YWW8yMnVpVXMxWUg0RXE4bUJRbWJzNTBhNA/Avatar%20%28TLA%29%20-%20S01%20E10%20-%20Jet%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/WElBS2xBWnM0M1A3MXBVZHdSRmRIbjVsekNWNGlVVWZlQm92RUNWOVp0WQ/Avatar%20%28TLA%29%20-%20S01%20E11%20-%20The%20Great%20Divide%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/SmpjWUhHNk05OVBUSSszZ0xkNEJlb2pSUzFQU1o1cjFSM3RjSW03ZWRLWQ/Avatar%20%28TLA%29%20-%20S01%20E12%20-%20The%20Storm%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/MXJINHFIN3BxSkZyMUVxbk5yT3N6UW9EYzgrKzd0cDJPMy82WXVOa25nUQ/Avatar%20%28TLA%29%20-%20S01%20E13%20-%20The%20Blue%20Spirit%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/alFyNHNxcHR5RFBHbTk2d2FEL21uTy9YUXliTHA2bFhTNGJGdE1nU1VVdw/Avatar%20%28TLA%29%20-%20S01%20E14%20-%20The%20Fortuneteller%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/dnFWTmY4cDNsODVZZEZ4eXJ3VERIRCt2aytPR2V0UFIyYVNqOGpwNjBlaw/Avatar%20%28TLA%29%20-%20S01%20E15%20-%20Bato%20of%20the%20Water%20Tribe%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/cEtjbWo4NlNsZDVRaFZKYzdCNndLN3VjMkRwZGFIVnRoK2pQT3BjeUZiSQ/Avatar%20%28TLA%29%20-%20S01%20E16%20-%20The%20Deserter%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/azFHU24wWDRtOW9QZ2ZnZnNoemplK2w5eGI4MXFLVXhIOGlDTmxMQlFHQQ/Avatar%20%28TLA%29%20-%20S01%20E17%20-%20The%20Northern%20Air%20Temple%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/UEorWDM5b0ZsOGxhSThFRnRUY0dWRE05ek1KODRMYm9HQnFBeXZqMysvOA/Avatar%20%28TLA%29%20-%20S01%20E18%20-%20The%20Waterbending%20Master%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/eFRiRHZxSUxQUTA0WWUxMHFKcHFZb1RkaEkyYjVwWVZSaTZyRzQzSnRkOA/Avatar%20%28TLA%29%20-%20S01%20E19%20-%20The%20Siege%20of%20the%20North%2C%20Part%201%20of%202%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/TS9tWjZQcjYvbnBpVlZ4NTg5bG9WazJrcm9IRlJuVC95eDBRWHByelZNdw/Avatar%20%28TLA%29%20-%20S01%20E20%20-%20The%20Siege%20of%20the%20North%2C%20Part%202%20of%202%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/dGJNaS8yaWlrTmZHWERVbC9GQk9vUmhMN01qVDBOc1dYSitDS3AxRStNTQ/Ask%20The%20Creators%20Featurette%20%28480p%29.mp4
https://debrid.gookie.dev/V3p6RUV4MTJZRTBYbUc4Ukw5TWtvYWJuMDVZdkxKQkFDL0lkN1d3WlNUVQ/Avatar%20Pilot%20Episode%20With%20Audio%20Commentary%20%28480p%29.mp4
https://debrid.gookie.dev/a3hXSmVGSFNwWlJjUE03d2F2M1hKaGdZQmJFUUY5bEFrT3MrYStjSGlSRQ/Behind%20The%20Scenes%20-%20The%20Voices%20Of%20Avatar%20%28480p%29.mp4
https://debrid.gookie.dev/enc1dGplQ3hwbUpoNU1LL0krVjdRMXp3d1dSMVlJbkdWSmZRNWhGZ1BvZw/Behind%20The%20Scenes%20With%20The%20Avatar%20Cast%20and%20Crew%20%28480p%29.mp4
https://debrid.gookie.dev/TnRDUWlNcU1qc1VqVUo3Uit0UVJlT0FlelBKR3g3WmZxUVdQeHdJSGZOYw/Creating%20The%20Legend%20Of%20Airbending%20%28480p%29.mp4
https://debrid.gookie.dev/SXpHc3pIREVoVko0aUtvd0p2QXVjdnNsWUFZM2FhRXFJMC9GTG0yTUtidw/Creating%20The%20Legend%20Of%20Earthbending%20%28480p%29.mp4
https://debrid.gookie.dev/QVI5WDJoL2hORVRLTWJOMnJEQlF5WUFsUFB4alNKV0Y5SVFlT2NNNTRSRQ/Creating%20The%20Legend%20Of%20Firebending%20%28480p%29.mp4
https://debrid.gookie.dev/dEtnZ2JHYmQyd2p1bEhTQTA5SlRVV3NBMWd2VFhsUTRWVEY4ZCtNUXZjVQ/Creating%20The%20Legend%20Of%20Waterbending%20%28480p%29.mp4
https://debrid.gookie.dev/cHhZWnE4VVZRTlBqNmFyVE44VWxHekNTOU8rVU9ZYjN3eENnalVEQzJKZw/Menu%20Art%20-%20Disk%201%20%281080p%29.mp4
https://debrid.gookie.dev/ci93bkJ1WTIyWGJwSk94NVZRWW14dGM5aDI5Ui9ueXBiZ0FRSEV1WEVXUQ/Menu%20Art%20-%20Disk%202%20%281080p%29.mp4
https://debrid.gookie.dev/SEF1U3BCQkpvdi9Ld0xCbHBSa2hLbDFBWTZ2MU1ZOHhya0xRQ1pocXVTOA/Menu%20Art%20-%20Disk%203%20%281080p%29.mp4
https://debrid.gookie.dev/V0ltUUttb1lWa1M1aTgwek02eDRNVk9VZStVcWlQK2Yrb1hzRWZINTRLcw/Original%20Uncut%20Animatic%20-%20Episode%2015%20-%20Bato%20Of%20The%20Water%20Tribe%20%28480p%29.mp4
https://debrid.gookie.dev/ZUFxVVlMTFdqdnF0Z3JkUVJtSGxRcmVqYzJWMjVNcVJuQ3V2elQwNDFscw/The%20Making%20Of%20Avatar%20-%20From%20Real%20Life%20To%20Animation%20%28480p%29.mp4
https://debrid.gookie.dev/UElLZkwxUUVHZlM4RFIzUEpMK255eSttTGdXWGo5V1dwQnFRWlBXMFlDYw/The%20Making%20Of%20Avatar%20-%20Inside%20The%20Korean%20Animation%20Studios%20%28480p%29.mp4
https://debrid.gookie.dev/ellJT3VST1ZJQVFtd3hpSUJCdmpqZUhDN3c0WHlmS1J6VkJndWlkL09pUQ/The%20Making%20Of%20Avatar%20-%20Inside%20The%20Sound%20Studios%20%28480p%29.mp4
https://debrid.gookie.dev/TkkvNERzd1IrTWFBZ0VTRUZlazZtdmJRTHNrTzcvdkVic2FVeWlMRVU4Yw/Avatar%20%28TLA%29%20-%20S02%20E01%20-%20The%20Avatar%20State%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/UitFd0ZmRk1Sb2cxT0svLzI1aDc3R2ZrVGhONDJsdWJLaThMTU1uSXkxUQ/Avatar%20%28TLA%29%20-%20S02%20E02%20-%20The%20Cave%20of%20Two%20Lovers%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/aWtEVXl5dGdKb1RUTDVUVlhuZko5Z2h1OFUrS3FReEthS3BYSnZRbjBzYw/Avatar%20%28TLA%29%20-%20S02%20E03%20-%20Return%20to%20Omashu%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/b045dXpvUXlubE5sek1uZWtBaVQ2enBnWDNpYmh6VGJEUXM5UUw4S2sxdw/Avatar%20%28TLA%29%20-%20S02%20E04%20-%20The%20Swamp%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/U1QvQW55YTZoclVHbGVKbmh1VllVSFUwcE9SanF6bi9GVmtZZW5NSHV6cw/Avatar%20%28TLA%29%20-%20S02%20E05%20-%20Avatar%20Day%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/QUhKNVdGTGx6eHlWbXRXK2lQam1QVFIzVHg1R1BOSGhpNVRkb2JtY2ZFcw/Avatar%20%28TLA%29%20-%20S02%20E06%20-%20The%20Blind%20Bandit%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/bXV0cU50QTBWYzlidEYyejB0YkRETms5QndpSmttSmVoZUl2MUZ6cXFKVQ/Avatar%20%28TLA%29%20-%20S02%20E07%20-%20Zuko%20Alone%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/YlFqdjJITTNhUUtOL3Vmdi9KYmZQazJoQVZhR3FIVE9PQklLVUw2YW1Maw/Avatar%20%28TLA%29%20-%20S02%20E08%20-%20The%20Chase%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/OEZWU3NQNWFuV29RWWZXMFo4T3BRR2EyblFGQUpGa0dSdnpMb3hsaXJPaw/Avatar%20%28TLA%29%20-%20S02%20E09%20-%20Bitter%20Work%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/U3g0cjNsQmhEMzdCaS90NzZGOWtlRTJqOGRaSDFocFVPcXNOeFVZaTdEQQ/Avatar%20%28TLA%29%20-%20S02%20E10%20-%20The%20Library%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/OVRQeUNvTDIyRkt0aC9EbDYyWkF2UmE1QWJQenFaS0ZyTGJpRlFwRFNnVQ/Avatar%20%28TLA%29%20-%20S02%20E11%20-%20The%20Desert%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/bDJjNERPaklqVlhNckk1VlNNRnIxUVVnN2JTWjBoeWlRd29maVJ2Tlk0cw/Avatar%20%28TLA%29%20-%20S02%20E12-E13%20-%20The%20Serpent%27s%20Pass%20and%20The%20Drill%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/eUIrS0hyKzRzZXVNOXlSZnlqdXEwM3kyVlkyYU11U2FxQVRQUXQzcW56SQ/Avatar%20%28TLA%29%20-%20S02%20E14%20-%20City%20of%20Walls%20and%20Secrets%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/eVowQ20vVE5UT3JxcWs2V3U2SHVSMDRvTm1NTVFWYm5iNlhLNDhiaWhJbw/Avatar%20%28TLA%29%20-%20S02%20E15%20-%20The%20Tales%20of%20Ba%20Sing%20Se%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/eHh4RTdvQzR4cjZIUVduRW8wVFRjL3N3eTVKdUpDcFpxQ1dRNStwWk5TOA/Avatar%20%28TLA%29%20-%20S02%20E16%20-%20Appa%27s%20Lost%20Days%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/ZnVySUEvMERHSjhMVkMwOTJ4L3BQOEJRZHhzUWh2Vk5DT0l4clJIQ3JjZw/Avatar%20%28TLA%29%20-%20S02%20E17%20-%20Lake%20Laogai%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/aE9YaGxqSk9iaEtacCtrbG1PQm9sNWdIS0cwbitJWXNScTFQSGNsdTVINA/Avatar%20%28TLA%29%20-%20S02%20E18%20-%20The%20Earth%20King%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/ZW1RRHpsSGdWQnhVa1dsMUZ3YkVmZ09JekZlSndXVERPeVhjaTN3U3dZbw/Avatar%20%28TLA%29%20-%20S02%20E19-E20%20-%20The%20Guru%20and%20The%20Crossroads%20of%20Destiny%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/WlkwTTM3NXhGNVdmTUJZUWlKRDNpd3dON2l0QVJmak1iOTdoMDlvYW9iYw/Bending%20Battle%20%28480p%29.mp4
https://debrid.gookie.dev/emN1bTVNamc2TFVNRG5oeWEvT0t6KzZENzBzbGw1RkVUYldWdyt1SFd2VQ/Escape%20From%20The%20Spirit%20World%20Animated%20Graphic%20Novel%20%28480p%29.mp4
https://debrid.gookie.dev/TVJIUWwxYUZ3ZjdRK2ZrcGR2aGFiUzhsbEpGUXFPSWVEUE1sL1F3UTF3QQ/Interview%20With%20Creators%20And%20M.%20Night%20Shyamalan%20%28480p%29.mp4
https://debrid.gookie.dev/N0hESHFCMlIrbGRwaEs0VjBKSlV0UU12MWFXYzV2b2VvbzFqVFVzdHNCZw/Original%20Uncut%20Animatic%20-%20Episode%2021%20-%20The%20Avatar%20State%20%28480p%29.mp4
https://debrid.gookie.dev/emJFaGNhdHh0aEpoTDRpSllUNWlUMkxpeWFjWnBCeitPKzROMHo4NnJoOA/School%20Time%20Shipping%20%28480p%29.mp4
https://debrid.gookie.dev/MXFZZXJtMUhIb1doOEl1dDIrYUt0YlRmNzV5RXhObTJlUGVVR0Y0TjZROA/Swamp%20Skiin%27%20Throwdown%20%28480p%29.mp4
https://debrid.gookie.dev/MkRGUFQzYlNxZXFhVE1YSDNPVmdvU3FaREh5RERLZ1J2MnF2cmRhcTA1QQ/The%20Crossroads%20Of%20Destiny%20%28Sd%29%20Commentary%20By%20Creators%2C%20Cast%20and%20Crew%20%28480p%29.mp4
https://debrid.gookie.dev/MFArK2pKeGwyWWFjWGZCYyt2c29uOWVsMDd2TTNyOCtXcWNwQ25yblBHdw/The%20Essence%20Of%20Bending%20With%20Bryan%20Konietzko%20And%20Sifu%20Kisu%20%28480p%29.mp4
https://debrid.gookie.dev/Wk9ISFY0bXQxQyt3d1dma0NvdFhma2xkWHJYL0FVSTVJaEpXMDUyR2lXNA/The%20Serpent%27s%20Pass%20%28Sd%29%20Commentary%20By%20Creators%2C%20Cast%20and%20Crew%20%28480p%29.mp4
https://debrid.gookie.dev/Z3NjZ3VJVjJla0hlcmd0YmVwcGJKWGNJK2ZseTBNd09PVWswU2p3N2hvbw/Avatar%20%28TLA%29%20-%20S03%20E01%20-%20The%20Awakening%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/ejlVNk5tN0VkcWFlSjBGZEs2NCtNUW1Sb3FDaW1XdWFnOGhXcEM1V3pjQQ/Avatar%20%28TLA%29%20-%20S03%20E02%20-%20The%20Headband%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/ajIrZUhYcnZBaXFOL0JEdmNBdmFXVm55bnh5UHlSNkpYT1lNQllDS28vTQ/Avatar%20%28TLA%29%20-%20S03%20E03%20-%20The%20Painted%20Lady%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/M2hpTXRKdVc0dXkvT0ZOWFRqZnQrMzNzdFBMdTh4NmE5QS9HdkxESWc1NA/Avatar%20%28TLA%29%20-%20S03%20E04%20-%20Sokka%27s%20Master%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/RDJOYmgvU2FxaUd2Z1NLTUl5ZEN2cGthUUNrKytSdnhBNFZad1B6NzFaZw/Avatar%20%28TLA%29%20-%20S03%20E05%20-%20The%20Beach%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/VUdia3ZvUG1Ka2d5N0JlQ1pGSDBacFRsMzFQR3FHbUlicm1WalRUcmJOWQ/Avatar%20%28TLA%29%20-%20S03%20E06%20-%20The%20Avatar%20and%20the%20Fire%20Lord%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/T3NVRE16aEJpbHp4T2dhNzVHZnBMRG9MUm1YOGpnUkxsaUJ2UkVTWHVvVQ/Avatar%20%28TLA%29%20-%20S03%20E07%20-%20The%20Runaway%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/L0tuQlJJczY5akdMT08rd0dwUFlidEc0d09IVjNkMFhHR09GdGw1bHRkbw/Avatar%20%28TLA%29%20-%20S03%20E08%20-%20The%20Puppetmaster%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/TkdZekF3NGhmcjRaTjRuR3U5ZG1ycCt0Wkd5Q1ptVWFIVUJPQ09ER1lQMA/Avatar%20%28TLA%29%20-%20S03%20E09%20-%20Nightmares%20and%20Daydreams%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/aWZYNjc1dVF2ekZxeFBXS3c4U2xpNFY4SmVmMjg4SHhMcUVPcmV6b3FyWQ/Avatar%20%28TLA%29%20-%20S03%20E10-E11%20-%20The%20Day%20of%20Black%20Sun%2C%20Parts%201-2%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/SHdQUzU4TUI2NyttNGFVNVg5Q0RjeUExdkhicndrMGt0T2tPK2hlSlV5QQ/Avatar%20%28TLA%29%20-%20S03%20E12%20-%20The%20Western%20Air%20Temple%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/TTY3TXFOK3VKOXNKUWZKL09hbzdYV1oyTlJ5d2RsK2NCUHNDWlVUT21uTQ/Avatar%20%28TLA%29%20-%20S03%20E13%20-%20The%20Firebending%20Masters%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/Q2RwVEJqUU1UYm5oREIvQ0hQY2l3TnBwVnRBSnNINlU5VWQ1S3VtZXJlRQ/Avatar%20%28TLA%29%20-%20S03%20E14-E15%20-%20The%20Boiling%20Rock%2C%20Parts%201-2%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/QzVXY0pwWHpOL0NKcDJkd05vU1J4aDVEZ0dyMjJZNW9ta2FuYVNvYVpxYw/Avatar%20%28TLA%29%20-%20S03%20E16%20-%20The%20Southern%20Raiders%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/eGRHRWdjVE1JenluUklGMFhQQTBsSUhqZ0ZoM0JYS2h5WGRkN3BSeldjNA/Avatar%20%28TLA%29%20-%20S03%20E17%20-%20The%20Ember%20Island%20Players%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/KzlMdkl6WHZrdUVYTlZYSFh4U2dmblRmWEtCeFo2T0NnOFg4c25aRFZ4WQ/Avatar%20%28TLA%29%20-%20S03%20E18-E21%20-%20Sozin%27s%20Comet%2C%20Parts%201-4%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/TFQ0WnJhby9TamRnZXlNVnVBODRxNFlWWnhyTGFneis1dTFKeVZnbzdNMA/Book%203%20Finale%20Pencil%20Test%20Animation%20%28480p%29.mp4
https://debrid.gookie.dev/bFRBdjZ6b1QxRndTaFVxZlVvNzhHanVsNHFjSjBMME9oV2JPNitnTTAxYw/Into%20The%20Fire%20Nation%20At%20San%20Diego%20Comic-Con%20%28480p%29.mp4
https://debrid.gookie.dev/VVYrNld2NUtCZCsySlUyTG83VnB5N0tWV1ZReFRVRmV3dWZYTnVNT0NSTQ/Menu%20Art%20-%20Disk%201%20%281080p%29.mp4
https://debrid.gookie.dev/Q0gxck05eUhNaGY0b0IxaFl2dmI3L01DN2REdlloRndrbHlCZGdlY0JBVQ/Menu%20Art%20-%20Disk%202%20%281080p%29.mp4
https://debrid.gookie.dev/dlVlb1F1SjJCVWJUU1o4WkRHdFVzcHhoU0NjUEpPc0FmeVhwY1RQVFJUcw/Menu%20Art%20-%20Disk%203%20%281080p%29.mp4
https://debrid.gookie.dev/T293eEhUVThCYkREYnJnbGd5Y0hLVkdnM2N2aU9BZjkyd3EzMVFaeUNIdw/The%20Women%20Of%20Avatar%20-%20The%20Last%20Airbender%20%28480p%29.mp4
https://debrid.gookie.dev/S3NxaHYrM1dJcEhielprNVFWZ0daQ0QwUldINThocVFDS3dlVFZablBscw/Avatar%20%28TLoK%29%20-%20S01%20E01%20-%20Welcome%20to%20Republic%20City%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/QmRBZEtTeHJSeDdTVjJNVGd5RFlIU3NTU1BGeCtLSkx1SDNybm9qaEFrVQ/Avatar%20%28TLoK%29%20-%20S01%20E02%20-%20A%20Leaf%20in%20the%20Wind%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/WE5KZnk2MVo3SmJscnc2YjE5dzRXc0NqZlgzNzE3ckt3YU9YSHMvUGpTcw/Avatar%20%28TLoK%29%20-%20S01%20E03%20-%20The%20Revelation%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/cWs3clBrTzZUeGpxcHdRbmpBMGFyeFRlcU1VU3RXRmVsWVVtaGpRWVhwMA/Avatar%20%28TLoK%29%20-%20S01%20E04%20-%20The%20Voice%20in%20the%20Night%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/WlZlbHNpa3F4QXFOZFBlUE1XbS84NXNwYTQ2K25tZjFicVV6cEkvMmYwRQ/Avatar%20%28TLoK%29%20-%20S01%20E05%20-%20The%20Spirit%20of%20Competition%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/bEgzTmVpUW0zVjZNTndGZkdIdy9vSVltNFg0OXdsZEZVU2YrSFp3Y0ZNTQ/Avatar%20%28TLoK%29%20-%20S01%20E06%20-%20And%20the%20Winner%20Is%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/RHQ1Q2x0OWp3UldDRlNVQjlQK3JVT3F3d3I5cmVYVnRVTWRacDV2VSt5Zw/Avatar%20%28TLoK%29%20-%20S01%20E07%20-%20The%20Aftermath%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/bGlSRmVXZWVRRGR3RE9EaFBvNTJvYXYwcUs3WTltaFFBQTE3cFNBdUFoUQ/Avatar%20%28TLoK%29%20-%20S01%20E08%20-%20When%20Extremes%20Meet%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/Q3JCY28zTGhPVU9zeDhzMlBoQU1CdlJxNlNEbjRDUnZZaVROamFqV2Fyaw/Avatar%20%28TLoK%29%20-%20S01%20E09%20-%20Out%20of%20the%20Past%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/VVN6VEhGa2pLOXVLaCtaTzBOdWZwUWJYV1U2c3dYcWVLUmtPT3JIWEZiVQ/Avatar%20%28TLoK%29%20-%20S01%20E10%20-%20Turning%20the%20Tides%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/VDJWSC85ejdxSVlqVVhuNWVEK0Flb3h3VXV2NlVWbG1maUdMb3Rka0ZSTQ/Avatar%20%28TLoK%29%20-%20S01%20E11%20-%20Skeletons%20in%20the%20Closet%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/Z2tLVFp4a3cwVTZObzFzcWhCc0t5WHAyL2kwY2EyT0Jtb0dFb3dzenUvcw/Avatar%20%28TLoK%29%20-%20S01%20E12%20-%20Endgame%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/WWw1WWFURXg0eTFRb1ZDYUt3ZU0rM2dMNEtSWW5pVHBuZGlJSDNkd0xmcw/Creator%27s%20Favorite%20Animatics%20Scene%20-%20And%20The%20Winner%20Is%20%281080p%29.mp4
https://debrid.gookie.dev/WnROc1BnK3doMDh2YzEwUWwrb2Nsd0R2VW9jdm1ndXFzakdBRnpqYTk3Zw/Creator%27s%20Favorite%20Animatics%20Scene%20-%20Endgame%20%281080p%29.mp4
https://debrid.gookie.dev/aXpiQUxpcDlTT0JpNlhkQzFWWmkyOWpLSTVhNnM4L1dQRkhwbHAyZHBXbw/Creator%27s%20Favorite%20Animatics%20Scene%20-%20The%20Revelation%20%281080p%29.mp4
https://debrid.gookie.dev/aitTNkRxbE52SFZTOFE1QURwOWFycXBNdTMvWW9vMFdad2MzTmFhTllkMA/Creator%27s%20Favorite%20Animatics%20Scene%20-%20The%20Spirit%20Of%20Competition%20%281080p%29.mp4
https://debrid.gookie.dev/UVZYUjFJdldDS1RodEtoU00rc1AwTzF1VktZV0lnWVRudDEzOTZyZGY2Yw/Creator%27s%20Favorite%20Animatics%20Scene%20-%20The%20Voice%20In%20The%20Night%20%281080p%29.mp4
https://debrid.gookie.dev/bzI0S2RvcGZ5bGR2aUM4bEFSbHB4MGc0SXdyTVdPcjh6K2pvNXkybW8yRQ/Creator%27s%20Favorite%20Animatics%20Scene%20-%20Turning%20The%20Tides%20%281080p%29.mp4
https://debrid.gookie.dev/bVpkQ1BySkt0WWlvZFZRK1hraVUvY3ZQT2NwQnd2QzYxY1FBQzNSQXQ4aw/Creator%27s%20Favorite%20Animatics%20Scene%20-%20Welcome%20To%20Republic%20City%20%281080p%29.mp4
https://debrid.gookie.dev/VFQzRXljOHRoeFRMaWNEZDRrOHI0eXVzNmh4YzRQbXF2R29pODVJcCt2bw/Creator%27s%20Favorite%20Animatics%20Scene%20-%20When%20Extremes%20Meet%20%281080p%29.mp4
https://debrid.gookie.dev/YjZudDNQQ3hVM3FSVC9OdlZ5YUNSZ21DbHF4WEVrRmREanNvdU5aSXFuNA/Menu%20Art%20%281080p%29.mp4
https://debrid.gookie.dev/MkdKNGRkVHpQVzdQekVNeHlERkpKK2c4Ukc3b1ZIeDRkMGRFTWp0M1dKNA/The%20Making%20Of%20A%20Legend%20-%20The%20Untold%20Story%20%281080p%29.mp4
https://debrid.gookie.dev/TFQyc2dCenY4eThhaExiVnBrczlubjF6c1BLVkZhK3hvRkVubDVlaXJRSQ/Avatar%20%28TLoK%29%20-%20Republic%20City%20Hustle%2C%20Part%201%20of%203%20%281080p%29.mp4
https://debrid.gookie.dev/dEdyTzFBRzcvRE1HNk1Qd1AwVmlmVkhQc1kzMlRPMC84YlJpajh1V2R3QQ/Avatar%20%28TLoK%29%20-%20Republic%20City%20Hustle%2C%20Part%202%20of%203%20%281080p%29.mp4
https://debrid.gookie.dev/QnZOUXg3V0JqeFRWc2Z3WWJGcDhRcE01MzNuOHdEVVdpTjlUQzRlOFlnRQ/Avatar%20%28TLoK%29%20-%20Republic%20City%20Hustle%2C%20Part%203%20of%203%20%281080p%29.mp4
https://debrid.gookie.dev/aGpOZmVESEtVMUF5a3N5YytmQXA0blNoQ0RjdUlrTytaMDRENEw3RVk2dw/Avatar%20%28TLoK%29%20-%20S02%20E01%20-%20Rebel%20Spirit%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/czBjSjdKd0FYalFaaHloVjdobHBEdU9ZOEJ6YURDaU9ZT3pMaERON2FzVQ/Avatar%20%28TLoK%29%20-%20S02%20E02%20-%20The%20Southern%20Lights%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/bFYrcXJrOXBJUmFlUWp1Ujh5djhLRWE3V2VqMWZkUXcyL0dVNTVaczFzbw/Avatar%20%28TLoK%29%20-%20S02%20E03%20-%20Civil%20Wars%2C%20Part%201%20of%202%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/S3JRSmEyNXRkUUdWY1BxRGdMbDdQSmVNOWZKMldXckZDdnp2ejV5Q0xadw/Avatar%20%28TLoK%29%20-%20S02%20E04%20-%20Civil%20Wars%2C%20Part%202%20of%202%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/a3N6U3ZoTUptcFovekI2Slo0REVVQldyNndTNUZEMzh2aXpyQllJaE5PMA/Avatar%20%28TLoK%29%20-%20S02%20E05%20-%20Peacekeepers%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/Tkl4NDBsaWFaWkl6SVZUVzkwN0tyamttZTJzZmRYSHRjZUJuVjIxMUJoUQ/Avatar%20%28TLoK%29%20-%20S02%20E06%20-%20The%20Sting%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/M29yRXlVQzIyY1hmai92RTg0NkhiZTNnMkRYWVMwTm9lT21MdXA4Vmthdw/Avatar%20%28TLoK%29%20-%20S02%20E07%20-%20Beginnings%2C%20Part%201%20of%202%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/elB4cEFsTG1qRVY0aFJVYzlxdmd2aGlWb2RRbkh0andzaWN5dVNtUk82VQ/Avatar%20%28TLoK%29%20-%20S02%20E08%20-%20Beginnings%2C%20Part%202%20of%202%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/VW1CMFEycGF0RmlMaTlOUlVjbk4wWmR5UUt4NGtRa1RsblFXd2NMQ0FMOA/Avatar%20%28TLoK%29%20-%20S02%20E09%20-%20The%20Guide%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/alRoRFkwYUdQMThzVGE3d3FnN0pNejRLTmM1TVBwcXBXcW9tRjFvalo3dw/Avatar%20%28TLoK%29%20-%20S02%20E10%20-%20A%20New%20Spiritual%20Age%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/cHpVZ3hiSEQ3RWRBSlFxM2l2Qmovb1p5Mi9Ncis5cmNjVDA1eWpVeUE5MA/Avatar%20%28TLoK%29%20-%20S02%20E11%20-%20Night%20of%20a%20Thousand%20Stars%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/a25DdDN1b2l3RFFScVJUV2NvT3IxTnVINlFyZVQ4bVBoWjg0OFhzenN2aw/Avatar%20%28TLoK%29%20-%20S02%20E12%20-%20Harmonic%20Convergence%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/TlBZNktmZUVwYTZreWNzakZmOVFvaDl6cE5obFhCMUprNXB6MjJGTFU4MA/Avatar%20%28TLoK%29%20-%20S02%20E13%20-%20Darkness%20Falls%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/NlRqTCtZOWt6SE5MWmxHcVlHalRHc1FyejNuRE1LaFd5Z2RMV09GTEdIUQ/Avatar%20%28TLoK%29%20-%20S02%20E14%20-%20Light%20in%20the%20Dark%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/aXhyWCtaYWt3YkxwRlhDYTN2YXRldzJ6SE5uNUpPWm43ZVlGQmlrazZCSQ/A%20New%20Spiritual%20Age%20%281080p%29.mp4
https://debrid.gookie.dev/TUpNTzBCMDhCVlQ4R1JuSW5LUVE5S0xLcldBeUJCZEdiTXJmczYyVmJsMA/Beginnings%2C%20Part%201%20%281080p%29.mp4
https://debrid.gookie.dev/MWx4YStyMy9yS3NQT0tSN1VUNTlYekVyVjFxcDJNSXlDVE43eWVaeE9TNA/Beginnings%2C%20Part%202%20%281080p%29.mp4
https://debrid.gookie.dev/eVpmR1Jic3R4dmdXUDNFbnd5dE9UM25aT2ZSNytzd3NkdUhvclU4M3lsaw/Civil%20Wars%2C%20Part%201%20%281080p%29.mp4
https://debrid.gookie.dev/OFhyVDFyZzJ5dTJZdXhJR0VKKzQ3Y2s2b0NOaWpDbURkT05mZ080cDZrZw/Civil%20Wars%2C%20Part%202%20%281080p%29.mp4
https://debrid.gookie.dev/cXlBRVRrMGJWb3JSY2pZOXJUSnZ1SmQ4bDJmZ2E3cGw0d3lCZ1lsSm9tcw/Darkness%20Falls%20%281080p%29.mp4
https://debrid.gookie.dev/WXJqRTE3ZkJTWURtL3FJeWdOWGxBbXVoZm94eWhadzJEb05HTWlybWNaTQ/Feuding%20Spirts%20Korra%E2%80%99s%20Family%20%281080p%29.mp4
https://debrid.gookie.dev/L0lKbkFkaEZDdnVTbEp6UW1FUkpIeUtrTUp5dkJTajlnci95NUQ0c0RiQQ/Harmonic%20Convergence%20%281080p%29.mp4
https://debrid.gookie.dev/WnJjT2NmOWZ3NUxNWE5zYUM3czEvNm1nNmFzV2xiQjNaN0dDNDUwQmdPUQ/Inside%20The%20Book%20Of%20Spirts%20%281080p%29.mp4
https://debrid.gookie.dev/VUo0WWYydnZ2Q3E2N21lVmtZN3JFS2p1bVpmb0ZVell1bGhUZzhoYS9QVQ/Kindred%20Spirts%20Tenzin%E2%80%99s%20Family%20%281080p%29.mp4
https://debrid.gookie.dev/QXNIbjFvNVdZeU5xbW9ENWZ1aE1HYUFnYkpkeUZ6cWVza2kvZ0t2Q3loWQ/Light%20In%20The%20Dark%20%281080p%29.mp4
https://debrid.gookie.dev/Yk85clpMOVRkUXdjNWRIZktiNmdJOVJZM1hwRDRJQXJLcmFMVDJUaWc0bw/Menu%20Art%20Disk%201%20%281080p%29.mp4
https://debrid.gookie.dev/c1FudDhCR1p1OUNVeGdlbi96U0xNa3NTajNMM0hJaHM2c2xjQ05MVTRGdw/Menu%20Art%20Disk%202%20%281080p%29.mp4
https://debrid.gookie.dev/U1g3MGZFbjdQY0twQ1dHRzg3bFB5TmFselV4U1Y4V3NITGxQK0YvRWNNcw/Night%20Of%20A%20Thousand%20Stars%20%281080p%29.mp4
https://debrid.gookie.dev/cEhCSkR4NVAxYkF5WS94aVlyTkN2NmlZR1g4TVdhSjZuNHA2L2pyTTNzOA/Peacekeepers%20Scene%20%281080p%29.mp4
https://debrid.gookie.dev/STV1SEF4VTlaRlcweVhiNjl3NWI5WGNNcWpPTUhPWDgrRHVEVEVCdlRNaw/Rebel%20Spirt%20Scene%201%20%281080p%29.mp4
https://debrid.gookie.dev/TjV4U0gxemxlZVdwZTJGMFFEV0NGYlJFaDVaQks5VGQ0TWJKbkErWWJNVQ/Rebel%20Spirt%20Scene%202%20%281080p%29.mp4
https://debrid.gookie.dev/cGs4RVE3NWh4YXlXQmd1aTVRQU1rb2lSbzRydlBoMDAycm0rL1ZjZ1ZpNA/The%20Guide%20%281080p%29.mp4
https://debrid.gookie.dev/NTQvTGN1QmNHNHV3NVNJS242bFdFWHR6clZ4RHZBdWIyKzNibnp4Q1hEaw/The%20Re-Telling%20Of%20Korra%E2%80%99s%20Journey%20%281080p%29.mp4
https://debrid.gookie.dev/eFY4Z2lnK0ZrUXBPTG9ZWmVOd1lCSUpocmhEakRPOFZwYXRZbitCTEJ0UQ/The%20Southern%20Lights%20Scene%201%20%281080p%29.mp4
https://debrid.gookie.dev/cjRwd3R6dVNoTXZNOEhVSTBJdGx5ekJsSFNQYWc3Zk95RHpaUHV5V01pNA/The%20Southern%20Lights%20Scene%202%20%281080p%29.mp4
https://debrid.gookie.dev/ZFhnYVhDcU9ZV2s4QVpSbGVnQUg1V1pLb1FWVC9MOWlaYSswM2ZlcDA0Zw/Avatar%20%28TLoK%29%20-%20S03%20E01%20-%20A%20Breath%20of%20Fresh%20Air%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/aW5CZW0reE01dEdkejBLTDlEdk83S3o4d1NTdExSR1F0UG5BT2tzVXlqaw/Avatar%20%28TLoK%29%20-%20S03%20E02%20-%20Rebirth%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/VDlqOHJBNnR2R1F0TzlOVzZINzByWGk3Yjh6S1NjeVM2RUtyaVVkb01HOA/Avatar%20%28TLoK%29%20-%20S03%20E03%20-%20The%20Earth%20Queen%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/NGhPOEV2TDIxZFNCSUdMNEIzSWlhSmZOK3NrLzRLUGJSY1BScWtXQ3UvMA/Avatar%20%28TLoK%29%20-%20S03%20E04%20-%20In%20Harm%27s%20Way%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/Nkk1WUlNV3RoVVRWd2tHZHB6VjgwRmN6NFFIbG9vM0crWFZuTFM1UzBOSQ/Avatar%20%28TLoK%29%20-%20S03%20E05%20-%20The%20Metal%20Clan%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/aFZOWWl3Tm84VklDdzZZcThrVWwxRDlIbTlWUGVpSEtmcHgvd1hDNHVpNA/Avatar%20%28TLoK%29%20-%20S03%20E06%20-%20Old%20Wounds%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/QVc1dzJULzdDbHpJaUhVNFExUzBFM2ZmQ0ZBcDNXTkNRd3BYWkZJTTBEaw/Avatar%20%28TLoK%29%20-%20S03%20E07%20-%20Original%20Airbenders%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/c2JjWWQxZEsrYjBMN3g3M0pBTHB4c0FpOVl6RlZXa1VtSnlGYUpXOHY1SQ/Avatar%20%28TLoK%29%20-%20S03%20E08%20-%20The%20Terror%20Within%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/WnMwaFEyMmpEaXlGWW8yTjVmS3ZQY09PeWdyV2ZJRjFtd0lWSEExNUx0QQ/Avatar%20%28TLoK%29%20-%20S03%20E09%20-%20The%20Stakeout%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/NUZtMnZtK1luWFhtNHlaWjRGSmp4VysrN1RGYjBGQ0YyZnRQMUhFZitQQQ/Avatar%20%28TLoK%29%20-%20S03%20E10%20-%20Long%20Live%20the%20Queen%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/dUhZQWVLZU8zRGxsbnU3aTVKRzJjQ2x6dVBZUVphMmIvQXVjL21ZcVFiWQ/Avatar%20%28TLoK%29%20-%20S03%20E11%20-%20The%20Ultimatum%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/RkxJbkFvbWovRzVFSU5ZUEI4c3RjSTdhZTRKcTVOVkJ3U0NCVTBtY2YyRQ/Avatar%20%28TLoK%29%20-%20S03%20E12%20-%20Enter%20the%20Void%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/bHErRmFKdzRCblB6TlVOelk0eUFGS25NZFBYVmgzQi9TdHVicmtnWVN6aw/Avatar%20%28TLoK%29%20-%20S03%20E13%20-%20Venom%20of%20the%20Red%20Lotus%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/LzhnWm80dS90akFMWUFsQ1RHMUp2VTFrMGVsNk9hZzFNeHZDSGlvOTFHWQ/A%20Breath%20Of%20Fresh%20Air%20%281080p%29.mp4
https://debrid.gookie.dev/aHhVL0tpbEl0WkdaYThMNndZNi8yVkxwKzdqbDVkajNBQjlCT3JzMTZZMA/Enter%20The%20Void%20%281080p%29.mp4
https://debrid.gookie.dev/WEt0SDV2NmdwZHcyU2hGQTFZYnROZnNHTEI4dFp4ejk2NTJEUjE5ZlAwTQ/In%20Harm%E2%80%99s%20Way%20%281080p%29.mp4
https://debrid.gookie.dev/VmxJdVk4MTFFS0hJYnBtTVltdVo5RlhSOWdqL3gyaDZmTWp5amFoa0pjSQ/Long%20Live%20The%20Queen%20%281080p%29.mp4
https://debrid.gookie.dev/R1hvdVc2V0hZSnczdXQ0SnhsYWo4YzdYKzNieVVnVUYvTDl4b2I1TCt3Yw/Menu%20Art%20Disk%201%20%281080p%29.mp4
https://debrid.gookie.dev/akJ4SGJXbXMzcDAzYmRkUjJJWHBvTk0yQmR6K3pkSElvQmFWbHlFeC81Zw/Menu%20Art%20Disk%202%20%281080p%29.mp4
https://debrid.gookie.dev/VXJiL1J4Tm5GMHluNWF2eU1FY2tQRXUrTThVNnVMbmw1dnlRbSsyckJNOA/Old%20Wounds%20%281080p%29.mp4
https://debrid.gookie.dev/NWZwM1dFZTVTeUhPaGZqcnF3N3FXL0l1ZXlCbzhvNEVDdDRTZEFpTG5sdw/Original%20Airbenders%20%281080p%29.mp4
https://debrid.gookie.dev/MDh0b1NKVnlNSDkwbnVZQ0dKcEgwUk1rR0o1SUV2U090VmRybHk2S3lLbw/Rebirth%20%281080p%29.mp4
https://debrid.gookie.dev/clB4c0pOd1BjMFlyN2l3VVoxbnltQ3RYcGhLeGJySW5wUklNRzU5dW9LWQ/The%20Earth%20Queen%20%281080p%29.mp4
https://debrid.gookie.dev/Y0xTZElKZCtuTkwwbFhxWEFFUUdUbzVTSE5ZUzdYQUQ5QXlZdWErM1gyWQ/The%20Metal%20Clan%20%281080p%29.mp4
https://debrid.gookie.dev/dEpQWjNrbGRUS1ErOEFGbS9tS1hDdC9LU3VVL0JOKy9CVlMxU3JEN1RCVQ/The%20Stakeout%20%281080p%29.mp4
https://debrid.gookie.dev/OWlkQ2ZSMGhpS3FJMDd2Qk5hcWpTeWZvSXhLZGVLUVY5TUlBYy9KNFFZOA/The%20Terror%20Within%20%281080p%29.mp4
https://debrid.gookie.dev/US9hUHVKVlNlZU1NQmRSTkxwL1phbXV1UTdkR2tpSkt4WEJBbTh4WDRHUQ/The%20Ultimatum%20%281080p%29.mp4
https://debrid.gookie.dev/SUlZcGlZczFGaFVBSnRXSkdZY29kNm5KT0NIOXBVa0tDenNjeXdSbk90SQ/Venom%20Of%20The%20Red%20Lotus%20%281080p%29.mp4
https://debrid.gookie.dev/VFZ2MXhodHg0eFFuZ3kzOVgwamdWc3RsU2prYytkaXorWDJtL1dxMVA1Zw/Avatar%20%28TLoK%29%20-%20S04%20E01%20-%20After%20All%20These%20Years%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/SFRrdGRwMDFDc1VBb015Y1FkcUpBSUp2bWZUdG5qSm94ZTB3THRyVUREOA/Avatar%20%28TLoK%29%20-%20S04%20E02%20-%20Korra%20Alone%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/d3Y2VkxnRUlqOGpzSEpaZitMemFmdkd5VlJ1TWtuK29wOWNTN3VHb0FuYw/Avatar%20%28TLoK%29%20-%20S04%20E03%20-%20The%20Coronation%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/cnJxamVwWHVobm1rT3p4dDlJRWNTMzA3Zi9wZkVraHluZ3BCdnUraUFlRQ/Avatar%20%28TLoK%29%20-%20S04%20E04%20-%20The%20Calling%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/eHNhVDQwQzk4dGI3TG56Lzc4cHl6eVUrVkV0b1krdmw2MitkTlAybERlTQ/Avatar%20%28TLoK%29%20-%20S04%20E05%20-%20Enemy%20at%20the%20Gates%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/TUZraTlhODc4S29jSUl6OFd6Q2N1M21EaHpNMEY5RFJwM0hWTk1CZWlqbw/Avatar%20%28TLoK%29%20-%20S04%20E06%20-%20The%20Battle%20of%20Zaofu%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/d2xqQWNoeS92Slp1clU4SG1DMTBMRngyNUVxaDFxU1hRcjRrZWtYdG9ZNA/Avatar%20%28TLoK%29%20-%20S04%20E07%20-%20Reunion%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/cC9Da2VpNFlCdVNPZituWHZhRDZ1UFp1alh0TFdiOHJ0bkFNL3hRb0ZvOA/Avatar%20%28TLoK%29%20-%20S04%20E08%20-%20Remembrances%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/aXhOQklzNjhpNjBSTHZQMFlGeU5ERU43NjNGUGlpa3JmWlVFeVlHcTl3bw/Avatar%20%28TLoK%29%20-%20S04%20E09%20-%20Beyond%20the%20Wilds%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/eEJQTGEvVW9DR2tyTUU1R0NPMHFLLzlNdEhqYlRlZDFlZTh6Q0xjQjlJRQ/Avatar%20%28TLoK%29%20-%20S04%20E10%20-%20Operation%20Beifong%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/bHN1YzFXUmhNUXYrUGQrd0Z0eHRUOXZoYk1pT3pvZy9VNWhtV2JJUU80MA/Avatar%20%28TLoK%29%20-%20S04%20E11%20-%20Kuvira%27s%20Gambit%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/ZWlnQ0VBOTIrangxTGVmRHJpencyZUp5Zm52RGcwU29vWDRtZlhYbWc5WQ/Avatar%20%28TLoK%29%20-%20S04%20E12%20-%20Day%20of%20the%20Colossus%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/RDUrRkJtNzBnTWc5Q2pOL1locFM1OWt3bi9seUlhNTRhaWp6WXZhMm9SRQ/Avatar%20%28TLoK%29%20-%20S04%20E13%20-%20The%20Last%20Stand%20%281080p%20-%20BluRay%29.mp4
https://debrid.gookie.dev/eVIvTUtrMDZ2d3RmZWlBellZRGVMT3ZublJ6bXJFRWt2UDlKUGR1SHRyYw/2014%20Comic-Con%20Panel%20%281080p%29.mp4
https://debrid.gookie.dev/bnpJenNSaEEvaGg0RFZVSDc0SXVCckd1cXgxdm0xK2Jtc24xRkZ0L3NaUQ/Kuvira%20Vs.%20Prince%20Wu%20%281080p%29.mp4
https://debrid.gookie.dev/SmJMYmJNVDFvSG9YRW9tOVlUNnM0ZFZHSkdFZTBheVUvWFJrdTExcXUwZw/Menu%20Art%201%20%281080p%29.mp4
https://debrid.gookie.dev/aytJSjkrSzRnZWE3dVQ1MS9lME9jMjhFZDU3eEh3cjZ1UjRpUHUzeWVTWQ/Menu%20Art%202%20%281080p%29.mp4
https://debrid.gookie.dev/dW9RQ1RjOG43YmNTcEJ4MEJHR1drMXFkc3lzYkFRN2lrSlFHU0dUdHd5NA/The%20Making%20Of%20A%20Legend%20-%20The%20Untold%20Story%20Part%202%20%281080p%29.mp4
https://debrid.gookie.dev/Yk1UR01tOEd0TElOTUcyN1BmOHFHelpxRHJtbFZjRWVTUHo5Mk1CNmhRRQ/Avatar%20-%20The%20Last%20Airbender%20Movie%20%282010%20-%201080p%20BluRay%29.mp4
"""

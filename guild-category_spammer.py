import requests
import time

token = ""
channelid = ""
headers = {
    "authorization": token
}
data = {
    "name": "josh poop",
    "permission_overwrites": [],
    "type": "4"
}
url = f"https://discord.com/api/v9/guilds/{channelid}/channels"

while True:
    r = requests.post(url, headers=headers, json=data)
    print(f"Response Headers: {r.headers}\r\n\r\nResponse Text: {r.text}\r\n\r\nResponse Code: {r.status_code}")
    time.sleep(1)

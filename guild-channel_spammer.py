# You must have permission to create channels in a server to use this.

import requests
import json
import time

token = ""
headers = {
    "authorization": token
}
guild_id = input("Guild ID: ")
url = f"https://discord.com/api/v9/guilds/{guild_id}/channels"
r = requests.get(url, headers=headers)
channels = json.loads(r.text)
for channel in channels:
    if channel["name"] == "josh poop":
        for _ in range(10):
            data = {
                "name": "josh poop",
                "parent_id": channel["id"],
                "permission_overwrites": [],
                "type": "0"
            }
            requests.post(url, headers=headers, json=data)
            time.sleep(1)

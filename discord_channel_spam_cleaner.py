from time import time
import requests
import json
import time

token = ""
guild_id = ""
headers = {
    "authorization": token
}
r = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers)
response_json = json.loads(r.text)
for channel in response_json:
    if channel["name"] == "josh-poop":
        d = requests.delete(f"https://discord.com/api/v9/channels/{channel['id']}", headers=headers)
        print(d.text)
        #time.sleep(1)

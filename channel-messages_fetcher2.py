import requests
import json

token = ""
headers = {
    "authorization": token
}

def get_messages(channel_id, skipfrom=None):
    fetched = 0
    lastid = None
    while True:
        if fetched == 0 and skipfrom == None:
            url = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=50"
        else:
            url = f"https://discord.com/api/v9/channels/{channel_id}/messages?before={lastid}&limit=50"
        response_text = requests.get(url, headers=headers).text
        response_json = json.loads(response_text)
        fetched += len(response_json)
        if len(response_json) == 0:
            break
        #print(len(response_json))
        for message in response_json:
            lastid = message["id"]
            if message["content"] == "":
                continue
            print(f"{message['author']['username']}: {message['content']}")

get_messages(612682182481216680)

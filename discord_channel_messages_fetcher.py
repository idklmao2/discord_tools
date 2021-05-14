#Version = 1.0.0
#Expect me to create another version of this piece of code.
import requests
import json

token = "Obviously your authorization token here. Can be found from network tab in browser developer mode."
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
        print(len(response_json))
        for message in response_json:
            lastid = message["id"]
            print(message["content"])

get_messages(6176821824811823280)

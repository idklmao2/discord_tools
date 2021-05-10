import requests
import time

headers = {"authorization": "your authorization token here"}
texts = ["nub", "poop", "pee", "idjat", "josh", "josh nub"]

def changeStatus(string):
    data = {
        "custom_status": {
            "text": string
        }
    }
    req = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=data)

while True:
    for text in texts:
        changeStatus(text)
        time.sleep(2)

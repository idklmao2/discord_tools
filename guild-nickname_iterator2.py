import requests
import time

token = ""
server_id = input("Server ID: ")
member_id = input("Member ID: ")
url = f"https://discord.com/api/v9/guilds/{server_id}/members/{member_id}"
texts = ["test1", "test2", "test3"]

while True:
    for text in texts:
        data = {
            "nick": text
        }
        headers = {
            "authorization": token
        }
        r = requests.patch(url, json=data, headers=headers)
        #print(r.text)
        #print(r.status_code)
        time.sleep(2)

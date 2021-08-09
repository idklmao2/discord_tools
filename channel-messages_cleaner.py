import threading
import requests
import json
import time
import sys

token = input("Token: ")
headers = {
    "Authorization": token
}
myid = None


active_threads = 0
max_threads = 10

def getid():
    try:
        r = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
        rj = json.loads(r.text)
        if not "id" in rj:
            print("Invalid token")
            sys.exit()
        return rj["id"]
    except Exception as e:
        print(f"getid error: {e}")
        pass

def delete(channel_id, message_id):
    try:
        global active_threads
        active_threads += 1
        r = requests.delete(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}", headers=headers)
        if "You are being rate limited." in r.text:
            delete(channel_id, message_id)
    except Exception as e:
        print(f"delete error: {e}")
        pass
    finally:
        active_threads -= 1

def clean(channel_id):
    try:
        offset = 0
        while True:
            r = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages/search?author_id={myid}&offset={offset}", headers=headers)
            rj = json.loads(r.text)["messages"]
            if "message" in rj:
                print(f"ERROR: {rj['message']}")
                sys.exit()
            offset += 25
            for message in rj:
                message_id = message[0]["id"]
                message_type = message[0]["type"]
                if message_type == 0:
                    while True:
                        if active_threads >= max_threads:
                            continue
                        threading.Thread(target=delete, args=[channel_id, message_id], daemon=True).start()
                        time.sleep(.1)
                        break
            while True:
                if active_threads == 0:
                    break
            if len(rj) < 25:
                break
        while True:
            if active_threads == 0:
                break
    except Exception as e:
        print(f"clean error: {e}")
        pass

myid = getid()
while True:
    try:
        clean(input("Channel ID: "))
    except KeyboardInterrupt:
        sys.exit()

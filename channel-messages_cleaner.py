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

deleted = 0
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
        global deleted
        active_threads += 1
        while True:
            r = requests.delete(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}", headers=headers)
            if r.status_code == 204:
                break
        deleted += 1
        print(f"Deleted {deleted} messages")
    except Exception as e:
        print(f"delete error: {e}")
        pass
    finally:
        active_threads -= 1

def clean(channel_id):
    try:
        while True:
            try:
                r = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages/search?author_id={myid}&channel_id={channel_id}&include_nsfw=true", headers=headers)
                if r.status_code != 200:
                    print(f"Error. Try again!")
                rj = json.loads(r.text)
                print(f"Total Length: {rj['total_results']}")
                print(f"Fetched Length: {len(rj['messages'])}")
                for message in rj["messages"]:
                    message_id = message[0]["id"]
                    message_type = message[0]["type"]
                    if message_type != 3:
                        while True:
                            if active_threads >= max_threads:
                                continue
                            threading.Thread(target=delete, args=[channel_id, message_id], daemon=True).start()
                            time.sleep(.5)
                            break
                while True:
                    if active_threads == 0:
                        break
                if len(rj["messages"]) < 1:
                    break
            except KeyboardInterrupt:
                break
        while True:
            try:
                if active_threads == 0:
                    break
            except KeyboardInterrupt:
                break
    except Exception as e:
        print(f"clean error: {e}")
        pass

myid = getid()
while True:
    try:
        clean(input("Channel ID: "))
        deleted = 0
    except KeyboardInterrupt:
        sys.exit()

import threading
import requests
import random
import time
import sys

try:
    token_file = open("token.txt", "r")
    token = token_file.read().strip()
    token_file.close()
except FileNotFoundError:
    token = input("Token: ")
    token_file = open("token.txt", "w");
    token_file.write(token)
    token_file.close()
    print(f"Token Saved: token.txt")
except Exception:
    pass
headers = {
    "Authorization": token
}

def message(channel_id, message):
    try:
        requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", json={"content": message}, headers=headers)
    except Exception as e:
        print(f"message error: {e}")
        pass

def genchars(length):
    try:
        text = ""
        for _ in range(length):
            if len(text) == length:
                break
            text += "@everyone"
            for _ in range(5):
                number = random.randrange(13000)
                text += chr(number)
        return text
    except Exception as e:
        print(f"genchars error: {e}")
        pass

while True:
    try:
        channel_id = input("Channel ID: ")
        while True:
            try:
                for _ in range(10):
                    threading.Thread(target=message, args=[channel_id, genchars(2000)[:2000]]).start()
                time.sleep(15)
            except KeyboardInterrupt:
                break
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print(f"main error: {e}")
        pass

import threading
import requests
import time

token = "your token here"
texts = ["test1", "test2", "test3"]

def changer(server_id, member_id):
    url = f"https://discord.com/api/v9/guilds/{server_id}/members/{member_id}"
    headers = {
        "authorization": token
    }
    while True:
        try:
            for text in texts:
                data = {
                    "nick": text
                }
                r = requests.patch(url, headers=headers, json=data)
                print(r.text)
                print(r.status_code + "\r\n")
                time.sleep(2)
        except Exception:
            pass

def main():
    server_id = input("Server ID: ")
    member_ids = input("Member IDs: ")
    members = member_ids.split(" ")
    for member in members:
        threading.Thread(target=changer, args=[server_id, member], daemon=True).start()
    input("Press enter to exit.")

if __name__ == "__main__":
    main()

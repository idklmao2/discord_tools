import requests
import json
import sys

def getroblox(user_id):
    try:
        r1 = requests.get(f"https://verify.eryn.io/api/user/{user_id}")
        r2 = requests.get(f"https://api.blox.link/v1/user/{user_id}")
        if "-d" in sys.argv:
            print(f"RoVer: {r1.text}")
            print(f"Bloxlink: {r2.text}")
            return
        rj1 = json.loads(r1.text)
        rj2 = json.loads(r2.text)
        if rj1["status"] == "error":
            print(f"RoVer: {rj1['error']}")
        elif rj1["status"] == "ok":
            print(f"RoVer: {rj1['robloxUsername']}")
        if rj2["status"] == "error":
            print(f"Bloxlink: {rj2['error']}")
        elif rj2["status"] == "ok":
            print(f"Bloxlink: {rj2['primaryAccount']}")
    except Exception as e:
        print(f"getroblox error: {e}")
        pass

while True:
    try:
        getroblox(input("User ID: "))
        print("\r\n")
    except KeyboardInterrupt:
        sys.exit()

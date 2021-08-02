import requests
import json
import sys

token = ""
image_size = 1024
headers = {
    "Authorization": token
}

def getprofile(user_id):
    try:
        r = requests.get(f"https://discord.com/api/v9/users/{user_id}", headers=headers)
        profile = json.loads(r.text)
        if "message" in profile:
            print("ERROR: {profile['message']}")
            return
        user_id = profile["id"]
        username = profile["username"]
        avatar = profile["avatar"]
        discriminator = profile["discriminator"]
        user_tag = f"{username}#{discriminator}"
        avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar}?size={image_size}"
        avatar_text = ""
        banner = ""
        if not profile["avatar"] == None:
            avatar_text = f"\r\nAvatar URL: {avatar_url}"
        if not profile["banner"] == None:
            banner = f"\r\nBanner: https://cdn.discordapp.com/banners/{user_id}/{profile['banner']}?size={image_size}"
        print(f"Tag: {user_tag}{avatar_text}{banner}\r\n\r\n")
    except Exception as e:
        print(f"getprofile error: {e}")
        pass

try:
    while True:
        user_id = input("User ID: ")
        getprofile(user_id)
except KeyboardInterrupt:
    sys.exit()

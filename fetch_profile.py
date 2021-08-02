import requests
import json
import time
import sys

token = ""
image_size = 1024
headers = {
    "Authorization": token
}

def snowflaketoepoch(snowflake):
    try:
        snowflake = int(snowflake)
        convertion1 = snowflake / 4194304 + 1420070400000
        convertion2 = convertion1 / 1000
        return convertion2
    except Exception as e:
        print(f"snowflaketoepoch error: {e}")
        pass

def epochtodate(epoch):
    try:
        return time.strftime("%B %d, %Y %H:%M:%S", time.gmtime(epoch))
    except Exception as e:
        print(f"epochtodate error: {e}")
        pass

def idtodate(user_id):
    try:
        epoch = snowflaketoepoch(user_id)
        datetime = epochtodate(epoch)
        return datetime
    except Exception as e:
        print(f"idtodate error: {e}")
        pass

def getprofile(user_id):
    try:
        r = requests.get(f"https://discord.com/api/v9/users/{user_id}", headers=headers)
        profile = json.loads(r.text)
        if "message" in profile:
            print(f"ERROR: {profile['message']}")
            print(f"Date Creation: {idtodate(user_id)}\r\n")
            return
        user_id = profile["id"]
        username = profile["username"]
        avatar = profile["avatar"]
        discriminator = profile["discriminator"]
        user_tag = f"{username}#{discriminator}"
        avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar}?size={image_size}"
        date_creation = idtodate(user_id)
        avatar_reverse_image = ""
        banner_reverse_image = ""
        avatar_text = ""
        banner = ""
        if not profile["avatar"] == None:
            avatar_text = f"\r\nAvatar URL: {avatar_url}"
            avatar_reverse_image = f"\r\nAvatar Reverse Image: https://www.google.com/searchbyimage?image_url={avatar_url}"
        if not profile["banner"] == None:
            banner_url = f"https://cdn.discordapp.com/banners/{user_id}/{profile['banner']}?size={image_size}"
            banner = f"\r\nBanner: {banner_url}"
            banner_reverse_image = f"\r\nBanner Reverse Image: https://www.google.com/searchbyimage?image_url={banner_url}"
        print(f"Tag: {user_tag}\r\nDate Creation: {date_creation}{avatar_text}{avatar_reverse_image}{banner}{banner_reverse_image}\r\n\r\n")
    except Exception as e:
        print(f"getprofile error: {e}")
        pass

try:
    while True:
        user_id = input("User ID: ")
        getprofile(user_id)
except KeyboardInterrupt:
    sys.exit()

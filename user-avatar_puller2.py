import requests
import json

token = "authorization token here!"
api = "https://discord.com/api/v9/users/"

def getAvatarURL(userid):
    try:
        request = requests.get(f"{api}+{userid}", headers={"authorization": token})
        response = json.loads(request.text)
        if "avatar" in response:
            avatar_url = f"https://cdn.discordapp.com/avatars/{userid}/{response['avatar']}"
            return avatar_url
        else:
            return "Error"
    except Exception:
        return "Error"
        pass

def main():
    while True:
        try:
            userid = input("User ID: ")
            avatarURL = getAvatarURL(userid)
            print(avatarURL)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()

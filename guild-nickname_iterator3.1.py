import socket
import time
import json
import sys
import ssl

token = ""
headers = {
    "Authorization": token
}
s = None

def createSocket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        context = ssl.create_default_context()
        s.connect(("discord.com", 443))
        s = context.wrap_socket(s, server_hostname="discord.com")
        return s
    except Exception as e:
        print(f"createSocket error: {e}")
        pass

def sendHttp(method, path="/", data=None):
    try:
        global s
        if not path.startswith("/"):
            path = "/" + path
        http = f"{method} {path} HTTP/1.1\r\nHost: discord.com\r\nAuthorization: {token}\r\nContent-Type: application/json\r\nContent-Length: {len(json.dumps(data))}\r\n\r\n"
        http += json.dumps(data)
        s.send(http.encode())
    except Exception as e:
        print(f"sendHttp error: {e}. Recreating socket...")
        del s
        s = createSocket()
        pass

def changeNick(guild_id, nickname):
    try:
        sendHttp("PATCH", f"/api/v9/guilds/{guild_id}/members/@me", {"nick": nickname})
    except Exception as e:
        print(f"changeNick error: {e}")
        pass

def main():
    try:
        global s
        guild_id = input("Guild ID: ")
        nickname = input("Nickname: ")
        s = createSocket()
        while True:
            current_nick = ""
            for i in nickname:
                current_nick += i
                changeNick(guild_id, current_nick)
                time.sleep(1.5)
            for i in range(len(nickname) - 1):
                current_nick = current_nick[1:]
                changeNick(guild_id, current_nick)
                time.sleep(1.5)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()

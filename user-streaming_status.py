import websocket
import json
import time
import sys

token = ""
ws = websocket.WebSocket()
ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
hello = json.loads(ws.recv())
heartbeat_interval = hello['d']['heartbeat_interval']
gamejson = {
    "name": "Alper",
    "type": 1,
    "url": "https://www.twitch.tv/Alper"
}
auth = {
    "op": 2,
    "d": {
        "token": token,
        "properties": {
            "$os": sys.platform,
            "$browser": "RTB",
            "$device": f"{sys.platform} Device"
        },
        "presence": {
            "game": gamejson,
            "status": "Online",
            "since": 0,
            "afk": False
        }
    },
    "s": None,
    "t": None
    }
ws.send(json.dumps(auth))
ack = {
        "op": 1,
        "d": None
    }
while True:
    time.sleep(heartbeat_interval/1000)
    try:
        ws.send(json.dumps(ack))
    except Exception:
        break

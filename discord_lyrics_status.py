import requests
import time

url = "https://discord.com/api/v9/users/@me/settings"
token = "YOUR TOKEN HERE"
texts = []
lyrics = """
Why you mad, why you mad? Why you mad, why you mad?
That's all I wanna know
You're lookin' like a joke, dry humor at the most
Steady chokin' on your shade, like a dick in your throat
Well, if you're gonna throw shade my way
Maybe you should throw with a little more aim
It's a cold day in hell when they dirty up your name
They don't got no business talkin' in the first place, I'm freezin'
""".strip()
for line in lyrics.splitlines():
    texts.append(line)

headers = {
    "authorization": token
}

while True:
    try:
        for text in texts:
            data = {
                "custom_status": {
                    "text": f"🎵{text}🎵"
                }
            }
            r = requests.patch(url, headers=headers, json=data)
            time.sleep(3)
    except KeyboardInterrupt:
        break
    except Exception:
        pass

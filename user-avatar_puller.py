import clipboard
import discord
client = discord.Client()

@client.event
async def on_ready():
    while True:
        userid = input("User ID: ")
        user = await client.fetch_user(userid)
        print(user.avatar_url)
        clipboard.copy(str(user.avatar_url))

client.run("your authorization token here", bot=False)

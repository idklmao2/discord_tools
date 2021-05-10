import discord
client = discord.Client()

@client.event
async def on_ready():
    user = await client.fetch_user(userid)
    async for message in user.history(limit=99999):
        if message.is_system():
            continue
        if message.author.id == client.user.id:
            await message.delete()

client.run("your token here", bot=False)

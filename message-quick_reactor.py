import discord
client = discord.Client()

token = ""
emoji_list = ["🇫", "🇺", "🇨", "🇰"]

@client.event
async def on_ready():
    channel = await client.fetch_channel(input("Channel ID: "))
    while True:
        message_id = input("Message ID: ")
        for emoji in emoji_list:
            await channel.get_partial_message(message_id).add_reaction(emoji)

client.run(token, bot=False)

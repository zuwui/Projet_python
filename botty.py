import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run("MTAzOTE2MTc3MTQzMDI0ODU0MA.G9prAT.HxeRQm4EJeQA9YFdf7r3gSUIArxoJZp4HGN5Q0")
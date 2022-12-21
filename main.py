import discord
import json

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

    if message.content.startswith('$'):      
        from ClassGestionnaireCommandes import GestionnaireCommandes
        
        # print(message.author.roles)
        
        # We get the commandManager
        gestionnaireCommandes = GestionnaireCommandes()
        
        # We get the main command
        commandName = message.content[1:].split(" ")[0]
        
        # We get all the parametres
        commandParametres = message.content[1:].split(" ")[1:]
        
        # We get the result of the command
        responseCommand = gestionnaireCommandes.execCommand(commandName, commandParametres, message)
        
        if(responseCommand is not None):
            await message.channel.send(responseCommand)
        else:
            await message.channel.send(responseCommand)
        
# We open the JSON file
dataFile = open('./data.json')

# We return the file as a JSON object
dataJsonObject = json.load(dataFile)

# We get the command path
token = dataJsonObject["token"]      

# We start the discord bot with our token
client.run(token)

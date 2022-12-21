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
        responseCommand = await gestionnaireCommandes.execCommand(commandName, commandParametres, message, client)
        
        #get channel of the message sender
        channel = message.channel

        if(responseCommand is not None):
            if "embed" in str(responseCommand):
                await channel.send(embed=responseCommand)
                return
            await channel.send(responseCommand)
        else:
            print("Command invalid")
        
# We open the JSON file
dataFile = open('./data.json')

# We return the file as a JSON object
dataJsonObject = json.load(dataFile)

# We get the command path
token = dataJsonObject["token"]      

# We start the discord bot with our token
client.run(token)


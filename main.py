import discord
import shutil

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
        
        # We get the commandManager
        gestionnaireCommandes = GestionnaireCommandes()
        
        # We get the main command
        commandName = message.content[1:].split(" ")[0]
        
        # We get all the parametres
        commandParametres = message.content[1:].split(" ")
        del commandParametres[0]
        
        
        responseCommand = gestionnaireCommandes.execCommand(commandName, commandParametres)
        
        if(responseCommand is not None):
            print(responseCommand)
        else:
            print("Command invalid")
        
            

client.run("MTAzOTE2MTc3MTQzMDI0ODU0MA.G9prAT.HxeRQm4EJeQA9YFdf7r3gSUIArxoJZp4HGN5Q0")
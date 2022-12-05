import json
import discord


def help(commandParametres):
    
    # We open the JSON file
    dataFile = open('./commandsConfig.json')

    # We return the file as a JSON object
    dataJsonObject = json.load(dataFile)
    commands = dataJsonObject["commands"]
    if commandParametres:
        return commandEmbed(dataJsonObject, commandParametres[0]) 

    embed = discord.Embed(title="Bot commands", description="Welcome to the help options, here all the comands", color=discord.Color.blue())
    embed.set_thumbnail(url="https://i.ibb.co/GxzcHHC/pngwing-com.png")
    embed.set_footer(text=dataJsonObject["info"])

    for key in commands:
        command = commands[key]
        embed.add_field(name=f"Commande {key}", value=command["baseCommand"], inline=True)
        embed.add_field(name="Description", value=command["description"], inline=True)
        embed.add_field(name='\u200B', value= '\u200B',inline=False)
    return embed


def commandEmbed(dataJsonObject, key):
    commands = dataJsonObject['commands']
    if key not in commands.keys():
        return f"The specified command is invalid, valids commands are : {', '.join(commands.keys())}"
    command = commands[key]
    embed = discord.Embed(title=key.capitalize(), description=command["description"], color=discord.Color.red())
    embed.set_image(url=command["image"])
    embed.add_field(name="Base command", value=command["baseCommand"], inline=False)
    embed.set_footer(text=dataJsonObject["info"])
    if command["subCommands"]:
        embed.add_field(name='\u200B', value= '\u200B',inline=False)
        embed.add_field(name='Subcommands', value= '\u200B',inline=False)
        i=0
        subCommands = command["subCommands"]
        for subCommandKey in subCommands:
            embed.add_field(name=subCommands[subCommandKey]["command"], value=subCommands[subCommandKey]['description'],inline=False)
    return embed
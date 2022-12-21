import discord
from discord import FFmpegPCMAudio


async def join(message):
    voiceTrue = message.author.voice
    if voiceTrue is None:
        return "Vous n'êtes pas dans un channel vocal"
    await message.author.voice.channel.connect()
    return "J'ai rejoins votre channel vocal"



async def leave(message, client):
    voiceTrue = message.author.voice
    try:
        await client.voice_clients[0].disconnect()
        return "J'ai quitté votre channel vocal"
    except:
        return 'Je ne suis pas dans un channel vocal'


async def pause(message, client):
    voice = discord.utils.get(client.voice_clients, guild = message.guild)
    if voice.is_playing():
        voice.pause()
        return "I will pause sir !"
    else:
        return "No songs are playing right now"


async def resume(message, client):
    voice = discord.utils.get(client.voice_clients, guild = message.guild)
    if voice.is_paused():
        voice.resume()
        return "Let's resume it !"
    else:
        return "No songs are paused"


async def stop(message, client):
    voice = discord.utils.get(client.voice_clients, guild = message.guild)
    voice.stop()
    return "Music stop"


async def play(message, arg):
    voice = message.guild.voice_client
    source = FFmpegPCMAudio(arg[0])
    player = voice.play(source)
    return f"Playing {arg[0]} !"
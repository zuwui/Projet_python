import requests
import json
import discord
import random
import string


def anime(commandParametres):
    # prepare api key params 
    headers = {
        "X-MAL-CLIENT-ID":"70a356502f99b93118839aa313f3a274"
    }
    # get 3 randoms letter for the request
    randomAlphabetLetters = "".join(random.choices(listAlphabet(), k=3))
    getAnimeByNameRequest = []

    # request for get one random anime
    getAnimeByName = f'https://api.myanimelist.net/v2/anime?q={randomAlphabetLetters}&limit=1'
    getAnimeByNameRequest = apiRequest(getAnimeByName, headers=headers)
    #check for the status
    if(getAnimeByNameRequest.status_code != 200 or not getAnimeByNameRequest.json()["data"]):
           return f"Error while fetching data with query : {randomAlphabetLetters}"  

    globalData = getAnimeByNameRequest.json()["data"][0]["node"]
    image=globalData["main_picture"]["large"]
    getAnimeDetailsRequest = apiRequest(f'https://api.myanimelist.net/v2/anime/{globalData["id"]}?fields=synopsis,status,num_episodes,genres', headers=headers)
    if(getAnimeDetailsRequest.status_code != 200):
        return f"Error while fetching data"  
    detailsData = getAnimeDetailsRequest.json()
    genres = ""
    for genre in detailsData["genres"]:
        genres += ", "+genre["name"]
    genres = genres[2:]

    
    embed = discord.Embed(title=detailsData["title"], description=detailsData["synopsis"])
    embed.set_image(url=image)
    embed.set_author(name="Bot created by the Botty team")
    embed.add_field(name="Status :hourglass:", value=detailsData["status"], inline=True)
    embed.add_field(name="Nombre d'épisodes :eyes:", value=detailsData["num_episodes"], inline=True)
    embed.add_field(name="Genres :nerd:", value=genres, inline=False)
    return embed
    


def listAlphabet():
    return list(string.ascii_lowercase)

def apiRequest(request, headers):
    return requests.get(request, headers=headers)
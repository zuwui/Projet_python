import requests
import json
import discord
import random
import string
import random


def anime(commandParametres):
    # prepare api key params 
    headers = {
        "X-MAL-CLIENT-ID":"70a356502f99b93118839aa313f3a274"
    }
    # check if there paramaters
    if commandParametres:
        if commandParametres[0] == "randomRank":
            # check if the number of parameters is equal to the required paramaters number
            if len(commandParametres) < 2:
                return "You must specify the ranking type" 
            return getRandomRankingAnime(commandParametres[1:], headers)
        if commandParametres[0] == "seasonal":
            # check if the number of parameters is equal to the required paramaters number
            if len(commandParametres) < 3:
                return "You must specify the year and season [winter, spring, summer, fall] and the selection limit (not required)" 
            return getSeasonalAnime(commandParametres[1:], headers)
        params = " ".join(commandParametres)

        if len(params) < 3: 
            return "You must write at least 3 characters in parameter or not at all."
        return getAnimeByName(params, headers)
            

    # get 3 randoms letter for the request
    randomAlphabetLetters = "".join(random.choices(listAlphabet(), k=3))
    return getAnimeByName(randomAlphabetLetters, headers)

# return a random letter
def listAlphabet():
    return list(string.ascii_lowercase)


def apiRequest(request, headers):
    return requests.get(request, headers=headers)


    # request for get one random anime
def getAnimeByName(name, headers):  
    getAnimeByName = f'https://api.myanimelist.net/v2/anime?q={name}&limit=1'
    getAnimeByNameRequest = apiRequest(getAnimeByName, headers=headers)
    #check for the status
    if(getAnimeByNameRequest.status_code != 200 or not getAnimeByNameRequest.json()["data"]):
        return f"Error while fetching data with query : {name}"  
    return createEmbedByFormattingData(getAnimeByNameRequest.json()["data"], headers)


def createEmbedByFormattingData(getAnimeByNameRequest, headers):
    # get anime information
    globalData = getAnimeByNameRequest[0]["node"]
    image=globalData["main_picture"]["large"]
    # request detail of anime
    getAnimeDetailsRequest = apiRequest(f'https://api.myanimelist.net/v2/anime/{globalData["id"]}?fields=synopsis,status,num_episodes,genres', headers=headers)
    if(getAnimeDetailsRequest.status_code != 200):
        return f"Error while fetching data"  
    detailsData = getAnimeDetailsRequest.json()
    genres = ""

    # get all genres
    for genre in detailsData["genres"]:
        genres += ", "+genre["name"]
    # delete the first two charater who are "," and space 
    genres = genres[2:]
    # create a discord embed
    embed = discord.Embed(title=detailsData["title"], description=detailsData["synopsis"])
    embed.set_image(url=image)
    embed.set_author(name="Bot created by the Botty team")
    embed.add_field(name="Status :hourglass:", value=detailsData["status"], inline=True)
    embed.add_field(name="Number of episodes :eyes:", value=detailsData["num_episodes"], inline=True)
    embed.add_field(name="Genres :nerd:", value=genres, inline=False)
    return embed


def getRandomRankingAnime(params, headers):
    authorizedRankingTypeParams = ["all", "airing", "upcoming", "tv", "ova", "movie", "special","bypopularity","favorite"]
    #check if the first param is in the authorizedRankingTypeParams array 
    if params[0] not in authorizedRankingTypeParams:
        return 'The authorized parameters for ranking type are : ["all", "airing", "upcoming", "tv", "ova", "movie", "special","bypopularity","favorite"]'
    limit = 100
    error = ""
    # i did try except to prevent the application from crashing because of int() in non int variable
    try:
        if len(params) >= 2 and not isinstance(int(params[1]), int):
            error = 'An int is expected for the limit' 
    except ValueError:
        error = 'An int is expected for the limit'
    
    if error != "":
        return error
    # fix the max limit to 500 (api limit)
    if len(params) >= 2:
        limit = params[1] if int(params[1]) <= 500 else 500
    rankingAnime = getRankingAnime(params[0], limit, headers)
    
    # check if erro message
    if(rankingAnime == "Error while fetching data"):
        return rankingAnime
    return createEmbedByFormattingData([random.choice(rankingAnime)], headers)

def getRankingAnime(rankingType, limit, headers):
    rankingAnime = apiRequest(f'https://api.myanimelist.net/v2/anime/ranking?ranking_type={rankingType}&limit={limit}', headers=headers)
    if(rankingAnime.status_code != 200 or not rankingAnime.json()["data"]):
        return f"Error while fetching data"
    return rankingAnime.json()["data"]


def getSeasonalAnime(params, headers):
    authorizedSeason = ["summer", "fall", "winter", "spring"]
    error = ""
    # check if the year arg is in a correct format
    try:
        if not isinstance(int(params[0]), int) or len(params[0]) != 4:
            error = "Invalid year"
    except ValueError:
        error = "Year must be an int"

    if error != "":
        return error

    if params[1] not in authorizedSeason:
        return 'The authorized parameters for season are : ["summer", "fall", "winter", "spring"]'
    
    # check if the optiomal param "limit" is a number
    try:
        if len(params) >= 3 and not isinstance(int(params[2]), int):
            return 'An int is expected for the limit'
    except ValueError:
        error = "An int is expected for the limit"
    
    if error != "":
        return error

    limit = 100
    # fix the limit to 500
    if len(params) >= 3:
        limit = params[2] if int(params[2]) <= 500 else 500
        
    seasonalAnime = getRandomSeasonalAnime(params[0], params[1], limit, headers)
    if(seasonalAnime == "Error while fetching data"):
        return seasonalAnime
    return createEmbedByFormattingData([random.choice(seasonalAnime)], headers)

def getRandomSeasonalAnime(year, season, limit, headers):
    seasonalAnime = apiRequest(f'https://api.myanimelist.net/v2/anime/season/{year}/{season}?limit={limit}', headers=headers)
    if(seasonalAnime.status_code != 200 or not seasonalAnime.json()["data"]):
        return f"Error while fetching data"
    return seasonalAnime.json()["data"]
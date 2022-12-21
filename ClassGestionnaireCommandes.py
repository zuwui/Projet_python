

class GestionnaireCommandes:
      
     
    async def execCommand(self, commandName, commandParametres, message, client):
                
        if(commandName == "ping"):
            from commandes.ping import ping
            return ping(commandParametres)
        elif(commandName == "help"):
            from commandes.help import help
            return help(commandParametres)
        elif(commandName == "jaj"):
            from commandes.jaj import jaj
            return jaj(commandParametres)
        elif(commandName == "math"):
            from commandes.math import math
            return math(commandParametres)
        elif(commandName == "anime"):
            from commandes.anime import anime
            return anime(commandParametres)
        elif(commandName == "join"):
            from commandes.song import join
            return await join(message)
        elif(commandName == "leave"):
            from commandes.song import leave
            return await leave(message, client)
        elif(commandName == "play"):
            from commandes.song import play
            return await play(message, commandParametres)
        elif(commandName == "pause"):
            from commandes.song import pause
            return await pause(message, client)
        elif(commandName == "resume"):
            from commandes.song import resume
            return await resume(message, client)
        elif(commandName == "stop"):
            from commandes.song import stop
            return await stop(message, client)
        return

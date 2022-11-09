

class GestionnaireCommandes:
      
     
    def execCommand(self, commandName, commandParametres):
                
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
        return

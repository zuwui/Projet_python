import json


class GestionnaireCommandes:
       
    def execCommand(self, commandName, commandParametres):
        # # We open the JSON file
        # commandesFile = open('./config.json')
        
        # # We return the file as a JSON object
        # listeCommandes = json.load(commandesFile)
        
        # # We get the command path
        # commandPath = listeCommandes[commandName]
        
        if(commandName == "ping"):
            from commandes.ping import ping
            return ping(commandParametres)
        if(commandName == "help"):
            from commandes.help import help
            return help(commandParametres)
        if(commandName == "jaj"):
            from commandes.jaj import jaj
            return jaj(commandParametres)
        else:
            return
        
        
        


class GestionnaireCommandes:
       
    def execCommand(self, commandName, commandParametres):
                
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
        
        
        

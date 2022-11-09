

def math(commandParametres):
    commandParametres = removeVoidParametres(commandParametres)

    operatorList = ["add", "sub", "mult", "div"]

    if(len(commandParametres) < 2):
        return "ERROR: No secondary parametres provided"

    if(commandParametres[0] not in operatorList):
        return "ERROR: Primary parametres must be an operation"

    if(commandParametres[0] == "add"):
        return add(commandParametres[1:])
        

def add(commandParametres):
    if(checkIfSecondaryParametresAreNumeric(commandParametres) == False):
        return "ERROR: Secondary parametres must be numeric"
    
    for i in range(len(commandParametres)):
        commandParametres[i] = (int)(commandParametres[i])

    return sum(commandParametres)

def substract(commandParametres):
    return
      

def checkIfSecondaryParametresAreNumeric(commandParametres):
    for i in range(len(commandParametres)):
        if commandParametres[i].isnumeric() == False:
            return False
    return True

  
def removeVoidParametres(commandParametres):
    newCommandParametres = []
    
    for i in range(len(commandParametres)):
        if commandParametres[i] != "":
            newCommandParametres.append(commandParametres[i])
    
    return newCommandParametres
            
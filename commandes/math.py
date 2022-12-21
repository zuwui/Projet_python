import json

def math(commandParametres):
    commandParametres = removeVoidParametres(commandParametres)

    operatorList = ["add", "sub", "mult", "div", "help"]

    if(commandParametres[0] not in operatorList):
        return "ERROR: Primary parametres must be an operation"

    if(len(commandParametres) < 2 and commandParametres[0] != "help"):
        return "ERROR: No secondary parametres provided"
    
    # We ignore the first parametres which is the operation type
    if(checkIfSecondaryParametresAreNumeric(commandParametres[1:]) == False): 
        return "ERROR: Secondary parametres must be numeric"

    # We convert all parametres in int
    for i in range(len(commandParametres)):
        if(i != 0): # We do not convert the operation type
            commandParametres[i] = (int)(commandParametres[i])

    # We do the appropriate operation
    if(commandParametres[0] == "add"):
        return add(commandParametres[1:])
    elif(commandParametres[0] == "sub"):
        return substract(commandParametres[1:])
    elif(commandParametres[0] == "mult"):
        return multiply (commandParametres[1:])
    elif(commandParametres[0] == "div"):
        return divide (commandParametres[1:])
    elif(commandParametres[0] == "help"):
        return "------- MATH HELP ------\n  add (to make an addition)\n  sub (to make a substraction)\n  mult (to make a multiplication)\n  div (to make a division)"
        

def add(commandParametres):
    total = sum(commandParametres)
    
    return total

def substract(commandParametres):
    total = commandParametres[0] 
        
    for i in range(len(commandParametres)):
        if(i != 0): # We ignore the first number cause it's our starting point
            total -= commandParametres[i]

    return total

def multiply(commandParametres):
    total = commandParametres[0] 
        
    for i in range(len(commandParametres)):
        if(i != 0): # We ignore the first number cause it's our starting point
            total *= commandParametres[i]

    return total

def divide(commandParametres):
    total = commandParametres[0] 
        
    for i in range(len(commandParametres)):
        if(i != 0): # We ignore the first number cause it's our starting point
            total /= commandParametres[i]

    return total

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

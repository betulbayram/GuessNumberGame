import random

debug_flag = False

def generateRandom():
    return random.randint(1,20)

def guess():
    return input("guess number: ")    

def debugState():
    global debug_flag
    
    if(debug_flag == False):
        debug_flag = True
    
    elif(debug_flag == True):
        debug_flag = False

def debugMode():
    print(f"secret number was {secret_number}. Secret number changing..")
    return generateRandom()

def stateMachine(guess_):
    
    if(guess_ == 'x' or guess_ == 'X'):
        return 0

    elif(guess_ == 's' or guess_ == 'S'):
        print(f"hack mode on. secret number is {secret_number}")
        return 1

    elif(guess_ == 'd' or guess_ == 'D'):
        debugState()

    elif(secret_number == int(guess_)):
        print("good job, correct guess")
        return 0

    elif(secret_number > int(guess_)):
        print("noo, it's smaller than secret number")
        return 1

    elif(secret_number < int(guess_)):
        print("noo, it's bigger than secret number")
        return 1

secret_number = generateRandom()
        


def Game():
    while(True):
        
        if(debug_flag == False):
            
            guess_ = guess()
            
            if(stateMachine(guess_) == 0):
                break
        
        elif(debug_flag == True):
            
            global secret_number
            secret_number = debugMode()
            guess_ = guess()
            
            if(stateMachine(guess_) == 0):
                break

Game()
    

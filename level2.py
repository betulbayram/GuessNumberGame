import random

def generateRandom():
    return random.randint(1,20)

def guess():
    return int(input("guess number"))

def stateMachine():
    
    if(secret_number == guess_):
        print("good job, correct guess")
        return 0
   
    elif(secret_number > guess_):
        print("noo, it's smaller than secret number")
        return 1
    
    elif(secret_number < guess_):
        print("noo, it's bigger than secret number")
        return 1

secret_number = generateRandom()

while(True):
    
    guess_ = guess()
   
    if(stateMachine() == 0):
        break


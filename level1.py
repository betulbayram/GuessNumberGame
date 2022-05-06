import random

def generateRandom():
    return random.randint(1,20)

def guess():
    return int(input("guess number"))

def stateMachine():
    
    if(secret_number == guess_):
        print("good job, correct guess")
   
    elif(secret_number > guess_):
        print("noo, it's smaller than secret number")
    
    elif(secret_number < guess_):
        print("noo, it's bigger than secret number")

secret_number = generateRandom()
guess_ = guess()
stateMachine()


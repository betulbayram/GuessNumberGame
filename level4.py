import random

def generateRandom():
    return random.randint(1,20)

def guess():
    return input("guess number: ")

def stateMachine():
   
    if(guess_ == 'x' or guess_ == 'X'):
        return 0
  
    elif(guess_ == 's' or guess_ == 'S'):
        print(f"hack mode on. secret number is {secret_number}")
        return 1    
  
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

while(True):
    
    guess_ = guess()
    
    if(stateMachine() == 0):
        break


import random

debug_flag = False
movement_flag = False

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

def movementState():
    global movement_flag
   
    if(movement_flag == False):
        movement_flag = True
   
    elif(movement_flag == True):
        movement_flag = False

def movementMode():
    global secret_number
  
    if(secret_number < 19):
        secret_number +=2
  
    elif(secret_number > 1):
        secret_number-=2
  
    return secret_number
        

def stateMachine(guess_):
  
    if(guess_ == 'x' or guess_ == 'X'):
        return 0

    elif(guess_ == 'n' or guess_ == 'N'):
        print("next game initilazing")
        return -1

    elif(guess_ == 's' or guess_ == 'S'):
        print(f"hack mode on. secret number is {secret_number}")
        return 1

    elif(guess_ == 'd' or guess_ == 'D'):
        debugState()

    elif(guess_ == 'm' or guess_ == 'M'):
        movementState()
    
    elif(secret_number == int(guess_)):
        print("good job, correct guess")
        return 0

    elif(secret_number > int(guess_)):
        print("noo, it's smaller than secret number")
        return 1

    elif(secret_number < int(guess_)):
        print("noo, it's bigger than secret number")
        return 1


        


def Game():
   
    print("NEW GAME STARTING")
   
    global secret_number
    secret_number = generateRandom()
   
    while(True):

        if(debug_flag == False):
            
            if(movement_flag == True):
                
                print(secret_number)
                guess_ = guess()
                secret_number = movementMode()
                state = stateMachine(guess_)
                
                if(state == -1):
                    Game()
                    break
                
                elif(state== 0):
                    break
                
                

            elif(movement_flag == False):
                
                guess_ = guess()
                state = stateMachine(guess_)
               
                if(state == -1):
                    Game()
                    break
               
                elif(state == 0):
                    break

        elif(debug_flag == True):
            
            secret_number = debugMode()
            guess_ = guess()
            state = stateMachine(guess_)
          
            if(state == -1):
                Game()
                break
           
            elif(state == 0):
                break

Game()
    

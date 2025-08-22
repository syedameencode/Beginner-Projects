print('''
                                                                                                    
                                            ..::-----:..                                            
                                        .:=++++++++++++**+-.                                        
                                      .:++===+++++++++++++**=.                                      
                                     .=+===++++++++++++++++**+.                                     
                                    .=+==++***:.     .++++++**+.                                    
                                    :+++++**=.        .=++++***:                                    
                                    :++++**+.          :+++++**-                                    
                                                       .+++++**-                                    
                                                      .-++++***:                                    
                                                     .-+++++**=                                     
                                                    :+++++***-.                                     
                                                  .++++++***:.                                      
                                                .=+++++***=.                                        
                                              .:++++++**=.                                          
                                              :+++++**+.                                            
                                              +++++**=                                              
                                             :++++**+.                                              
                                             :++++**+.                                              
                                              ......                                                
                                                                                                    
                                              ..:::..                                               
                                             :+++++**:                                              
                                            .+++++++**.                                             
                                            .+++++++**.                                             
                                            .-+++++**:                                              
                                              .:==-..                                               
                                                                                                    ''')
print('''
          ____                       _____ _          
         / ___|_   _  ___  ___ ___  |_   _| |__   ___ 
        | |  _| | | |/ _ \/ __/ __|   | | | '_ \ / _ \
      
        |_| | |_| | |__/  \__ \__ \   | | | | | |  __/
         \____|\__,_|\___||___/___/   |_| |_| |_|\___|
      
        | \ | |_   _ _ __ ___ | |__   ___ _ __        
        |  \| | | | | '_ ` _ \| '_ \ / _ \ '__|       
        | |\  | |_| | | | | | | |_) |  __/ |          
        |_| \_|\__,_|_| |_| |_|_.__/ \___|_|          \n''')


print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

import random

#Choose a random number between 1 and 100
def guess_the_number():
    number=random.randint(1,100)
    print(number)
    return number

Hard_attempts=0
Easy_attempts=0

#Choosing the diffculty level
def difficulty_level():
    print("Choose a difficulty level:")
    level=input("easy or hard: ").lower()
    if level == "easy":
        print("Going easy huh?")
    elif level == "hard":
        print("You are a brave one!")
    
    print(f"You have chosen {level} level.")
    if level=="easy":
        global Easy_attempts
        Easy_attempts = 10
        return Easy_attempts
    elif level=="hard":
        global Hard_attempts
        Hard_attempts = 5
        return Hard_attempts
    else:
        print("Invalid choice, please choose 'easy' or 'hard'.")
    

#Compare the user's guess with the actual number
def compare_guess(guess,number,turns):
    if guess <  number:
        print("Low")
        return turns - 1
    elif guess > number:
        print("High")
        return turns - 1
    else:
        print(f"You guessed it right!, the number was {number}.")
        print( "You win")
#Main game function
def game():
    print("Welcome to the Guess The Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    turns=difficulty_level()
    guess=0
    number_generated=guess_the_number()
    while guess!= number_generated:
        print(f"You have {turns} attempts to guess the number.")
        guess=int(input("Make a guess: "))
        turns=compare_guess(guess,number_generated,turns)
        if turns == 0:
            print("You have run out of attempts, you lose.")
            return
game()            




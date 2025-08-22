#Black jack educational purposes only
import random
import os
from art import logo
print(logo)

def deal_card():
    "Returnes a random card from the deck."
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
#Clear screen function
def clear_screen():
    """Clears the screen for a fresh start."""
    os.system('cls' if os.name == 'nt' else 'clear')

#Result of the game
def compare(user_score, computer_score):
    "Compares the scores and returns the result."
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "Lose, opponent has Blackjack"
    elif user_score==0:
        return "Win with a Blackjack"
    elif user_score>21:
        return "You went over. You lose"
    elif computer_score>21:
        return "Opponent went over. You win"
    elif user_score>computer_score:
        return "You win"
    else:
        return "You lose"
    
#Function to calculate the score of a hand
def calculate_score(cards):
    "Calculates the score of a hand."
    #Add sum function
    if sum(cards)==21 and len(cards)==2:
        return 0 # Blackjack
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def play_game():
    player_cards=[]
    computer_cards=[]
    game_over=False
    
    '''Lopping the card twice'''
    for i in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
    print("Welcome to Black Jack")
    print("You can get a card by typing 'y' or pass by typing 'n'")
    print("The goal is to get as close to 21 without going over.")
    print("Aces are worth 11 or 1, face cards are worth 10, and all other cards are worth their number value.")

    while not game_over:
        player_score=calculate_score(player_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your Cards:{player_cards},Current Score:{player_score}")
        print(f"Computer First Card:{computer_cards[0]}")
        #Player should get another card or pass
        if player_score==0 or computer_score==0 or player_score>21:
            game_over=True
        else:
            user_choice=input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_choice=="y":
                player_cards.append(deal_card())
            else:
                game_over=True

    '''Looking for computer Score '''
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())  # <-- add parentheses to call the function
        computer_score = calculate_score(computer_cards)

    print(compare(player_score,computer_score))
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
#Ask user to play the game
start_game=input("Do you want to play a game of Black Jack? Type 'y' or 'n': ").lower()
while start_game=="y":
    clear_screen()
    play_game()
    start_game=input("Do you want to play again? Type 'y' or 'n': ").lower()
    if start_game == "n":
        print("Thank you for playing Black Jack!")
        break
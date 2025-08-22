#display art
from art import logo, vs
import random
from game_data import data
import os
def clear_screen():
    """Clear the screen for secret bidding"""
    os.system('clear' if os.name == 'posix' else 'cls')

#Format acount into printable format
def format_data(account_a):
    account_name=account_a["name"]
    account_decr=account_a["description"]
    account_country=account_a["country"]
    return f"{account_name}, a {account_decr}, from {account_country}."

def check_andswer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

score=0
should_continue=True
print(logo)
#Generate a random account from the game data
account_b=random.choice(data)
while should_continue:
    account_a=account_b
    account_b=random.choice(data)
    if account_a == account_b:
        account_b=random.choice(data)
    print(f"Compare A:{format_data(account_a)}")
    print(vs)
    print(f"Against B:{format_data(account_b)}")
    
    
#check if user is correct
    guess=input("Who has more followers? Type A or B: ").lower()
#Get follower count
    a_followers=account_a["follower_count"]
    b_followers=account_b["follower_count"]
#Check if user is correct
    is_correct = check_andswer(guess, a_followers, b_followers)
    clear_screen()
#Give user feedback on their guess
#Score keeping
    if is_correct:
        score+=1
        print(f"You are right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue = False

#Make the game repeatable
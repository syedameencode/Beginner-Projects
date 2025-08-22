
import os

def print_banner():
    print('''    
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\\''')

def get_user_bid():
    """Get a valid bid from a user"""
    while True:
        try:
            name = input("Enter your name: ").strip()
            if not name:
                print("Name cannot be empty. Please try again.")
                continue
            
            bid = int(input("Enter your bid: $"))
            if bid <= 0:
                print("Bid must be a positive number. Please try again.")
                continue
            
            return name, bid
        except ValueError:
            print("Please enter a valid number for your bid.")

def clear_screen():
    """Clear the screen for secret bidding"""
    os.system('clear' if os.name == 'posix' else 'cls')

def find_highest_bid(bids):
    """Find and announce the winner"""
    if not bids:
        print("No bids were placed.")
        return
    
    winner = max(bids, key=bids.get)
    highest_bid = bids[winner]
    
    print(f"\nThe Winner is {winner} with a bid of ${highest_bid}!")
    print(f"\nAll bids:")
    for name, bid in sorted(bids.items(), key=lambda x: x[1], reverse=True):
        print(f"  {name}: ${bid}")

def main():
    print_banner()
    print("Welcome to the Secret Auction System!")
    print("-" * 40)
    
    user_bids = {}
    
    # Get first bid
    name, bid = get_user_bid()
    user_bids[name] = bid
    
    # Get additional bids
    while True:
        continue_bidding = input("\nIs there another bidder? (yes/no): ").lower().strip()
        
        if continue_bidding in ['no', 'n']:
            break
        elif continue_bidding in ['yes', 'y']:
            clear_screen()
            print("Next bidder, please step forward...")
            name, bid = get_user_bid()
            user_bids[name] = bid
        else:
            print("Please enter 'yes' or 'no'.")
    
    # Clear screen and announce results
    clear_screen()
    print_banner()
    print("Bidding has ended!")
    print("=" * 40)
    find_highest_bid(user_bids)

if __name__ == "__main__":
    main()

#end of Secret Auction System
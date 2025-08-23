import random

print("PASSWORD RANDOM GENERATOR")
print('''                                                                                                                              
                                                                                -+****++**                              
                                                                               +#.       +*+                            
                                                                              +#          +*                            
                                                                              **          -**                           
                                                                              **   .      -**                           
                                                                              **    .     -**                           
                                  *+*=*   ++*=*   *+*-*   =**:*    **.*    ===================+                         
                                   *=*     ***     ***     ***     ***   .++++++++++++++++++++++#                       
                                                                         :++++++++++++++++++++++#..                     
                                                                         :++++++++++++++++++++++#:..                    
                         ..:::::::::::::::::::::::::::::::::::::::::::::::++++++++++++++++++++++#:..                    
                                                                         :+++++++++*%%++++++++++#:..                    
                                                                         :++++++++++#%++++++++++#:..                    
                                                                         :++++++++++%%++++++++++#:..                    
                                                                         :++++++++++++++++++++++#:..                    
                                                                         :++++++++++++++++++++++#:..                    
                                                                         :++++++++++++++++++++++#:..                    
                                                                          +++++++++++++++++++++++...                    
                                                                             ....::::::::::::::....                     
                                                                               ..................                       
''')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
symbols = ['@', '#', '!', '$']
numbers = [1, 2, 3, 4, 5]

# Get user input with error handling
try:
    user_letters = int(input("Enter No. of Letters: "))
    user_symbols = int(input("Enter No. of Symbols: "))
    user_numbers = int(input("Enter No. of Numbers: "))
except ValueError:
    print("Error: Please enter valid numbers.")
    exit()

# Initialize empty password list
password = []

# Append random letters
for i in range(user_letters):
    password.append(random.choice(letters))

# Append random symbols
for i in range(user_symbols):
    password.append(random.choice(symbols))

# Append random numbers
for i in range(user_numbers):
    password.append(random.choice(numbers))

# Shuffle the password to make it random
random.shuffle(password)

# Convert the list to a string using a simple loop
password_str = ""
for char in password:
    password_str += str(char)  # Convert each element to string and concatenate

# Print the final password
print(f"Your Password is: {password_str}")
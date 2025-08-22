#Caesar cipher
print('''This program implements the Caesar Cipher encryption and decryption.\n
It allows the user to input a string, a shift value, and choose whether to encrypt or decrypt the string.\n
The program will then output the transformed string based on the user's choices.''')
print('''                                                    
                     :=+=--==--=+-:                 
                 :++===+=--==--+=--==-.             
              :====+=====-=+--+=--==----.           
            -=++===+===-:.:::-==-=+---=+--          
          :+===++=-::..=..:.::..:---++------        
         =======:::..:.::--.:..:...:-----=---       
       .+=====--..::.........:-..:..:===-----:      
      .===++=...:-.............:..-::-----=+=-      
     .======..:::...............-:..:.-==--::=.     
     =+=++=-:-:......---:........:....----:--=:     
    :=====-.........-#*+#........-.--.-====+==:     
    ++=+*=-:.........=*#+.............---:::-=.     
    ======::..:....................--:===-==-=      
    =+++*=-....:...............-:::..-------=:      
    ======-:-..::............--...:.==---::-=       
    -===+==:::..::..........-..::.:-----=-=+        
     ++=====-..-.....-.:..-..-..:-==--:::=+         
     .===++=-=:..:..:..-:.:...:---------==          
      .++=-=++-=-::::..::::----=------=+:           
       .-====--++--++--=---+=--------+-             
         .==--==--=+=--==---=-----=+-               
           .:-+=--=+=-=+=------=+-.                 
               .-===---====+=-.                     
                                                    
                                                    ''')
print('''
          ____                                  _       _               
         / ___|__ _  ___  ___  __ _ _ __    ___(_)_ __ | |__   ___ _ __ 
        | |   / _` |/ _ \/ __|/ _` | '__|  / __| | '_ \| '_ \ / _ \ '__|
        | |__| (_| |  __/\__ \ (_| | |    | (__| | |_) | | | |  __/ |   
         \____\__,_|\___||___/\__,_|_|     \___|_| .__/|_| |_|\___|_|   
                                                             ''')
alphabet= [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
#Main function for encryption and decryption
def ceaesar(user_txt,user_shift,user_choice):
    cypher_txt=""
    if user_choice==2:
        user_shift*= -1
    for i in user_txt:
        if i not in alphabet:
            cypher_txt+=i
            continue
        shift_pos=alphabet.index(i)+user_shift
        shift_pos%=len(alphabet)
        cypher_txt+=alphabet[shift_pos]
    if user_choice==1:
        print(f"Here is your encrypted {cypher_txt}")
    else:
        print(f"Here is your decrypted {cypher_txt}")
#Making the program run in a loop
countinue=True
while countinue:
    user_choice=int(input("Enter 1 for Encrypt or 2 for Decrypt\n"))
    user_txt=input("Enter your word\n").lower()
    user_shift=int(input("Enter you Shift\n"))
    ceaesar(user_txt,user_shift,user_choice)
    user_continue=input("Do you want to continue? (yes/no)\n").lower()
    if user_continue == "no":
        countinue=False
        print("Thank you for using Caesar cipher!")
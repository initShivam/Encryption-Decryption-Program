print('''
% >>========================================================<<
% ||                                                        ||
% ||   _____                             _   _              ||
% ||  | ____|_ __   ___ _ __ _   _ _ __ | |_(_) ___  _ __   ||
% ||  |  _| | '_ \ / __| '__| | | | '_ \| __| |/ _ \| '_ \  ||
% ||  | |___| | | | (__| |  | |_| | |_) | |_| | (_) | | | | ||
% ||  |_____|_| |_|\___|_|   \__, | .__/ \__|_|\___/|_| |_| ||
% ||                         |___/|_|                       ||
% ||   ____                             _   _               ||
% ||  |  _ \  ___  ___ _ __ _   _ _ __ | |_(_) ___  _ __    ||
% ||  | | | |/ _ \/ __| '__| | | | '_ \| __| |/ _ \| '_ \   ||
% ||  | |_| |  __| (__| |  | |_| | |_) | |_| | (_) | | | |  ||
% ||  |____/ \___|\___|_|   \__, | .__/ \__|_|\___/|_| |_|  ||
% ||                        |___/|_|                        ||
% ||                                                        ||
% >>========================================================<<
''')
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           '0','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z']

choise = input("Type encrypt to 'encrypt' data and decrypt to 'decrypt' data.\n").lower()
def encrypt(cypher_text,shift_amount):
    CypherText = ""
    for i in cypher_text:
        shift_position = alphabet.index(i) + shift_amount
        shift_position %= len(alphabet)
        CypherText += alphabet[shift_position]
    print("Here is Your Converted Value : ",CypherText)

def decrypt(cypher_text,shift_amount):
    plaintext = ""
    for i in cypher_text:
        shift_position = alphabet.index(i) - shift_amount
        shift_position %= len(alphabet)
        plaintext += alphabet[shift_position] 
    print("Here is Your Converted Value : ",plaintext)

do_going = True
while do_going:
    if choise == "encrypt":
        text = input("Enter Your Message: ").lower()
        shift =int(input("How Many Numbers You Want to Shift ? \n"))
        print("Encryption is in progress.....")
        encrypt(text,shift)

    elif choise == "decrypt":
        cyphertext = input("Enter Your Cyphertext: ")
        shift = int(input("How Many Numbers You Want to Shift ? \n"))
        print("Decryption is in progress.....")
        decrypt(cyphertext,shift)
    else:
        print("Invalid Input")

    condition = input("Do you want to continue ? (yes/no)")

    if condition == "yes":
        do_going = True
    elif condition == "no":
        do_going = False
    else:
        print("Invalid Input")
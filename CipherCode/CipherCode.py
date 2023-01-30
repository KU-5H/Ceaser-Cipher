"""
Python Program: Encryption and Decryption Code

Problem: 
Sometimes you may use common passwords to access infromation and that allows others who maby know some things about you (such as birthday or school) to access your information.
To combat this, you can use a simple encrpytion tool to encrypt your infromation and while not very compelx, the ceaser cypher ecnryption is fine for everyday password use.
This program has both a encryption (Which will add a space after every 3 letters) and decyption option (which will output with no spaces)

Code:
The code will either encrypt or decrpyt based on what you need and will incremement it based on your input. The code also flips lower and upper case letters
Encrypt - This will change your input based on the increment you use. It will also add a space every 3 letters (Ex. ABc increment 1 is bcD)
Decrypt - This will change your input based on the decrement you use. The final answer will have no spaces (Ex. BC d decrement 1 is abC)
"""

## Two lists that hold both the lowercase and uppercase alphabets. To be used to find letters in the encoder or decoder
lowerAlphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperAlphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

## A function to find how much the letter will be incremented by (Accounts for going over the range)
def increase(location, step):

    # If statement to check if the increment is outside the range of the list
    if location+step > 25:
        # By using floor division and subtrcting by 26, we can loop back around in the list to find the increment
        return location + step - 26*((location+step)//26)

    else:
        # Returning the increment in the case there is no overflow
        return location + step

## A function to find how much the letter will be decremented by (Accounts for going under the range)
def decrease(location, step):

    # If statement to check if the decrement is outside the range of the list 
    if location-step < 25:
        # By using floor division and adding by 26, we can loop back around in the list to find the increment
        return location - step + 26*(abs((location-step)//26))

    else:
        # Returning the increment in the case there is no overflow
        return location - step

## A function to encode the words the user put into the input
def encodeStatement(word, step):

    # Variables that serve as the encrypted messages (One with and one without formatting)
    encrypt = ''
    trueEncrypt = ''

    # For loop to check every letter in a word
    for n in word:
        # If statement to check if the letter is an uppercase or lowercase letter. In the case it is neither, it's not included in the encryption
        if n.isupper():
            # For loop to serach for the exact letter that n represents
            for i in range(len(upperAlphabet)):
                # If statement to check if n, the letter, is equal to a letter in the two global lists
                if n == upperAlphabet[i]:
                    # Adding a incremented version of the letter to the new encrypted message
                    encrypt += upperAlphabet[increase(i, step)].lower()

        elif n.islower():
            # For loop to serach for the exact letter that n represents
            for i in range(len(lowerAlphabet)):
                # If statement to check if n, the letter, is equal to a letter in the two global lists
                if n == lowerAlphabet[i]:
                    # Adding a incremented version of the letter to the new encrypted message
                    encrypt += lowerAlphabet[increase(i, step)].upper()

    # For loop to add formatting to the encrypted message to make it more difficult to decypher
    for k in range(len(encrypt)):
        # If statement to ignore any spaces in the encrypted message
        if encrypt[k] != ' ':
            # If statement that adds a space for every 3 letters to make it diffuclt to read
            if k % 3 == 0 and k != 0:
                trueEncrypt += ' '
            # Adding the letters from the non-formatting encrypted message to the formatted one
            trueEncrypt += encrypt[k]
    
    # Returning the encrypted message
    return trueEncrypt

## A function to edcode the words the user inputted
def decodeStatement(word, step):

    # Variables that serve as the decrypted messages (One with and one without formatting)
    decrypt = ''
    trueDecrypt = ''

    # For loop to check every letter in a word
    for n in word:
        # If statement to check if the letter is an uppercase or lowercase letter. In the case it is neither, it's not included in the decryption
        if n.isupper():
            # For loop to serach for the exact letter that n represents
            for i in range(len(upperAlphabet)):
                # If statement to check if n, the letter, is equal to a letter in the two global lists
                if n == upperAlphabet[i]:
                    # Adding a decremented version of the letter to the new encrypted message
                    decrypt += upperAlphabet[decrease(i, step)].lower()

        elif n.islower():
            # For loop to serach for the exact letter that n represents
            for i in range(len(lowerAlphabet)):
                # If statement to check if n, the letter, is equal to a letter in the two global lists
                if n == lowerAlphabet[i]:
                    # Adding a incremented version of the letter to the new encrypted message
                    decrypt += lowerAlphabet[decrease(i, step)].upper()

    # For loop to deformat the decrypted message to make it more readable
    for k in range(len(decrypt)):
        # If statement to ignore any spaces in the decrypted message
        if decrypt[k] != ' ':
            # Adding the letters from the formatted decrypted message to the deformatted one
            trueDecrypt += decrypt[k]

    # Returning the decrypted message       
    return trueDecrypt

# A boolean variable to keep running the inputs until the user is satisfied with their inputs
everythingUserWants = True

# While loop to keep running until the user inputs everything and confirms that they are happy with it
while(everythingUserWants):

    # Asking the user whether they want ot encode or decode a message
    encodeOrDecode = str(input("Would you like to encode or decode?: ")).lower()

    # Asking the user for a statement or word to encode/decode
    statement = str(input("Enter what needs to be encoded/decoded (symbols, numbers and periods are NOT suppported). Decoding will not space any words: "))

    # Asking the user for how much the letter should increment/decrement by
    increment = int(input("Enter the integer of how much you want to increment each letter: "))

    # Boolean that's used to check if what the user inputted is what they acutally want
    key = True

    # While loop to keep running until the user answers with either true or false
    while(key):
        # Asking the user if what they chose to encrypt/decrypt is acutaly what the wanted in the case they wish to change it
        userWants = input("Are you sure about you chose? Enter yes or no (Selecting no will reset all of your inputs): ").lower()
        #Checking if the user put sometginf that isnt yes or no
        if userWants != 'yes' and userWants != 'no':
            # Simply asking the user to print an acutal answer
            print("Please enter either yes or no")
        else:
            # Checking if the user selected yes or no
            if userWants == 'yes':
                # Cutting the large while loop so the code can move on
                everythingUserWants = False
            elif userWants == 'no':
                # Telling the user that the inputs have been reset so the while loop will run again
                print()
                print('--------------------------------------')
                print("All of your inputs have been reset, please re-enter them")
                print("--------------------------------------")
                print()
            # Setting the key to false to break the while loop
            key = False

# Print statement to space out the output from the inputs
print()

# If statement to see if the user wishes to encode or decode the message
if encodeOrDecode == 'encode':
    # Printing out the encoded message after going through the encoding fucntion
    print("Your encrypted message is: " + str(encodeStatement(statement, increment)))
elif encodeOrDecode == 'decode':
    # Printint out the decoded message after going through the decoding function
    print("Your decrypted message is (without spaces): " + str(decodeStatement(statement, increment)))
else:
    print("ERROR: You did not enter encode or decode, please restart the program.")
### CAESAR ENCRYPTION ###

str = input("Geheime Nachricht: ")
key = int(input("Schlüssel: "))
alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar(str, key):
    encrypted_str = ""

    for letter in str:
        if letter.isalpha(): # Check if the character is a letter
            if letter.islower(): # Check if the character is lowercase
                alphabet = alphabet_lower
            else:
                alphabet = alphabet_upper

            # Perform the Caesar Cypher Shift!
            index = alphabet.index(letter) # Make index of letter to an integer
            new_index = (index + key) % 26
            new_letter = alphabet[new_index]
            encrypted_str += new_letter
        else:
            # If the character is not a letter, keep it unchanged
            encrypted_str += letter
    print("Verschlüsselte Nachricht:", encrypted_str)

caesar(str, key)
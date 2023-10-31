alphabet = "abcdefghijklmnopqrstuvwxyz"

phrase = input("Please enter a sentence: ")

phrase = phrase.lower()

encrypted_phrase = ""

shift = 5 

for char in phrase:
    if char in alphabet:
        index = alphabet.find(char)
        index = (index + shift) % 26
        char = alphabet[index]
    encrypted_phrase += char

print('The encrypted sentence is: ',  encrypted_phrase)


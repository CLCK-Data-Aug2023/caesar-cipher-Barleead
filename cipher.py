alphabet = "abcdefghijklmnopqrstuvwxyz"

shift = int(input("Number of spaces to shift: "))

phrase = input("Please enter a word or phrase to encrypt: ")

phrase = phrase.lower()

encrypted_phrase = ""

for char in phrase:
    if char in alphabet:
        index = alphabet.find(char)
        index = (index + shift) % 26
        char = alphabet[index]
    encrypted_phrase += char

print(encrypted_phrase)

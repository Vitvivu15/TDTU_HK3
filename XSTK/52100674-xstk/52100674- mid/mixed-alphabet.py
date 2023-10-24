import random
import string


def mixed_alphabet(plaintext):
    # make sure input is correct
    plaintext = plaintext.lower()
    # create list containing all letters of the alphabet
    alphabet = list(string.ascii_letters)
    # create list of all letters but in different order
    key = alphabet.copy()
    random.shuffle(key)
    # create empty string to store ciphertext
    ciphertext = ""
    print(key)
    # loop through plaintext and encrypt each letter with mixed alphabet cipher
    for i in plaintext:
        # if letter is in alphabet, encrypt it
        if i.isalpha():
            ciphertext += key[ord(i) - 97]
        # if letter is not in alphabet, add it to ciphertext
        else:
            ciphertext += i
    return ciphertext.upper()


print(mixed_alphabet("mixed_alphabet"))
fread = open("plaintext_50.txt", "r")
fwrite = open("ciphertext.txt", "w")

fwrite.write(mixed_alphabet(fread.read()))
fwrite.close()

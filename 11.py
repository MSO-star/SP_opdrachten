user_srtring = input("Geef een tekst: ")
user_shift = int(input("Geef een rotatie: "))



def Caesarcijfers():
    cipher_tekst = ""
    for letter in user_srtring:
        if letter.isalpha():
            nog_alphabet = ord(letter) + user_shift
        if nog_alphabet > ord('z'):
             nog_alphabet -= 26
        finalLetter = chr(nog_alphabet)
        cipher_tekst += finalLetter

    print ("Cassarcode is:", cipher_tekst)

Caesarcijfers()


# bron: https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm


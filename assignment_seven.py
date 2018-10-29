# Flint Eller
# 10/26/18
# This program encrypts and decrypts strings


def user_key():
    key = int(input("Please enter the key (0 - 25): "))
    return key


def rotate(key, alphabet):
    first = alphabet[:key]
    last = alphabet[key:]
    new_alphabet = last + first
    return new_alphabet


def user_phrase():
    phrase = input("Please enter the text to be encoded: ")
    return phrase.lower()


def encode(phrase, alphabet, new_alphabet):
    for letter in phrase:
        index = alphabet.index(letter)
        new_phrase = new_alphabet[index]
    return new_phrase




def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = user_key()
    new_alphabet = rotate(key, alphabet)
    print(alphabet)
    print(new_alphabet)
    phrase = user_phrase()
    new_phrase = encode(phrase, alphabet, new_alphabet)
    print(new_phrase)


main()

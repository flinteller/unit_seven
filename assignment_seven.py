# Flint Eller
# 10/26/18
# This program encrypts and decrypts strings


def user_action():
    action = input("Press e to encode, d to decode, or q to quit: ")
    return action


def user_key():
    key = int(input("Please enter the key (0 - 25): "))
    return key


def rotate(key, alphabet):
    first = alphabet[:key]
    last = alphabet[key:]
    new_alphabet = last + first
    return new_alphabet


def encode_phrase():
    en_phrase = input("Please enter the text to be encoded: ")
    en_phrase = en_phrase.replace(" ", "")
    return en_phrase.lower()


def encode(phrase, alphabet, new_alphabet):
    new_phrase = ""
    for letter in phrase:
        index = alphabet.index(letter)
        new_letter = new_alphabet[index]
        new_phrase = new_phrase + new_letter
    return new_phrase


def decode_phrase():
    de_phrase = input("Please enter the test to be decoded: ")
    de_phrase = de_phrase.replace(" ", "")
    return de_phrase.lower()


def decode(phrase, alphabet, new_alphabet):
    de_phrase = ""
    for letter in phrase:
        index = new_alphabet.index(letter)
        new_letter = alphabet[index]
        de_phrase = de_phrase + new_letter
    return de_phrase


def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    action = user_action()
    while True:
        if action == "q":
            print("Thanks for playing!")
            break
        elif action == "e":
            key = user_key()
            new_alphabet = rotate(key, alphabet)
            en_phrase = encode_phrase()
            new_phrase = encode(en_phrase, alphabet, new_alphabet)
            print(new_phrase)
            break
        elif action == "d":
            key = user_key()
            new_alphabet = rotate(key, alphabet)
            de_phrase = decode_phrase()
            de_phrase = decode(de_phrase, alphabet, new_alphabet)
            print(de_phrase)
            break
        else:
            print("You have entered an invalid command")
            break


main()

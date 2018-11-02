# Flint Eller
# 10/26/18
# This program encrypts and decrypts strings


def user_action():
    """
    Asks the user if they want to encode, decode or quit
    :return: user's answer
    """
    action = input("Press e to encode, d to decode, or q to quit: ")
    return action


def user_key():
    """
    Asks user how much they want to rotate the alphabet
    :return: user's answer
    """
    key = int(input("Please enter the key (0 - 25): "))
    return key


def rotate(key, alphabet):
    """
    This slices the alphabet and rotates it by the key given by the user
    :param key:
    :param alphabet:
    :return: Rotated alphabet
    """
    first = alphabet[:key]
    last = alphabet[key:]
    new_alphabet = last + first
    return new_alphabet


def encode_phrase():
    """
    Gets the phrase the user wants to encode
    :return: the phrase in lower case
    """
    en_phrase = input("Please enter the text to be encoded: ")
    return en_phrase.lower()


def encode(en_phrase, alphabet, new_alphabet):
    """
    This checks for and adds symbols in, finds the index of each letter in the alphabet and gets the letter in that
    spot in the rotated alphabet
    :param en_phrase:
    :param alphabet:
    :param new_alphabet:
    :return: the encoded phrase
    """
    encoded_phrase = ""
    for letter in en_phrase:
        if letter not in alphabet:
            encoded_phrase = encoded_phrase + letter
        else:
            index = alphabet.index(letter)
            new_letter = new_alphabet[index]
            encoded_phrase = encoded_phrase + new_letter
    return encoded_phrase


def decode_phrase():
    """
        Gets the phrase the user wants to decode
        :return: the phrase in lower case
        """
    de_phrase = input("Please enter the text to be decoded: ")
    return de_phrase.lower()


# Adds symbols in, finds index of each letter in the rotated alphabet and gets the letter in that spot in the alphabet
def decode(de_phrase, alphabet, new_alphabet):
    """
    This checks for and adds symbols in, finds the index of each letter in the rotated alphabet and gets the letter in
    that spot in the alphabet
    :param de_phrase:
    :param alphabet:
    :param new_alphabet:
    :return: the decoded phrase
    """
    decoded_phrase = ""
    for letter in de_phrase:
        if letter not in alphabet:
            decoded_phrase = decoded_phrase + letter
        else:
            index = new_alphabet.index(letter)
            new_letter = alphabet[index]
            decoded_phrase = decoded_phrase + new_letter
    return decoded_phrase


def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    action = user_action()
    if action == "q":
        print("Thanks for playing!")
    elif action == "e":
        key = user_key()
        new_alphabet = rotate(key, alphabet)
        en_phrase = encode_phrase()
        encoded_phrase = encode(en_phrase, alphabet, new_alphabet)
        print(encoded_phrase)
    elif action == "d":
        key = user_key()
        new_alphabet = rotate(key, alphabet)
        de_phrase = decode_phrase()
        decoded_phrase = decode(de_phrase, alphabet, new_alphabet)
        print(decoded_phrase)
    else:
        print("You have entered an invalid command")


main()

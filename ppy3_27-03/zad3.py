def caesar_cipher(message, key, alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                                          'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']):
    message = message.lower()
    message_list = list(message)

    for index, letter in enumerate(message_list):
        if letter not in alphabet:
            continue

        letter_index_in_alphabet = alphabet.index(letter)
        message_list[index] = alphabet[(letter_index_in_alphabet + key) % len(alphabet)]


    return "".join(message_list)


if __name__ == '__main__':
    alphabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ń', 'o', 'ó', 'p',
                'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']

    print(caesar_cipher("Testowa wiadomość szyfrem Cezara", 69, alphabet))


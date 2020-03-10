def split_word(word):
    return [char for char in word]

BASE_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE_ALPHA_LIST = split_word(BASE_ALPHA)


def caesar_offset_passphrase(offset):
    return ''.join([BASE_ALPHA[offset:], BASE_ALPHA[:offset]])

def caesar_decode(val, passphrase):
    passphrase_list = split_word(passphrase)
    decoded_val = []

    for j in split_word(val):
        decoded_val.append(BASE_ALPHA_LIST[passphrase_list.index(j)])

    return ''.join(decoded_val)

import cipher_utils

ciphers_01 = [
    "ALVLREXS",
    "BXYLLHF",
    "PELRIAOBXA"
]

#for offset in range(0, 26):

offset = 23
passphrase = cipher_utils.caesar_offset_passphrase(offset)

for i in ciphers_01:
    print cipher_utils.caesar_decode(i, passphrase)

#print "------"

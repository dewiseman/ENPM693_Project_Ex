'''
@author Derek Wiseman
 created: 05/12/2021
'''

from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad, unpad

AES_BLOCK_LEN = 16

def split_n(string, length):
    arr = [string[i: i+ length] for i in range(0, len(string), length)]
    if (len(arr[-1]) != length):
        arr[-1] = pad(arr[-1], length)
    return arr


def encrypt_msg(message, key):
    encypted_text = b''
    aes = AES.new(key, AES.MODE_ECB)
    chunks = split_n(message, AES_BLOCK_LEN)
    for chunk in chunks:
        data = aes.encrypt(chunk) 
        encypted_text += data

    return encypted_text

    
    
if __name__ == '__main__':
    aes_key = bytes.fromhex("0f1571c947d9e8590cb7add6af7f6798")
    msg = bytes.fromhex("9090909090909090909090909090909090")
    enc = encrypt_msg(msg, aes_key)
    print(str(enc) + ' -> ' + str(dec))


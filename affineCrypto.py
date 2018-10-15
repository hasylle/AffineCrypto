from euclid import *

def affine(k, mode, msg):
    """
    Affine Cryptography
    C(p) = (a*p + b) mod 26
    :param k: (a,b)
    :param mode: 1 if Encrypt mode, 0 if Decrypt mode
    :param msg: Message to be encrypted/decrypted
    :return new_msg: Ecrypted/Decrypted Message
    :except ValueError: The inverse does not exist
    """
    new_msg = ""
    a = k[0]
    b = k[1]
    if modinv(a, 26) == False:
        raise ValueError
    msg = msg.upper() #Accept lower case but return upper case
    if mode:
        for ch in msg:
            p = ord(ch) - 65
            c = (a * p + b) % 26
            new_msg = new_msg + str(chr(c+65))
        return new_msg
    else:
        for ch in msg:
            q = ord(ch) - 65
            d = modinv(a, 26) * (q-b) % 26
            new_msg = new_msg + str(chr(d + 65))
        return new_msg



if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Encrypt/Decrypt Message using Affine Crypto')
    parser.add_argument('-k', '--key', type=int,  nargs=2, help='the key (a,b)', required=True)
    parser.add_argument('-m', '--mode', type=int, nargs=1, help='1 if Encrypt mode, 0 if Decrypt mode ', required=True)
    parser.add_argument('-msg', '--message', type=str, nargs=1, help='Message to Encrypt/Decrypt', required=True)
    args = parser.parse_args()
    print(args.key)
    k = args.key
    mode = args.mode[0]
    msg = args.message[0]
    try:
        new_msg = affine(k, mode, msg)
        if mode:
            print("Encrypted message: " + new_msg)
        else:
            print("Decrypted message: " + new_msg)
    except ValueError:
        print("The inverse does not exist. Please choose a different key(a,b)")
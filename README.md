#Affine Cryptography

Python implementation of the Affine Cryptography System

Returns an encrypted/decrypted message using Affine Crypto.

Usage: 
usage: affineCrypto.py [-h] -k KEY KEY -m MODE -msg MESSAGE

Example: 
python affineCrypto.py -k 3 4 -m 1 -msg "HELLOWORLD"
result: 
Encrypted message: ZQLLUSUDLN


Algorithms used:
(affineCrypto.py)
- Encryption:
C(p) = (a*p + b) mod 26

p -> a character between A-Z
(a,b) -> keys specified by user
C(p) -> encrypted character

- Decryption:
D(q) = modinv(a,26) * (q-b)
q -> a character between A-Z
(a,b) -> keys for decryption
D(q) -> decrypted character

(euclid.py)
- Extended Euclidean
ax + by = gcd(a,b)
(a,b) -> input to gcd
(x,y) -> factors of gcd multiplied to a,b respectively

- Modular Inverse
x = 1/a (mod n)
(x * a)(mod n) == 1
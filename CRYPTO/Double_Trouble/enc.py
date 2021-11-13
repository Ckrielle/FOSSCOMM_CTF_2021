from Crypto.Util.number import *
from Crypto.Util.Padding import pad
from Crypto.PublicKey.RSA import construct
from Crypto.Cipher import AES
import os

def encrypt(key, msg):
	cipher = AES.new(key, AES.MODE_CBC, key)
	return cipher.encrypt(pad(msg, 16))

key = os.urandom(16)

dt = open('flag', 'rb').read()
enc_dt = encrypt(key, dt)

open('flag.enc', 'wb').write(enc_dt)

e = 0x10001
p = getPrime(1024)
N = pow(p, 3)
m = bytes_to_long(key)

c = pow(m, e, N)

key = construct((N, e)).exportKey('PEM')
with open('key.pem', 'w') as k:
    k.write(key.decode())

print(f"{c=}")

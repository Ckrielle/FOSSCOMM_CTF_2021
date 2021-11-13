from Crypto.Util.number import *
from flag import FLAG

m = bytes_to_long(FLAG)
p = getPrime(549)
q = getPrime(549)
e = 3
N = p * q
c = pow(m, e, N)
print(f"N = {N}")
print(f"c = {c}")

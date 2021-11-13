from flag import FLAG
import random

seed = 0x31337
random.seed(seed)

xor_values = [random.randint(1, 255) for _ in range(len(FLAG))]

ct = [i ^ j for i, j in zip(FLAG, xor_values)]
print(ct)

#!/python3
import hashlib

h = hashlib.algorithms_guaranteed

print(h)
print('==========================')
h = hashlib.algorithms_available
print(h)

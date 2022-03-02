import random
import string
from string import ascii_lowercase, digits
a = ascii_lowercase + digits
m = 0
b = ''
c = ''
for _ in range(16): 
    b = b + random.choice(a)




print(b)

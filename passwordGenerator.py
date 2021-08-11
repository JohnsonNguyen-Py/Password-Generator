# JOHNSON NGUYEN
# GITHUB: https://github.com/JohnsonNguyen-Py

import random
import string


randomChar = string.ascii_letters + string.digits

password = ""

for length in range(10):
    password = password + random.choice(randomChar)

print(password)

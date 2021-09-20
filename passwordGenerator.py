# JOHNSON NGUYEN
# GITHUB: https://github.com/JohnsonNguyen-Py

import random
import string


randomChar = string.ascii_letters + string.digits

password = ""

for length in range(10):
    password += random.choice(randomChar)  # edit made it shorter

print(password)


# List Comprehension
print("".join([random.choice(string.ascii_letters + string.digits) for length2 in range(10)]))

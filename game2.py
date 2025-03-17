# Random password generator
import random
import string

allChar = string.ascii_letters + string.digits + string.punctuation
password = ""
i = 0
while i<12:
    password += random.choice(allChar)
    i+=1

print(f"password = {password}")

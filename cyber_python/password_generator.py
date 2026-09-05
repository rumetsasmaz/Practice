import random

lower_case = "abcdefghporsnmbvxwqtop"
upper_case = "ABCDEFGHMRFCXQWTYUIO"
symbols = "!@#$%^&*-?.,|/-+><@#$%^&"

password = ""

all_chars = lower_case + upper_case + symbols

for x in range(0, 12):

    random.choice(all_chars)
    password += random.choice(all_chars)

print(password)
    
import random
import string

data = input("Enter base word: ")
psw_strength = int(input("Enter desired password length: "))

replace_code = {
    'a': '@', 'i': '1', 's': '$', 'o': '0', 'e': '3',
    't': '7', 'l': '!', 'b': '8', 'g': '9', 'z': '2'
}

transform = ""

for char in data:
    if char.lower() in replace_code:
        transform += replace_code[char.lower()]
    else:
        transform += char

chars = string.ascii_letters + string.digits

miss = psw_strength - len(transform)

if miss > 0:
    for i in range(miss):
        transform += random.choice(chars)
        
# ----- shuffle -----
# password_list = list(transform)
# random.shuffle(password_list)

# final_password = "".join(password_list)
# -----   -----


print("Generated Password:", transform)
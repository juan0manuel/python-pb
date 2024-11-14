import random

def create_password(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range (pass_length):
        password += random.choice(elements)

    print(password)

create_password(int(input("Decuantos caracteres deseas tu contraseña: ")))
import random

print("bu bir şifre oluşturucu programıdır")
ert=int(input("kaç haneli bir şifre olsun?"))
tr = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre = ""
for i in range(ert):
    sifre += random.choice(tr)

print(sifre)

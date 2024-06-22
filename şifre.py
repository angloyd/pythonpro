import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("paralo uzunluğunu giriniz"))
parola = ""

for i in range(uzunluk):
    sembol = random.choice(karakterler)
    parola += sembol
print(parola)

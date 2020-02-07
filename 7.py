import random

getal= random.randrange(0,10)
getal_ueser= int(input(" Geef een getal:"))


while getal_ueser != getal:
     guess_nr= int(input("Geef een getal: "))
print("win!")
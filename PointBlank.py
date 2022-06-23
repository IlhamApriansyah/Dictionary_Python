import random as rd

def Weapon():

    list = {"SMG" : "AK47", "SG" : "M1887", "Knife":"Kriss" }

    del list["SMG"]

    print(list)

def Character():

    list = {"Male" : "Joker","Female" : "Tarantula"}

    list["Male"] = "Anker"

    print(list)
    

print("Data yang masih tersisa adalah : ")
Weapon()
Character()

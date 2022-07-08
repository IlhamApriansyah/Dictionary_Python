from operator import index

def Weapon():

    SMG = {
        "No" : 0,
        "Nama" : "MP7",
        "Akurasi" : "40-50%",
        "Peluru" : "30/120"
    }

    Shotgun = {
        "No" : 1,
        "Nama" : "M1887",
        "Akurasi" : "70%",
        "Peluru" : "8/16"
    }

    Machine_Gun = {
        "No" : 2,
        "Nama" : "Barreta",
        "Akurasi" : "30-40%",
        "Peluru" : "60/200"
    }

    Knife = {
        "No" : 3,
        "Nama" : "MP7",
        "Akurasi" : "-",
        "Peluru" : "-"
    }

    Bom = {
        "No" : 4,
        "Nama" : "Ketupat",
        "Akurasi" : "-",
        "Peluru" : "-"
    }

    print(SMG.values())

def Character():

    list = {"Male" : "Joker","Female" : "Tarantula"}

    list["Male"] = "Anker"

    print(list)
    

print("Data yang masih tersisa adalah : ")

if __name__ == "__main__":
    Weapon()
    Character()

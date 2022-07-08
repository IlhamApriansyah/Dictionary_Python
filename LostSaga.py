from ast import Set
from operator import index

def Normal():
    Contest = {
        "Number": 0,
        "Name":"Ganesha",
        "Upgrade-able":"Att+Spd"
    }

    Content = {
        "Number" : 1,
        "Name" : "Red Hood",
        "Upgrade-able" : "Att"
    }

    print("Data yang dipanggil adalah hero :" + Content["Name"])
    print("Lebih cocok di-upgrade ke :" + Content["Upgrade-able"])

def Premium():
    Blazeblue = {
                "Number": 0,
                "Name":"Ragna",
                "Upgrade-able":"Att"
                }

    print("Data yang dipanggil adalah hero : " + Blazeblue["Name"])
    print("Lebih cocok di-upgrade ke : " + Blazeblue["Upgrade-able"])

Normal()
Premium()
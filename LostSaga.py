from ast import Set
from operator import index

def Normal():
    Contest = {
        "Number": 0,
        "Name":"Ganesha",
        "Upgrade-able":"Att+Spd"
    }

    Contest2 = {
        "Number" : 2,
        "Name" : "Pencak Silat",
        "Upgrade-able" : "Att+Spd"
    }

    Content = {
        "Number" : 1,
        "Name" : "Red Hood",
        "Upgrade-able" : "Att"
    }

    Content2 = {
        "Number" : 2,
        "Name" : "Nang In",
        "Upgrade-able" : "Att+Spd"
    }

    
    print("Data yang dipanggil adalah hero :" + Content["Name"])
    print("Lebih cocok di-upgrade ke :" + Content["Upgrade-able"])

def Premium():
    Blazeblue = {
        "Number": 0,
        "Name":"Ragna",
        "Upgrade-able":"Att"
    }

    Blazeblue2 = {
        "Number" : 1,
        "Name" : "Jin Kisaragi",
        "Upgrade-able" : "Spd"
    }

    Blazeblue3 = {
        "Number" : 2,
        "Name" : "Hazama",
        "Upgrade-able" : "Att+Spd"
    }

    print("Data yang dipanggil adalah hero : " + Blazeblue["Name"])
    print("Lebih cocok di-upgrade ke : " + Blazeblue["Upgrade-able"])

Normal()
Premium()
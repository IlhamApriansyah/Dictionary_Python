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

    print("Kata kunci : " + Contest.keys() + Content.keys())
    print("Data nya : " + Contest.values() + Content.values())

def Premium():
    Blazeblue = {
                "Number": 0,
                "Name":"Ragna",
                "Upgrade-able":"Att"
                }

    print("kata kunci : " + Blazeblue.keys())
    print("Data nya : " + Blazeblue.values())

Normal()
Premium()
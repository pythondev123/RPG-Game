import os
from gamefiles.otherfunc import *
from gamefiles.inventoryfunc import *
from gamefiles.economy import *
def shop():
    os.system("cls")
    print("==============Shop===============")
    print("""
1 - Weapons
2 - Armor
3 - Go Back""")
    shopchoose = input("Choose - ")
    if shopchoose==1:
        weapon_shop()
    elif shopchoose==2:
        armor_shop()
    elif shopchoose==3:
        return True
        

def weapon_shop():
    os.system("cls")
    print("==========Weapon Shop===========")
    print("""
1 - Swords
2 - Spears (Will be implimented soon)
3 - Go Back""")
    weaponshopchoose = input("Choose - ")
    if weaponshopchoose==1:
        sword_shop()
    elif weaponshopchoose==2:
        print("Its coming soon")
        weapon_shop()
    elif weaponshopchoose==3:
        shop()
        
def armor_shop():
    os.system("cls")
    print("==========Armor Shop===========")
    print("""
1 - Body Armor
2 - Helmet (Will be implemented soon)
3 - Go Back""")
    armorshopchoose = input("Choose - ")
    if armorshopchoose==1:
        bodyarmor_shop()
    elif armorshopchoose==2:
        print("Its coming soon")
        armor_shop()
    elif armorshopchoose==3:
        shop()
        
        
def sword_shop():
    os.system("cls")
    print("==========Sword Shop===========")
    print("""
1 - Lvl 1 Sword     |     250 Credits     |     +30 Atk
2 - Lvl 2 Sword     |     500 Credits     |     +60 Atk
3 - Lvl 3 Sword     |     1000 Credits    |     +90 Atk
4 - Go Back""")
    swordshopchoose = input("Choose - ")
    if swordshopchoose==4:
        weapon_shop()
    confirmation = confirm_option()
    if confirmation==True:
        if swordshopchoose==1:
            try:
                sub("Money",250)
            except:
                print("You don't have enough credits")
            else:
                sub("Money",250)
                add("Atk",30)
                
        elif swordshopchoose==2:
            try:
                sub("Money",500)
            except:
                print("You don't have enough credits")
            else:
                sub("Money",500)
                add("Atk",60)
                
        elif swordshopchoose==3:
            try:
                sub("Money",1000)
            except:
                print("You don't have enough credits")
            else:
                sub("Money",1000)
                add("Atk",90)
    else:
        sword_shop()
                
def bodyarmor_shop():
    os.system("cls")
    print("==========Body Armor Shop===========")
    print("""
1 - Lvl 1 Armor     |     300 Credits     |     +30 Health
2 - Lvl 2 Armor     |     600 Credits     |     +60 Health
3 - Lvl 3 Armor     |     1200 Credits    |     +90 Health
4 - Go Back""")
    bodyarmorshopchoose = input("Choose - ")
    if bodyarmorshopchoose==4:
        armor_shop()
    confirmation = confirm_option()
    if confirmation==True:
        if bodyarmorshopchoose==1:
            try:
                sub("Money",250)
            except:
                print("You don't have enough credits")
            else:
                sub("Money",250)
                add("Health",30)
                
        elif bodyarmorshopchoose==2:
            try:
                sub("Money",500)
            except:
                print("You don't have enough credits")
            else:
                sub("Money",500)
                add("Health",60)
                
        elif bodyarmorshopchoose==3:
            try:
                sub("Money",1000)
            except:
                print("You don't have enough credits")
            else:
                sub("Money",1000)
                add("Health",90)
    else:
        bodyarmor_shop()
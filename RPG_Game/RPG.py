import os
from gamefiles.levels import *
from gamefiles.economy import *
from RPG_Game.gamefiles.shop import shop

os.system("cls")

def starting():
    global Health
    global Atk
    global Money
    Health = get("Health")
    Atk = get("Atk")
    Money = get("Money")
    os.system("cls")
    print("""Welcome to RPG 
Enter to start""")
    input("")

    home()


def home():
    os.system("cls")
    print("==========RPG==========")
    print("""1 - Check Stats
2 - Battle
3 - Shop
4 - Inventory""")
    a = input("Type number to select - ")
    if a=="1":
        stats()
    elif a=="2":
        battle()
    elif a=="3":
        bruh = shop()
        if bruh==True:
            home()
        else:
            shop()
        
        
        
def stats():
    os.system("cls")
    Health = get("Health")
    Atk = get("Atk")
    Money = get("Money")
    print("Health - ", Health)
    print("Attack - ", Atk)
    print("Money - ", Money)
    print(input("\nEnter to return:"))
    home()
    
    
def battle():
    os.system("cls")
    print("==========Battle==========")
    print("""1 - Lvl 1
2 - Lvl 2
3 - Lvl 3
4 - Back""")
    battle_lvl = input("\nChoose Lvl - ")
    if battle_lvl=="1":
        lvl1()
    elif battle_lvl=="2":
        lvl2()
    elif battle_lvl=="3":
        lvl3()
    elif battle_lvl=="4":
        home()
    home()
    
starting()

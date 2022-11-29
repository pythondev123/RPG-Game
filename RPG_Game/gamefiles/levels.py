import os
from gamefiles.fight_ai import *
from gamefiles.economy import *
from gamefiles.otherfunc import *

def updatestats():
    global Health
    global Atk
    global Money
    Health = get("Health")
    Atk = get("Atk")
    Money = get("Money")
    return Health,Atk,Money

def won(m,w):
    os.system("cls")
    print("=======Battle========")
    print("You won " + str(w))
    print("Your current balance - " + str(m))
    input("\nEnter to return:")

def lost():
    os.system("cls")
    print("=======Battle========")
    print("You Lost :(")
    input("\nEnter to return:")
    
    
def lvl1():
    updatestats()
    os.system("cls")
    EnemyH = 50
    Enemyatk = 30
    Win = fight(health=Health,atk=Atk,enemyh=EnemyH,enemyatk=Enemyatk)
    if Win==True:
        add("Money",50)
        m = get("Money")
        w = 50
        won(m,w)
    else:
        lost()
    
def lvl2():
    updatestats()
    os.system("cls")
    EnemyH = 150
    Enemyatk = 60
    Win = fight(health=Health,atk=Atk,enemyh=EnemyH,enemyatk=Enemyatk)
    if Win==True:
        add("Money",100)
        m = get("Money")
        w = 50
        won(m,w)
    else:
        lost()
    
def lvl3():
    updatestats()
    os.system("cls")
    EnemyH = 300
    Enemyatk = 90
    Win = fight(health=Health,atk=Atk,enemyh=EnemyH,enemyatk=Enemyatk)
    if Win==True:
        add("Money",200)
        m = get("Money")
        w = 50
        won(m,w)
    else:
        lost()
    
def lvl4():
    updatestats()
    os.system("cls")
    EnemyH = 600
    Enemyatk = 150
    Win = fight(health=Health,atk=Atk,enemyh=EnemyH,enemyatk=Enemyatk)
    if Win==True:
        add("Money",300)
        m = get("Money")
        w = 50
        won(m,w)
    else:
        lost()
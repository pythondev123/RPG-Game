import os
from fight_ai import *
from economy import *
from otherfunc import *


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
    Enemyatk = 20
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
    EnemyH = 100
    Enemyatk = 40
    Win = fight(health=Health,atk=Atk,enemyh=EnemyH,enemyatk=Enemyatk)
    if Win==True:
        add("Money",150)
        m = get("Money")
        w = 50
        won(m,w)
    else:
        lost()
    
def lvl3():
    updatestats()
    os.system("cls")
    EnemyH = 150
    Enemyatk = 60
    Win = fight(health=Health,atk=Atk,enemyh=EnemyH,enemyatk=Enemyatk)
    if Win==True:
        add("Money",250)
        m = get("Money")
        w = 50
        won(m,w)
    else:
        lost()
    
def lvl4():
    updatestats()
    os.system("cls")
    EnemyH = 150
    Enemyatk = 60
    Win = fight(health=Health,atk=Atk,enemyh=EnemyH,enemyatk=Enemyatk)
    if Win==True:
        add("Money",350)
        m = get("Money")
        w = 50
        won(m,w)
    else:
        lost()
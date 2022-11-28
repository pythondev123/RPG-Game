import os
import time

def fight(health,atk,enemyh,enemyatk):
    os.system("cls")
    print("==========Fight==========\n")
    print("\n-------------")
    print("Your health -   "+str(health))
    print("Enemy health -   "+str(enemyh))
    print("-------------\n")
    time.sleep(1)
        
    while int(health) > 0 and int(enemyh) > 0:
        print("\n==============")
        print(input("Enter to attack:"))
        print("==============")
        enemyh = int(enemyh) - int(atk)
        time.sleep(1)
        
        print("-------------")
        print("Your health -   "+str(health))
        print("Enemy health -   "+str(enemyh))
        print("-------------\n")
        time.sleep(1)
       
        print("")
        print("\n==============")
        print("Enemy attacked")
        print("==============")
        health = int(health) - int(enemyatk)
        print("\n-------------")
        print("Your health -   "+str(health))
        print("Enemy health -   "+str(enemyh))
        print("-------------\n")
        time.sleep(1)
    
    if int(health) > int(enemyh):
        Win = True
    else: 
        Win = False
        
    return Win
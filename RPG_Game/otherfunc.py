from economy import *

def updatestats():
    global Health
    global Atk
    global Money
    Health = get("Health")
    Atk = get("Atk")
    Money = get("Money")
    return Health,Atk,Money
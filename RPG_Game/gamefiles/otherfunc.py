from gamefiles.economy import *
def updatestats():
    global Health
    global Atk
    global Money
    Health = get("Health")
    Atk = get("Atk")
    Money = get("Money")
    return Health,Atk,Money

def confirm_option():
    confirmation = print("\nType 1 to confirm - ")
    if confirmation == 1:
        confirmation = True
    else:
        confirmation = False
    
    return confirmation
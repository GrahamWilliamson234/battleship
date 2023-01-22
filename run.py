from random import randrange
import random
from time import *

def check_ok(vessel,taken):
    
    vessel.sort()
    for i in range(len(vessel)):
        num = vessel[i]
        if num in taken:
            vessel = [-1]
            break            
        elif num < 0 or num > 99:
            boat = [-1]
            break
        elif num % 10 == 9 and i < len(vessel)-1:
            if vessel[i+1] % 10 == 0:
                vessel = [-1]
                break 
        if i != 0:
            if vessel[i] != vessel[i-1]+1 and vessel[i] != vessel[i-1]+10:
                vessel = [-1]
                break

    return vessel

def hello():
    name = str(input("Please enter your name: "))
    print("\033[0;31;40m\n")
    print("                              ")
    print ("Welcome Fleet Commander "  + str(name)) 
    print("                              ")
    print("Sir,                          ")
    print("your ships await your orders. ")
    print("Contacting your ships now...  ")
    return
hello()

def timer():
    start_timer = time()
    struct = localtime( start_timer)
    print("\nContacting Ships At:" , strftime("%x" , struct))
    i = 10
    while i > -1:
        print(i)
        i -= 1
        sleep(1)
    end_timer = time()
    difference = round(end_timer - start_timer)
    print("\033[1;31;47m\n")
    print("")
    print("       _____  ____                                  ____      ")
    print("     |   |   |             \            /   /\     |    \     ")
    print("     |   |   |___           \    /\    /   /  \    | ___/     ")
    print("     |   |       |           \  /  \  /   /----\   |    \     ")
    print("     |   |   ____|            \/    \/   /      \  |     \    ")
    print("                                                              ")
    return
timer()

def get_ship(long,taken):

    ok = True
    while ok:      
        ship = []
        print("")
        print("                      0 1 2 3 4 5 6 7 8 9 ")
        print("                   0  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
        print("                   1  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
        print("                   2  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
        print("                   3  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
        print("                   4  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
        print("                   5  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
        print("                   6  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
        print("                   7  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
        print("                   8  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
        print("                   9  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
        print("")
        print("             Let's get your Navy ready for battle")
        print("            Enter your coordinates for ship of length ",long)
        for i in range(long):
            vessel_num = input("              Please enter a coordinate number ")
            ship.append(int(vessel_num))       
        ship = check_ok(ship,taken)
        if ship[0] != -1:
            taken = taken + ship
            break
        else:
           print("ERROR - Please try again") 
        
    return ship,taken
       

from random import randrange
import random
from time import time, localtime, strftime, sleep

# check


def check_ok(vessel, taken):
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

# hello


def hello():
    while True:
        name = input("Please enter your name: ")
        if name:
            break
        print("Error: name cannot be empty. Please try again.")

    while True:
        rank = input("Please enter your rank: ")
        if rank:
            break
        print("Error: rank cannot be empty. Please try again.")

    print()
    print(f"Welcome Fleet {rank} {name}")
    print(" ")
    print("Sir,")
    print(f"Your ships await your orders, {rank}.")
    print("Attempting to contact your fleet now...")


hello()

# timer


def timer():
    start_timer = time()
    struct = localtime(start_timer)
    print("\nContacting Ships On:", strftime("%x", struct))
    i = 5
    while i > -1:
        print(i)
        i -= 1
        sleep(1)
    end_timer = time()
    difference = round(end_timer - start_timer)
    print("\033[1;31;47m\n")
    print("         Let the War begin..         ")
    return


timer()

# get ships


def get_ship(long, taken):
    while True:
        ship = []
        print("\033[1;31;47m")

# Print game board
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
# print commands
        print("Enter your coordinates for ship of length ", long)
        for i in range(long):
            while True:
                try:
                    vessel_num = int(input("Enter a coordinate number: "))
                    if vessel_num not in range(99):
                        raise ValueError
                    if vessel_num in ship:
                        raise ValueError("Already entered coordinate!")
                    break
                except ValueError:
                    print("Invalid Enter an integer between 0 and 99.")

            ship.append(vessel_num)

# Check if the ship is valid
        ship = check_ok(ship, taken)
        if ship[0] != -1:
            taken += ship
            return ship, taken
        else:
            print("ERROR: The coordinates are invalid. Please again.")

# create ships


def create_ships(taken, vessels):

    ships = []
    for vessel in vessels:
        ship, taken = get_ship(vessel, taken)
        ships.append(ship)
    return ships, taken

# check vessel


def check_vessel(b, start, dirn, taken):
    vessel = []
    if dirn == 1:
        for i in range(b):
            vessel.append(start - i*10)
    elif dirn == 2:
        for i in range(b):
            vessel.append(start + i)
    elif dirn == 3:
        for i in range(b):
            vessel.append(start + i*10)
    elif dirn == 4:
        for i in range(b):
            vessel.append(start - i)
    vessel = check_ok(vessel, taken)
    return vessel
# check boats


def create_boats(taken, boats):

    ships = []
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1, 4)
            boat = check_vessel(b, boat_start, boat_direction, taken)
        ships.append(boat)
        taken = taken + boat
    return ships, taken

# show board taken


def show_board_c(taken):
    print("")
    print("")
    print("          Battle of the Atlantic    ")
    print("                It's War    ")
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " ~ "
            if place in taken:
                ch = " o "
            row = row + ch
            place = place + 1
        print(x, " ", row)


# get shot sink
def get_shot_sink(guesses, tactics):
    ok = "n"
    while ok == "n":
        try:
            if len(tactics) > 0:
                shot = tactics[0]
            else:
                shot = randrange(99)
            if shot not in guesses:
                ok = "y"
                guesses.append(shot)
                break
        except Exception as e:
            print("Incorrect entry - Please enter again: ", e)
    return shot, guesses


# show board
def show_board(hit, miss, sink):
    print("         Battle of the Sea's    ")
    print("               It's War    ")
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " ~ "
            if place in miss:
                ch = " O "
            elif place in hit:
                ch = " X "
            elif place in sink:
                ch = " / "
            row = row + ch
            place = place + 1
        print(x, " ", row)


# check shot
def check_shot(shot, ships, hit, miss, sink):
    missed = 0
    for i in range(len(ships)):
        if shot in ships[i]:
            ships[i].remove(shot)
            if len(ships[i]) > 0:
                hit.append(shot)
                missed = 1
            else:
                sink.append(shot)
                missed = 2
    if missed == 0:
        miss.append(shot)
    return ships, hit, miss, sink, missed


# tactics
def calc_tactics(shot, tactics, guesses, hit):
    temp = []
    if len(tactics) < 1:
        temp = [shot-1, shot+1, shot-10, shot+10]
    else:
        if shot-1 in hit:
            temp = [shot+1]
            for num in [2, 3, 4, 5, 6, 7, 8]:
                if shot-num not in hit:
                    temp.append(shot-num)
                    break
        elif shot+1 in hit:
            temp = [shot-1]
            for num in [2, 3, 4, 5, 6, 7, 8]:
                if shot+num not in hit:
                    temp.append(shot+num)
                    break
        if shot-10 in hit:
            temp = [shot+10]
            for num in [20, 30, 40, 50, 60, 70, 80]:
                if shot-num not in hit:
                    temp.append(shot-num)
                    break
        elif shot+10 in hit:
            temp = [shot-10]
            for num in [20, 30, 40, 50, 60, 70, 80]:
                if shot+num not in hit:
                    temp.append(shot+num)
                    break
    cand = []
    for i in range(len(temp)):
        if temp[i] not in guesses and temp[i] < 100 and temp[i] > -1:
            cand.append(temp[i])
    random.shuffle(cand)
    return cand


# get shot
def get_shot(guesses):
    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter firing coordinates ")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("Incorrect Coordinates, Please fire again")
            elif shot in guesses:
                print("Incorrect Coordinates, already tried before")
            else:
                ok = "y"
                break
        except ValueError:
            print("Incorrect Coordinates - Please enter again")
    return shot

# check list


def check_if_empty_2(list_of_lists):
    return all([not elem for elem in list_of_lists])


hit1 = []
miss1 = []
sink1 = []
guesses1 = []
missed1 = 0
tactics1 = []
taken1 = []
taken2 = []
hit2 = []
miss2 = []
sink2 = []
guesses2 = []
missed2 = 0
tactics2 = []

battleships = [5, 4, 3, 3, 2]
ships1, taken1 = create_boats(taken1, battleships)
ships2, taken2 = create_ships(taken2, battleships)
show_board_c(taken2)

for i in range(100):

    guesses1 = hit1 + miss1 + sink1
    shot1 = get_shot(guesses1)
    ships1, hit1, miss1, sink1, missed1 = check_shot(
        shot1, ships1, hit1, miss1, sink1
    )
    show_board(hit1, miss1, sink1)
    if check_if_empty_2(ships1):
        print("                 You are the Winner in", i)
        print("")
        print("                      Let there be peace")
        break
    shot2, guesses2 = get_shot_sink(guesses2, tactics2)
    ships2, hit2, miss2, sink2, missed2 = check_shot(
        shot2, ships2, hit2, miss2, sink2
    )
    show_board(hit2, miss2, sink2)
    if missed2 == 1:
        tactics2 = calc_tactics(shot2, tactics2, guesses2, hit2)
    elif missed2 == 2:
        tactics2 = []
    elif len(tactics2) > 0:
        tactics2.pop(0)

    if check_if_empty_2(ships2):
        print("End of the War - Your enemy wins", i)
        print("Time to re-group and fight another day")
        break

# reset code below


def create_ships(taken, vessels):

    ships = []
    for vessel in vessels:
        ship, taken = get_ship(vessel, taken)
        ships.append(ship)
    return ships, taken


def create_boats(taken, boats):

    ships = []
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1, 4)
            boat = check_vessel(b, boat_start, boat_direction, taken)
        ships.append(boat)
        taken = taken + boat
    return ships, taken


def main():
    taken = []
    ships, taken = create_ships(taken, [5, 4, 3, 3, 2])
    boats, taken = create_boats(taken, [5, 4, 3, 3, 2])
    print("The enemy has placed their ships and boats on the board.\n")
    guesses = []
    tactics = []
    shots = 0
    hits = 0
    show_board_c(guesses)
    while hits < 100:
        try:
            shot, sink, tactics = get_shot_sink(guesses, tactics)
            shots += 1
            if sink:
                print("You sank the enemy's", sink)
            if shot in taken:
                print("Direct hit!")
                hits += 1
            else:
                print("Miss!")
            guesses.append(shot)
            show_board_c(guesses)
        except ValueError:
            print("Invalid input. Please try again.")
            continue
    print("You won the battle in", shots, "shots!")
    return


while True:
    answer = input("Do you want to play again? (y/n): ")
    if answer.lower() == "y":
        main()
    elif answer.lower() == "n":
        print("Thanks for playing! GOODBYE.")
        break
    else:
        print("Invalid input. Please try again.")
    break

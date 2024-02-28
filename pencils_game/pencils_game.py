import random

while True:
    try:
        pencil = int(input("How many pencils > "))
        if pencil == 0:
            print("The number of pencils should be positive")
            continue
        else:
            if pencil < 0:
                print("The number of pencils should be positive")
                continue
        break
    except ValueError:
        print("The number of pencils should be numeric")
pencil1 = pencil # стартове значення олівців
Name1 = input("Please enter a Name1 > ") # ім'я першого користувача
Name2 = input("Please enter a Name2 for the bot > ") # ім'я другого користувача (Бота)
print (f"Who will be the first {Name1,Name2}")
while True:
    The_first_move = str(input("please enter who chooses first > "))
    if The_first_move == Name1 or The_first_move == Name2:
        break
    else:
        print("Choose between *Name1* and *Name2*")
        continue
vertical_bar = ""

while pencil1 > 0:
    vertical_bar += "|"
    pencil1 = pencil1 - 1

print (vertical_bar)
print (f"{The_first_move} is going first")

while pencil > 0:
    while True:
        if The_first_move == Name1:
            pick_up_pencils = float(input("take the pencils > "))
        else:
            pick_up_pencils = random.choice([1, 2, 3])
        pencils_taken = vertical_bar.count("|")
        if pick_up_pencils == 1:
            break
        elif pick_up_pencils == 2:
            break
        elif pick_up_pencils == 3:
            break
        else:
            print ("Possible values: '1', '2' or '3'")
        continue
    while pick_up_pencils > pencils_taken:
        if The_first_move == Name1:
            pick_up_pencils = float(input("take the pencils > "))
        else:
            pick_up_pencils = random.choice([1, 2, 3])
        print("Too many pencils were taken")
        continue
    vertical_bar = vertical_bar [:- int(pick_up_pencils)]
    pencil = pencil - pick_up_pencils
    pencils_taken = vertical_bar.count("|")
    while True:
        if pencils_taken == 0:
            if The_first_move == Name1:
                print (f"{Name1} won!")
                break
            else:
                if The_first_move == Name2:
                    print (f"{Name2} won!")
                break
        if The_first_move == Name1:
            print (f"{Name1} turn!")
            The_first_move = Name2
            break
        else:
            if The_first_move == Name2:
                print (f"{Name2} turn!")
                The_first_move = Name1
            break
    print (vertical_bar)
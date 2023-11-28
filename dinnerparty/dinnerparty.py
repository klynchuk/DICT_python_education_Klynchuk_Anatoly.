import random
imenа_dict = {} #imena_list =[] [234234,234234]? список того де зберігається наші імена

print ("Enter the number of friends joining (including you):")

slovo = int(input("> "))   #тут зберігається кількість людей

a = 1

if slovo <= 0:
    print("No one is joining for the party")
else:
     print("Enter the name of every friend (including you),each on a new line:")

     while slovo >= a:
        a = a + 1
        z = input("> ") # тут вводяться імена людей
        imenа_dict[z] = 0

print ("Enter the total amount:")

l = int(input("> "))   #рахунок

print ("Who is lucky?")
y = input("> ")
print ("Do you want to use the 'Who is lucky?' feature? Write yes/no:")
if y.lower() == "yes":
    p = random.choice(list(imenа_dict.keys()))
    for name in imenа_dict:
        if name == p:
            continue
        imenа_dict[name] = round(l / (slovo-1), 2)
    print(f"{p} is the lucky one!")
    print(imenа_dict)
else:
    for name in imenа_dict:
        imenа_dict[name] = round(l / slovo, 2)
    print (imenа_dict)
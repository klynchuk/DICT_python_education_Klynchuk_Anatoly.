imenа_dict = {} #imena_list =[] [234234,234234]? список того где хранится наши имена
print ("Enter the number of friends joining (including you):")
slovo = int(input("> "))   #тут храница кол-во людей
a = 1
if slovo <= 0:
    print("No one is joining for the party")
else:
     print("Enter the name of every friend (including you),each on a new line:")

     while slovo >= a:
        a = a + 1
        z = input("> ") # тут вводятся имена людей
        imenа_dict[z] = 0

     print ("list name",imenа_dict)

print ("Enter the total amount:")
l = int(input("> "))   #счёт
for name in imenа_dict:
        imenа_dict[name] = round(l / slovo, 2)
print (imenа_dict)
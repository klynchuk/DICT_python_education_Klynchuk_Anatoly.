imena_list =[] # imenа_dict = {} [234234:0,234234:0]? список того где хранится наши имена
print ("Enter the number of friends joining (including you):")
slovo = int(input("> "))
a = 1
if slovo <= 0:
    print("No one is joining for the party")
else:
     print("Enter the name of every friend (including you),each on a new line:")
     while slovo >= a:
        a = a + 1
        z = input("> ")
        imena_list.append(z)
     print ("list name",imena_list)

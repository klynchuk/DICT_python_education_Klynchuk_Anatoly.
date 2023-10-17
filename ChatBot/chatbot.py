x = input("your name:") # перша змінна
i = 0 # друга змінна
print ("Hello! My name is BOT.")
print ("I was created in 2023.")
print ("Please, remind me your name.")
print ("What a great name you have:",x)
print ("Let me guess your age.")
print ("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int (input("day:")) # третя змінна
remainder5 = int (input("month:")) # четверта змінна
remainder7 = int (input("year:")) # п'ята змінна
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105 # шоста змінна
print (f"Your age is {age}; that's a good time to start programming!")
n = int (input("write number:"))
while i < n:
    print (f"{i}!")
    i = i + 1
print ("Let's test your programming knowledge.")
print ("Why do we use methods?")
print ("1. To repeat a statement multiple times.")
print ("2. To decompose a program into several small subroutines.")
print ("3. To determine the execution time of a program.")
print ("4. To interrupt the execution of a program.")
while True:
    a = int(input("enter the correct answer:")) # сьома змінна
    if a == 2:
        print("Completed, have a nice day!")
        break
    else:
        print ("Please, try again.")
print ("Congratulations, have a nice day!")

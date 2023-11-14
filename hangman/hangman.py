import random

print ("HANGMAN")
print ("The game will be available soon.")
print ("please enter the word")

while True:
    print("please enter play if you want to play or exit if you want to exit")
    k = input()
    if k == 'exit':
        break  # Вихід з циклу, якщо користувач ввів "exit"
    else:
        if k == 'play':
            i = ["python", "java", "javascript", "php"]  # список слів
            p = random.choice(i) # вибирається випадкове слово зі списку
            l = 8   # кількість життів
            z = "-" * len(p)  # кінцева підказка
            t = set()  # запис кожного символу введеного користувачем
            t.clear()  # чиститься пам'ять
            print("Guess the word", z)
            while l > 0:
                k = input("Input a letter: > ")
                if len(k[:1]) == k.islower():
                    if len(k) == 1 and k.isalpha():
                        if k in p and k[0] not in t:
                            t.add(k)
                            for i in range(len(p)):
                                if p[i] == k:
                                    z = z[:i] + k + z[i + 1:]
                            print(z)
                            if (z == p):
                                print("You survived!")
                                break
                        else:
                            if (k in t):
                                print("You've already guessed this letter")
                            else:
                                if (l > 0):
                                    l = l - 1
                                    print("That letter doesn't appear in the word")
                                    t.add(k[0])

                                if (l == 0):
                                    print ("You lost!")
                                    break
                    else:
                        print("You should input a single letter")
                else:
                    if (len(k) == k.isalpha() and k.islower()): #помилка при вписуванні Re і eR (текст один і той же)
                        print("You should input a single letter")
                    else:
                        print("Please enter a lowercase English letter")
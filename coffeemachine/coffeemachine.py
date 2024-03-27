class CoffeeMachine:
    def __init__(self):
        # Ініціалізація початкового стану кавоварки
        self.ml_of_water = 400
        self.ml_of_milk = 540
        self.grams_of_coffee = 120
        self.cups_available = 9
        self.earnings = 550

    def print_status(self):
        # Друк поточного стану кавоварки
        print(f"Залишок води: {self.ml_of_water} мл")
        print(f"Залишок молока: {self.ml_of_milk} мл")
        print(f"Залишок кави: {self.grams_of_coffee} г")
        print(f"Залишок одноразових стаканчиків: {self.cups_available}")
        print(f"Виручка: {self.earnings} грн")

    def prepare_coffee(self, water_needed, milk_needed, coffee_needed, price, coffee_type):
        # Приготування кави
        if self.ml_of_water >= water_needed and self.ml_of_milk >= milk_needed and \
                self.grams_of_coffee >= coffee_needed and self.cups_available >= 1:
            print(f"Ваш {coffee_type} готовий! Смачного!")
            self.ml_of_water -= water_needed
            self.ml_of_milk -= milk_needed
            self.grams_of_coffee -= coffee_needed
            self.cups_available -= 1
            self.earnings += price
        else:
            print(f"Вибачте, не вдалося приготувати {coffee_type}. Недостатньо інгредієнтів або одноразових стаканчиків.")

    def refill_machine(self, water, milk, coffee, cups):
        # Поповнення запасів кавоварки
        self.ml_of_water += water
        self.ml_of_milk += milk
        self.grams_of_coffee += coffee
        self.cups_available += cups

    def take_money(self):
        # Забір виручки з кавоварки
        print(f"Ви забираєте {self.earnings} грн. з кавоварки.")
        self.earnings = 0

    def process_input(self, user_input):
        # Обробка вводу користувача
        try:
            while True:
                if user_input == "1":
                    print("Оберіть тип кави:")
                    print("1 - еспресо")
                    print("2 - латте")
                    print("3 - капучіно")
                    coffee_type = input("Ваш вибір: ")
                    if coffee_type in ["1", "2", "3"]:
                        if coffee_type == "1":
                            self.prepare_coffee(250, 0, 16, 4, "еспресо")
                        elif coffee_type == "2":
                            self.prepare_coffee(350, 75, 20, 7, "латте")
                        elif coffee_type == "3":
                            self.prepare_coffee(200, 100, 12, 6, "капучино")
                        break  # Вийти з циклу після успішної обробки вводу
                    else:
                        print("Неправильний вибір. Спробуйте ще раз.")
                elif user_input == "2":
                    water = int(input("Скільки мілілітрів води ви хочете додати в кавоварку?: "))
                    milk = int(input("Скільки мілілітрів молока ви хочете додати в кавоварку?: "))
                    coffee = int(input("Скільки грамів кави ви хочете додати в кавоварку?: "))
                    cups = int(input("Скільки одноразових стаканчиків ви хочете додати в кавоварку?: "))
                    self.refill_machine(water, milk, coffee, cups)
                    break  # Вийти з циклу після успішної обробки вводу
                elif user_input == "3":
                    self.take_money()
                    break  # Вийти з циклу після успішної обробки вводу
                elif user_input == "4":
                    self.print_status()
                    break  # Вийти з циклу після успішної обробки вводу
                elif user_input == "5":
                    print("Спасибі за використання! До побачення!")
                    exit()
                else:
                    print("Неправильний вибір. Спробуйте ще раз.")
                    user_input = input("Ваш вибір: ")  # Запитати користувача знову
        except ValueError:
            print("Помилка: Будь ласка, введіть коректні числові значення.")

# Створення екземпляра кавоварки
coffee_machine = CoffeeMachine()

# Основний цикл програми
while True:
    print("\n Оберіть дію:")
    print("1. Приготувати каву")
    print("2. Поповнити запаси")
    print("3. Забрати гроші")
    print("4. Перевірити стан кавоварки")
    print("5. Вийти з програми")

    user_input = input("Ваш вибір: ")
    coffee_machine.process_input(user_input)


def rhombus_of_stars():
    def print_stars_in_row(spaces_count: int, stars_count: int):
        print(" " * spaces_count + "* " * stars_count)

    def print_upper_triangle(num):
        for row in range(1, num + 1):
            print_stars_in_row(num - row, row)

    def print_lower_triangle(num):
        for row in range(1, num + 1):
            print_stars_in_row(row, num - row)

    def print_rhombus(n: int):
        print_upper_triangle(n)
        print_lower_triangle(n)

    number = int(input().strip())
    print_rhombus(number)


##Scope Mess

# x = "global"
#
# def outer():
#     x = "local"
#
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)
#
#     def change_global():
#         global x
#         x = "global: changed!"
#
#     print("outer:", x)
#     inner()
#     print("outer:", x)
#     change_global()
#
#
# print(x)
# outer()
# print(x)

class Book:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages


# book = Book("My Book", "Me", 200)
# print(book.name)
# print(book.author)
# print(book.pages)


class Car:
    def __init__(self, name: str, model: str, engine: str):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f'This is {self.name} {self.model} with engine {self.engine}'


#
# car = Car("Kia", "Rio", "1.3L B3 I4")
# print(car.get_info())


class Music:
    def __init__(self, title: str, artist: str, lyrics: str):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


# song = Music("Title", "Artist", "Lyrics")
# print(song.print_info())
# print(song.play())


class Shop:
    def __init__(self, name: str, items: list[str]):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


# shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
# print(shop.get_items_count())


class Hero:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage: int) -> str | None:
        self.health -= damage

        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"
        return None

    def heal(self, amount: int):
        self.health += amount


# hero = Hero("Peter", 100)
# print(hero.defend(50))
# hero.heal(50)
# print(hero.defend(99))
# print(hero.defend(1))

class Employee:
    def __init__(self, employee_id: int, first_name: str, last_name: str, salary: int):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def raise_salary(self, param):
        self.salary += param
        return self.salary

    def get_annual_salary(self):
        return self.salary * 12


# employee = Employee(744423129, "John", "Smith", 1000)
# print(employee.get_full_name())
# print(employee.raise_salary(500))
# print(employee.get_annual_salary())

class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, param):
        free_space = self.size - self.quantity
        if free_space >= param:
            self.quantity += param
        return self.quantity

    def status(self):
        return self.size - self.quantity


# cup = Cup(100, 50)
# print(cup.status())
# cup.fill(40)
# cup.fill(20)
# print(cup.status())

class Flower:
    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity: int):
        self.is_happy = True if quantity >= self.water_requirements else False

    def status(self):
        is_happy = "" if self.is_happy else "not "
        return f'{self.name} is {is_happy}happy'


# flower = Flower("Lilly", 100)
# flower.water(50)
# print(flower.status())
# flower.water(60)
# print(flower.status())
# flower.water(100)
# print(flower.status())

class SteamUser:
    def __init__(self, username: str, games: list[str]):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        else:
            return f"{game} is not in library"

    def buy_game(self, game):
        if game not in self.games:
            self.games.append(game)
            return f'{self.username} bought {game}'
        else:
            return f'{game} is already in your library'

    def status(self):
        return f'{self.username} has {len(self.games)} games. Total play time: {self.played_hours}'


#
#
# user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
# print(user.play("Fortnite", 3))
# print(user.play("Oxygen Not Included", 5))
# print(user.buy_game("CS:GO"))
# print(user.buy_game("Oxygen Not Included"))
# print(user.play("Oxygen Not Included", 6))
# print(user.status())

class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name: str, language: str, skills_earned: int):
        if language == self.language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):
        if skills_needed <= self.skills:
            if new_language not in self.language:
                result = f"{self.name} switched from {self.language} to {new_language}"
                self.language = new_language
            else:
                result = f"{self.name} already knows {self.language}"
        else:
            result = f"{self.name} needs {skills_needed - self.skills} more skills"

        return result


#
# programmer = Programmer("John", "Java", 50)
# print(programmer.watch_course("Python Masterclass", "Python", 84))
# print(programmer.change_language("Java", 30))
# print(programmer.change_language("Python", 100))
# print(programmer.watch_course("Java: zero to hero", "Java", 50))
# print(programmer.change_language("Python", 100))
# print(programmer.watch_course("Python Masterclass", "Python", 84))

class Vehicle:

    def __init__(self, mileage: int, max_speed: int = 150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets: list[str] = []


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y


#
#
# p = Point(2, 4)
# print(p)
# p.set_x(3)
# p.set_y(5)
# print(p)

class Circle:
    pi = 3.14

    def __init__(self, radius: int):
        self.radius = radius

    def set_radius(self, new_radius: int):
        self.radius = new_radius

    def get_circumference(self):
        return 2 * self.radius * self.pi

    def get_area(self):
        return self.radius ** 2 * self.pi


#
# circle = Circle(10)
# circle.set_radius(12)
# print(circle.get_area())
# print(circle.get_circumference())


class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, filling_amount: int):
        if filling_amount + self.content > self.capacity:
            return f"Cannot add {filling_amount} ml"

        self.content = filling_amount + self.content
        return f"Glass filled with {filling_amount} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{self.capacity - self.content} ml left"


# glass = Glass()
# print(glass.fill(100))
# print(glass.fill(200))
# print(glass.empty())
# print(glass.fill(200))
# print(glass.info())


class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps: list[str] = []
        self.is_on = False

    def install(self, app: str, app_memory: int):
        if self.memory >= app_memory:
            if self.is_on:
                self.apps.append(app)
                self.memory -= app_memory
                return f"Installing {app}"
            else:
                return f"Turn on your phone to install {app}"
        return f"Not enough memory to install {app}"

    def power(self):
        self.is_on = not self.is_on

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


#
# smartphone = Smartphone(100)
# print(smartphone.install("Facebook", 60))
# smartphone.power()
# print(smartphone.install("Facebook", 60))
# print(smartphone.install("Messenger", 20))
# print(smartphone.install("Instagram", 40))
# print(smartphone.status())

class Vet:
    animals: list[str] = []
    space = 5

    def __init__(self, doctor_name: str):
        self.name = doctor_name
        self.animals: list[str] = []

    def register_animal(self, animal_name: str) -> str:
        if Vet.space > 0:
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            Vet.space -= 1
            return f"{animal_name} registered in the clinic"
        return "Not enough space"

    def unregister_animal(self, animal_name: str) -> str:
        if animal_name in self.animals and animal_name in Vet.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            Vet.space += 1
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in the clinic"

    def info(self) -> str:
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"


# peter = Vet("Peter")
# george = Vet("George")
# print(peter.register_animal("Tom"))
# print(george.register_animal("Cory"))
# print(peter.register_animal("Fishy"))
# print(peter.register_animal("Bobby"))
# print(george.register_animal("Kay"))
# print(george.unregister_animal("Cory"))
# print(peter.register_animal("Silky"))
# print(peter.unregister_animal("Molly"))
# print(peter.unregister_animal("Tom"))
# print(peter.info())
# print(george.info())


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int):  # - updates the time with the new values
        if hours <= self.max_hours and minutes <= self.max_minutes and seconds <= self.max_seconds:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds

    def get_time(self) -> str:

        """ returns '{hh}:{mm}:{ss}' """
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def next_second(self):  # updates the time with one second (use the class attributes for validation)
        # and returns the new time (use the get_time() method)

        if self.seconds == self.max_seconds:
            self.seconds -= self.max_seconds
            if self.minutes == self.max_minutes:
                self.minutes -= self.max_minutes
                if self.hours == self.max_hours:
                    self.hours -= self.max_hours
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1
        return self.get_time()


#
# time3 = Time(9, 30, 59)
# print(time3.next_second())
# time2 = Time(10, 59, 59)
# print(time2.next_second())
# time1 = Time(23, 59, 59)
# print(time1.next_second())


class Account:
    def __init__(self, account_id: int, name: str, balance: int = 0):
        self.id = account_id
        self.name = name
        self.balance = balance

    def credit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount) -> int | str:
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"

    def info(self) -> str:
        return f"User {self.name} with account {self.id} has {self.balance} balance"


#
# account = Account(1234, "George", 1000)
# print(account.credit(500))
# print(account.debit(1500))
# print(account.info())
# account = Account(5411256, "Peter")
# print(account.debit(500))
# print(account.credit(1000))
# print(account.debit(500))
# print(account.info())

class PizzaDelivery:
    ordered = False

    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float) -> str | None:
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        self.ingredients[ingredient] = self.ingredients.get(ingredient, 0) + quantity
        self.price += quantity * price_per_quantity
        return None

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float) -> str | None:
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients.keys():
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        else:
            if self.ingredients[ingredient] < quantity:
                return f"Please check again the desired quantity of {ingredient}!"

            self.ingredients[ingredient] -= quantity
            self.price -= quantity * price_per_quantity
            return None

    def make_order(self):
        self.ordered = True
        string_ingredients = []
        for k, v in self.ingredients.items():
            string_ingredients.append(f"{k}: {v}")

        return  f"You've ordered pizza {self.name} prepared with {', '.join(string_ingredients)} and the price will be {self.price}lv."

# margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
# margarita.add_extra('mozzarella', 1, 0.5)
# margarita.add_extra('cheese', 1, 1)
# margarita.remove_ingredient('cheese', 1, 1)
# print(margarita.remove_ingredient('bacon', 1, 2.5))
# print(margarita.remove_ingredient('tomatoes', 2, 0.5))
# margarita.remove_ingredient('cheese', 2, 1)
# print(margarita.make_order())
# print(margarita.add_extra('cheese', 1, 1))


import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "0"

    def eat(self):
        print(f"{self.name} кушает")


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        return "чирик чик чик"


class Mammal(Animal):
    def __init__(self, name, age, has_fur):
        super().__init__(name, age)
        self.has_fur = has_fur

    def make_sound(self):
        return "вах вах"


class Reptile(Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color

    def make_sound(self):
        return "шшш шшш"


def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} говорит: {animal.make_sound()}")


class Zoo():
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)


class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"Зоотехник {self.name} кормит {animal.name}")


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"Ветеринар {self.name} лечит {animal.name}")

def save_zoo(zoo, filename="zoo_data.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        # Животные
        f.write("Животные:\n")
        for animal in zoo.animals:
            f.write(f"Имя: {animal.name}\n")
            f.write(f"Возраст: {animal.age}\n")
            f.write(f"Тип: {animal.__class__.__name__}\n")
            if isinstance(animal, Bird):
                f.write(f"Размах крыльев: {animal.wingspan}\n")
            elif isinstance(animal, Mammal):
                f.write(f"Шерсть: {str(animal.has_fur).lower()}\n")
            elif isinstance(animal, Reptile):
                f.write(f"Цвет чешуи: {animal.scale_color}\n")
            f.write("--------\n")  # Разделитель

        # Сотрудники
        f.write("\nСотрудники:\n")
        for employee in zoo.employees:
            f.write(f"Имя: {employee.name}\n")
            f.write(f"Должность: {employee.__class__.__name__}\n")
            f.write("--------\n")

def load_zoo(filename="zoo_data.txt"):
    zoo = Zoo()
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            mode = None  # "animal" или "employee"
            animal_data = {}
            employee_data = {}
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                if line == "Животные:":
                    mode = "animal"
                    continue
                elif line == "Сотрудники:":
                    mode = "employee"
                    continue
                elif line == "--------":
                    # Конец объекта
                    if mode == "animal":
                        name = animal_data["Имя"]
                        age = int(animal_data["Возраст"])
                        typ = animal_data["Тип"]
                        if typ == "Bird":
                            wingspan = float(animal_data["Размах крыльев"])
                            zoo.add_animal(Bird(name, age, wingspan))
                        elif typ == "Mammal":
                            has_fur = animal_data["Шерсть"].lower() == "true"
                            zoo.add_animal(Mammal(name, age, has_fur))
                        elif typ == "Reptile":
                            scale_color = animal_data["Цвет чешуи"]
                            zoo.add_animal(Reptile(name, age, scale_color))
                        animal_data = {}
                    elif mode == "employee":
                        name = employee_data["Имя"]
                        role = employee_data["Должность"]
                        if role == "ZooKeeper":
                            zoo.add_employee(ZooKeeper(name))
                        elif role == "Veterinarian":
                            zoo.add_employee(Veterinarian(name))
                        employee_data = {}
                    continue
                # Наполняем словарь данных
                key, value = line.split(": ", 1)
                if mode == "animal":
                    animal_data[key] = value
                elif mode == "employee":
                    employee_data[key] = value
        return zoo
    except FileNotFoundError:
        return Zoo()


if __name__ == "__main__":
    # Загрузка существующего зоопарка или создание нового
    my_zoo = load_zoo()

    # Пример добавления животных
    eagle1 = Bird("Орёл Карлуша", 5, 2.0)
    eagle2 = Bird("Орёл Персик", 1, 1.2)
    lion1 = Mammal("Лев Дурак", 10, True)
    lion2 = Mammal("Лев Силач", 8, True)
    snake1 = Reptile("Змея Зеленка", 3, "зелёный")
    my_zoo.add_animal(eagle1)
    my_zoo.add_animal(eagle2)
    my_zoo.add_animal(lion1)
    my_zoo.add_animal(lion2)
    my_zoo.add_animal(snake1)

    # Пример добавления сотрудников
    keeper = ZooKeeper("Иван")  # Добавлено имя
    vet = Veterinarian("Анна")

    my_zoo.add_employee(keeper)
    my_zoo.add_employee(vet)

    # Проверка полиморфизма
    animal_sound(my_zoo.animals)

    # Пример взаимодействия сотрудников с животными
    keeper.feed_animal(lion1)
    vet.heal_animal(snake1)

    # Сохранение состояния зоопарка
    save_zoo(my_zoo)

    new_zoo = load_zoo()
    print("Животных загружено:", len(new_zoo.animals))
    print("Сотрудников загружено:", len(new_zoo.employees))
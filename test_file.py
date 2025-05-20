print('new test')

class Warrior ():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power += 1

    def hit(self):
        print(f"{self.name} бьет кого-то")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} гуляет")

    def info(self):
        print(f"имя воина - {self.name}")
        print(f"цвет волос воина - {self.hair_color}")
        print(f"сила воина - {self.power}")
        print(f"выносливость воина - {self.endurance}")

war1 = Warrior(name="Игорь",power=35,endurance=50,hair_color="блонд")
print(war1.name)
print(war1.power)
print(war1.endurance)
print(war1.hair_color)
war2 = Warrior(name="Стас",power=70,endurance=27,hair_color="шатен")
war1.info()
war1.sleep()
war1.hit()
war1.eat()
war1.walk()
war1.info()
war2.eat()
print(war2.power)
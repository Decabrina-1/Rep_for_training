from abc import ABC, abstractmethod


class Weapon(ABC):
    def __init__(self):
        self.name = ""

    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def __init__(self):
        self.name = "меч"

    def attack(self):
        print("Боец наносит удар мечом.")


class Bow(Weapon):
    def __init__(self):
        self.name = "лук"

    def attack(self):
        print("Боец поражает стрелой из лука.")


class Fighter:
    def __init__(self):
        self.weapon = None

    def change_weapon(self, new_weapon=None):
        previous_weapon = self.weapon
        self.weapon = new_weapon
        if new_weapon is None:
            print("Боец оставляет оружие и становится безоружным.")
        else:
            if previous_weapon is None:
                print(f"Боец выбирает {new_weapon.name}.")
            else:
                print(f"Боец меняет оружие с {previous_weapon.name} на {new_weapon.name}.")

    def attack(self):
        if self.weapon:
            self.weapon.attack()
            print("Монстр побежден!")
        else:
            print("Боец не может атаковать без оружия!")


if __name__ == "__main__":
    fighter1 = Fighter()


    fighter1.attack()


    fighter1.change_weapon(Sword())
    fighter1.attack()


    fighter1.change_weapon(Bow())
    fighter1.attack()


    fighter1.change_weapon()
    fighter1.attack()


    fighter1.change_weapon(Sword())
    fighter1.attack()
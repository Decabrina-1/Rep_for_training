import random


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.attack_count = 0  # Счетчик количества атак

    def attack(self, other):
        # Сначала проверяем, нужно ли менять силу удара
        if self.attack_count > 0:
            self.attack_power = random.randint(10, 25)

        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

        self.attack_count += 1  # Увеличиваем счетчик после атаки

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name, health=100, attack_power=20)
        self.computer = Hero("Компьютер", health=100, attack_power=20)

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            print("\n" + "=" * 30)
            print(f"Ход игрока {self.player.name}:")
            self.player.attack(self.computer)
            print(f"Здоровье {self.computer.name}: {self.computer.health}")
            if not self.computer.is_alive():
                break

            # Ход компьютера
            print(f"\nХод компьютера:")
            self.computer.attack(self.player)
            print(f"Здоровье {self.player.name}: {self.player.health}")

        self.show_result()

    def show_result(self):
        # Определяем победителя
        winner = self.player if self.player.is_alive() else self.computer
        loser = self.computer if winner == self.player else self.player

        # Увеличиваем здоровье победителя на 5
        winner.health += 5

        # Считаем общее количество ударов
        total_attacks = self.player.attack_count + self.computer.attack_count

        print("\n" + "=" * 30)
        print(f"Победил {winner.name}! 💪")
        print(f"Игра завершена за {total_attacks} ударов.")
        print(f"Итоговое здоровье:")
        print(f"- {self.player.name}: {self.player.health}")
        print(f"- {self.computer.name}: {self.computer.health}")

        # Сброс счетчика атак для следующей игры
        self.player.attack_count = 0
        self.computer.attack_count = 0

    def play_again(self):
        while True:
            choice = input("Хотите сыграть еще? (да/нет): ").lower()
            if choice == "да":
                self.player.health = 100  # Восстанавливаем исходное здоровье
                self.computer.health = 100
                self.start()
            elif choice == "нет":
                print("Спасибо за игру!")
                break
            else:
                print("Введите 'да' или 'нет'.")


if __name__ == "__main__":
    player_name = input("Введите имя игрока: ")
    game = Game(player_name)
    game.start()
    game.play_again()
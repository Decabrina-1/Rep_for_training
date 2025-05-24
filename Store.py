class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        if item_name not in self.items:
            self.items[item_name] = price

    def remove_item(self, item_name):
        self.items.pop(item_name, None)

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price


# Создание магазинов
store1 = Store("Магазин 1", "ул. Пушкина 1")
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2 = Store("Магазин 2", "ул. Ленина 5")
store2.add_item("хлеб", 2.0)
store2.add_item("молоко", 1.5)

store3 = Store("Магазин 3", "пр. Кирова 10")
store3.add_item("сыр", 3.0)
store3.add_item("колбаса", 4.5)

# Тестирование методов на store1
print("Тестирование методов для Store 1:")
# Добавление товара
store1.add_item("апельсины", 1.0)
print(f"Цена апельсинов: {store1.get_item_price('апельсины')}")  # 1.0

# Обновление цены
store1.update_price("бананы", 0.8)
print(f"Новая цена бананов: {store1.get_item_price('бананы')}")  # 0.8

# Удаление товара
store1.remove_item("яблоки")
print(f"Цена яблок после удаления: {store1.get_item_price('яблоки')}")  # None

# Проверка цены существующего товара
print(f"Цена бананов после обновления: {store1.get_item_price('бананы')}")  # 0.8
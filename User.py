class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def __str__(self):
        return (f"User ID: {self.__id}, Name: {self.__name}, "
                f"Access Level: {self.__access_level}")


class Admin(User):
    __all_users = []

    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        Admin.__all_users.append(self)

    def add_user(self, user):
        if isinstance(user, User):
            Admin.__all_users.append(user)
        else:
            raise ValueError("Only User instances can be added")

    def remove_user(self, user_id):
        for user in Admin.__all_users:
            if user.get_id() == user_id:
                Admin.__all_users.remove(user)
                return
        raise ValueError("User not found")

    def list_users(self):
        print("Список пользователей:")
        for user in Admin.__all_users:
            print(f" • {user}")

# Создание администратора
admin = Admin(1, "Петр")
print(admin)  # User ID: 1, Name: Admin1, Access Level: admin

# Создание обычного пользователя
user1 = User(2, "Клава")
print(user1)  # User ID: 2, Name: User1, Access Level: user


# Создание обычного пользователя
user2 = User(3, "Степа")
print(user2)  # User ID: 2, Name: User1, Access Level: user

# Добавление пользователя через админа
admin.add_user(user1)

# Добавление пользователя через админа
admin.add_user(user2)

admin.list_users()

# Попытка удалить пользователя
admin.remove_user(3)  # Удаляет user

admin.list_users()

# Попытка удалить несуществующего пользователя
try:
    admin.remove_user(4)
except ValueError as e:
    print(e)  # User not found




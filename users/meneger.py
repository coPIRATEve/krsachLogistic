import hashlib
import json
import os

class Manager:
    def __init__(self, username=None):
        self.username = username
        self.users_file = "users.json"
        self.users = self.load_users()

    def load_users(self):
        """Загружает данные пользователей из файла."""
        if not os.path.exists(self.users_file):
            return []
        with open(self.users_file, "r") as file:
            return json.load(file)

    def save_users(self):
        """Сохраняет данные пользователей в файл."""
        with open(self.users_file, "w") as file:
            json.dump(self.users, file, indent=4)

    def hash_password(self, password):
        """Хэширует пароль с использованием SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self):
        """Авторизация менеджера."""
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        hashed_password = self.hash_password(password)

        for user in self.users:
            if user["login"] == login and user["password"] == hashed_password:
                if user["role"] == "manager":
                    print("Вход выполнен! Добро пожаловать, менеджер.")
                    self.username = login
                    return True
                else:
                    print("Ошибка: недостаточно прав.")
                    return False
        print("Неверный логин или пароль.")
        return False

    def manage_users(self):
        """Управление пользователями: добавление, удаление, просмотр."""
        while True:
            print("\n--- Управление пользователями ---")
            print("1. Добавить пользователя")
            print("2. Удалить пользователя")
            print("3. Показать всех пользователей")
            print("0. Назад")

            option = input("Введите номер пункта меню: ")

            if option == "1":
                self.add_user()
            elif option == "2":
                self.delete_user()
            elif option == "3":
                self.show_users()
            elif option == "0":
                break
            else:
                print("Ошибка: неверный ввод!")

    def add_user(self):
        """Добавление нового пользователя."""
        username = input("Введите имя нового пользователя: ")
        phone = input("Введите номер телефона нового пользователя: ")
        self.users.append({"username": username, "phone": phone})
        self.save_users()
        print(f"Пользователь {username} успешно добавлен.")

    def delete_user(self):
        """Удаление пользователя."""
        username = input("Введите имя пользователя для удаления: ")

        for user in self.users:
            if user["username"] == username:
                self.users.remove(user)
                self.save_users()
                print(f"Пользователь {username} успешно удален.")
                return

        print("Ошибка: пользователь с таким именем не найден.")

    def show_users(self):
        """Показать список всех пользователей."""
        if not self.users:
            print("Нет зарегистрированных пользователей.")
            return

        print("\nСписок пользователей:")
        for user in self.users:
            print(f"Имя: {user['username']}, Телефон: {user['phone']}")

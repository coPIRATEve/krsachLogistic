#admin.py
import hashlib
import json
import os

class Admin:
    def __init__(self, username=None):
        self.username = username
        self.users_file = "users.json"
        self.users = self.load_users()

    def load_users(self):
        if not os.path.exists(self.users_file):
            return []
        with open(self.users_file, "r") as file:
            return json.load(file)

    def save_users(self):
        with open(self.users_file, "w") as file:
            json.dump(self.users, file, indent=4)

    def create_first_admin(self):
        """Создание первого администратора, если файл пуст."""
        if not self.users:
            print("Создание первого администратора:")
            login = input("Введите логин администратора: ")
            password = input("Введите пароль: ")
            hashed_password = self.hash_password(password)
            self.users.append({"login": login, "password": hashed_password, "role": "admin"})
            self.save_users()
            print("Администратор создан успешно!")

    def hash_password(self, password):
        """Хэширует пароль с использованием SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self):
        """Авторизация администратора."""
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        hashed_password = self.hash_password(password)

        for user in self.users:
            if user["login"] == login and user["password"] == hashed_password:
                if user["role"] == "admin":
                    print("Вход выполнен! Добро пожаловать в систему.")
                    self.username = login
                    return True
                else:
                    print("Ошибка: недостаточно прав.")
                    return False
        print("Неверный логин или пароль.")
        return False

    def manage_users(self):
        """Управление пользователями: добавление, удаление."""
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
        username = input("Введите имя нового пользователя: ")
        if any(user["username"] == username for user in self.users):
            print("Ошибка: пользователь с таким именем уже существует.")
            return

        role = input("Введите роль (admin/user): ").lower()

        if role not in ["admin", "user"]:
            print("Ошибка: роль должна быть 'admin' или 'user'.")
            return

        self.users.append({"username": username})
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

        print("Ошибка: пользователь с таким логином не найден.")

    def show_users(self):
        """Показать список всех пользователей."""
        if not self.users:
            print("Нет зарегистрированных пользователей.")
            return

        print("\nСписок пользователей:")
        for user in self.users:
            print(f"Логин: {user['username']}, Роль: {user['phone']}")

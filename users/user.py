import json
import os

from utils import update_user_data


class User:
    def __init__(self, username, phone_number):
        self.username = username
        self.phone_number = phone_number
        self.users_file = "users.json"
        self.users = self.load_users()
        update_user_data(self.users_file, self.username, self.phone_number)

    def load_users(self):
        """Загружает данные о пользователях. Если файл не существует, возвращает пустой список."""
        if os.path.exists(self.users_file):
            with open(self.users_file, "r") as file:
                return json.load(file)
        return []

    def save_users(self):
        """Сохраняет текущего пользователя в файл, если его еще нет в списке пользователей."""
        if not any(user["username"] == self.username for user in self.users):
            self.users.append({"username": self.username, "phone": self.phone_number})
            with open(self.users_file, "w") as file:
                json.dump(self.users, file, indent=4)


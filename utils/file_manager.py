#file_manager.py
import json
import os

def load_json_data(file_path):
    """Загружает данные из JSON файла, если файл существует."""
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return []

def save_json_data(file_path, data):
    """Сохраняет данные в JSON файл."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def update_user_data(users_file, username, phone_number):
    # Загружаем данные о пользователях
    try:
        with open(users_file, "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []  # Если файл не существует, создаем пустой список

    # Проверяем, есть ли уже такой пользователь
    if not any(user.get("username") == username for user in users):
        users.append({"username": username, "phone": phone_number})

        # Сохраняем обновленные данные
        with open(users_file, "w") as file:
            json.dump(users, file, indent=4)

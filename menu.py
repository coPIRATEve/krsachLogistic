from users import Admin, User
from logistics import LogisticsSystem

def main_menu():
    logistics_system = LogisticsSystem()
    while True:
        try:
            print("\n--- Добро пожаловать в логистическую систему ---")
            print("1. Войти как Администратор")
            print("2. Войти как Пользователь")
            print("0. Выход")

            option = input("Введите номер пункта меню: ").strip()

            if option == "1":
                admin = Admin()
                if admin.login():
                    admin_menu(admin, logistics_system)
            elif option == "2":
                username = input("Введите ваше имя: ").strip()
                phone_number = input("Введите номер телефона: ").strip()
                user = User(username, phone_number)
                user_menu(user, logistics_system)
            elif option == "0":
                print("Выход из системы. До свидания!")
                break
            else:
                print("Ошибка: неверный ввод!")
        except Exception as e:
            print(f"Ошибка в главном меню: {e}")


def admin_menu(admin, logistics_system):
    while True:
        try:
            print("\n--- Меню администратора ---")
            print("1. Управление пользователями")
            print("2. Добавить маршрут")
            print("3. Добавить транспорт")
            print("0. Назад")

            option = input("Введите номер пункта меню: ").strip()

            if option == "1":
                admin.manage_users()
            elif option == "2":
                add_route(logistics_system)
            elif option == "3":
                add_vehicle(logistics_system)
            elif option == "0":
                break
            else:
                print("Ошибка: неверный ввод!")
        except Exception as e:
            print(f"Ошибка в меню администратора: {e}")


def add_route(logistics_system):
    try:
        start = input("Введите начальную точку маршрута: ").strip()
        end = input("Введите конечную точку маршрута: ").strip()
        distance = float(input("Введите расстояние (в км): ").strip())
        logistics_system.add_route(start, end, distance)
        print(f"Маршрут {start} -> {end} успешно добавлен.")
    except ValueError:
        print("Ошибка: расстояние должно быть числом!")


def add_vehicle(logistics_system):
    try:
        name = input("Введите название транспортного средства: ").strip()
        capacity = int(input("Введите грузоподъемность (в кг): ").strip())
        speed = float(input("Введите скорость (в км/ч): ").strip())
        logistics_system.add_vehicle(name, capacity, speed)
        print(f"Транспорт {name} успешно добавлен.")
    except ValueError:
        print("Ошибка: грузоподъемность и скорость должны быть числами!")


def user_menu(user, logistics_system):
    while True:
        try:
            print(f"\n--- Меню пользователя ({user.username}) ---")
            print("1. Просмотреть маршруты")
            print("2. Выбрать маршрут и транспорт")
            print("0. Назад")

            option = input("Введите номер пункта меню: ").strip()

            if option == "1":
                logistics_system.show_routes()
            elif option == "2":
                select_route(logistics_system)
            elif option == "0":
                break
            else:
                print("Ошибка: неверный ввод!")
        except Exception as e:
            print(f"Ошибка в меню пользователя: {e}")


def select_route(logistics_system):
    try:
        logistics_system.show_routes()
        index = int(input("Введите индекс маршрута: ").strip())
        logistics_system.select_optimal_route(index)
    except ValueError:
        print("Ошибка: индекс маршрута должен быть числом!")

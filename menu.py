from users import Admin, User
from logistics import LogisticsSystem

def main_menu():
    logistics_system = LogisticsSystem()
    while True:
        try:
            print("\n--- Добро пожаловать в логистическую систему ---")
            print("1. Войти как Администратор")
            print("2. Войти как Менеджер")
            print("3. Войти как Пользователь")
            print("0. Выход")

            option = input("Введите номер пункта меню: ").strip()
            if option == "1":
                admin = Admin()
                if admin.login():
                    admin_menu(admin)
            elif option == "2":
                meneger_menu(logistics_system)
            elif option == "3":
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


def meneger_menu(logistics_system):
    while True:
        try:
            print(f"\n--- Меню менеджера ---")
            print("1. Добавить маршрут")
            print("2. Добавить транспорт")
            print("0. Назад")

            option = input("Введите номер пункта меню: ").strip()

            if option == "1":
                add_route(logistics_system)
            elif option == "2":
                add_vehicle(logistics_system)
            elif option == "0":
                print("Возврат в главное меню.")
                break
            else:
                print("Ошибка: неверный ввод!")
        except Exception as e:
            print(f"Ошибка в меню менеджера: {e}")


def admin_menu(admin):
    while True:
        try:
            print("\n--- Меню администратора ---")
            print("1. Управление пользователями")
            print("0. Назад")

            option = input("Введите номер пункта меню: ").strip()

            if option == "1":
                admin.manage_users()
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


def user_menu(user, logistics_system):
    while True:
        try:
            print(f"\n--- Меню пользователя ({user.username}) ---")
            print("1. Просмотреть маршруты")
            print("2. Выбрать маршрут и транспорт (оптимальный)")
            print("3. Рассчитать время для всех маршрутов и транспортов")
            print("0. Назад")

            option = input("Введите номер пункта меню: ").strip()

            if option == "1":
                logistics_system.show_routes()
            elif option == "2":
                logistics_system.select_optimal_route()
            elif option == "3":
                results = logistics_system.find_optimal_route()
                if results:
                    print("\nВремя для всех маршрутов и транспортов:")
                    for idx, result in enumerate(results, start=1):
                        print(f"{idx}. Маршрут {result['route']} с транспортом {result['vehicle']} займет {result['time']:.2f} часов.")
            elif option == "0":
                break
            else:
                print("Ошибка: неверный ввод!")
        except Exception as e:
            print(f"Ошибка в меню пользователя: {e}")

def add_vehicle(logistics_system):
    try:
        name = input("Введите название транспортного средства: ").strip()
        capacity = int(input("Введите грузоподъемность (в кг): ").strip())
        speed = float(input("Введите скорость (в км/ч): ").strip())
        logistics_system.add_vehicle(name, capacity, speed)
        print(f"Транспорт {name} успешно добавлен.")
    except ValueError:
        print("Ошибка: грузоподъемность и скорость должны быть числами!")





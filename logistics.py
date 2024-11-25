import os
import json

class LogisticsSystem:
    def __init__(self):
        self.vehicles_file = "data/vehicles.json"
        self.routes_file = "data/routes.json"  # Путь к файлу с маршрутами
        self.vehicles = self.load_vehicles()
        self.routes = self.load_routes()

    def load_vehicles(self):
        """Загружает транспортные средства из файла vehicles.json."""
        if os.path.exists(self.vehicles_file):
            if os.path.getsize(self.vehicles_file) > 0:  # Проверяем, что файл не пуст
                with open(self.vehicles_file, "r", encoding="utf-8") as file:
                    return json.load(file)
            else:
                print("Файл transport.json пуст. Загружаем пустой список.")
                return []
        else:
            print("Файл transport.json не найден. Создается новый.")
            return []  # Возвращаем пустой список, если файл не найден

    def add_vehicle(self, name, capacity, speed):
        """Добавляет транспортное средство в список и сохраняет в файл."""
        new_vehicle = {"name": name, "capacity": capacity, "speed": speed}
        self.vehicles.append(new_vehicle)
        self.save_vehicles()  # Сохраняем транспортные средства после добавления

    def save_vehicles(self):
        """Сохраняет транспортные средства в файл vehicles.json."""
        if not os.path.exists("data"):
            os.makedirs("data")  # Создаем директорию data, если она не существует
        with open(self.vehicles_file, "w", encoding="utf-8") as file:
            json.dump(self.vehicles, file, indent=4, ensure_ascii=False)

    def load_routes(self):
        """Загружает маршруты из файла routes.json."""
        if os.path.exists(self.routes_file):
            with open(self.routes_file, "r", encoding="utf-8") as file:
                return json.load(file)
        else:
            print("Файл маршрутов не найден, создается новый.")
            return []  # Возвращаем пустой список, если файл не найден

    def save_routes(self):
        """Сохраняет маршруты в файл routes.json."""
        if not os.path.exists("data"):
            os.makedirs("data")  # Создаем директорию data, если она не существует
        with open(self.routes_file, "w", encoding="utf-8") as file:
            json.dump(self.routes, file, indent=4, ensure_ascii=False)

    def add_route(self, start, end, distance):
        """Добавляет маршрут с уникальным индексом и сохраняет его в файл."""
        route_index = len(self.routes) + 1  # Присваиваем индекс маршрута
        new_route = {"index": route_index, "start": start, "end": end, "distance": distance}
        self.routes.append(new_route)
        self.save_routes()  # Сохраняем маршруты после добавления
        print(f"Маршрут {start} -> {end} с индексом {route_index} успешно добавлен.")

    def show_routes(self):
        """Отображает все маршруты с их индексами."""
        if not self.routes:
            print("Нет доступных маршрутов!")
            return
        print("\nДоступные маршруты:")
        for route in self.routes:
            print(f"{route['index']}. {route['start']} -> {route['end']} ({route['distance']} км)")

    def select_optimal_route(self, index):
        """Позволяет пользователю выбрать маршрут по индексу."""
        route = next((route for route in self.routes if route["index"] == index), None)
        if route:
            print(f"\nВы выбрали маршрут: {route['start']} -> {route['end']} ({route['distance']} км).")
            best_vehicle = self.find_optimal_vehicle(route)
            if best_vehicle:
                print(
                    f"Используемое транспортное средство: {best_vehicle['name']} (грузоподъемность: {best_vehicle['capacity']} кг, скорость: {best_vehicle['speed']} км/ч).")
            else:
                print("Нет подходящего транспорта для выбранного маршрута.")
        else:
            print(f"Маршрут с индексом {index} не найден!")

    def find_optimal_vehicle(self, route):
        """Находит лучший транспорт для выбранного маршрута."""
        best_vehicle = None
        min_time = float("inf")
        for vehicle in self.vehicles:
            time = route["distance"] / vehicle["speed"]
            if time < min_time and vehicle["capacity"] >= route.get("weight", 0):  # Проверка на вес, если он есть
                min_time = time
                best_vehicle = vehicle
        return best_vehicle

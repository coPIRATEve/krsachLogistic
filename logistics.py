import os
import json

class LogisticsSystem:
    def __init__(self):
        self.vehicles_file = "data/vehicles.json"
        self.routes_file = "data/routes.json"
        self.create_data_directory()
        self.vehicles = self.load_data(self.vehicles_file, [])
        self.routes = self.load_data(self.routes_file, [])

    def create_data_directory(self):
        """Создает директорию data, если она не существует."""
        if not os.path.exists("data"):
            os.makedirs("data")

    def load_data(self, file_path, default):
        """Загружает данные из файла JSON или возвращает значение по умолчанию."""
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        print(f"Файл {file_path} не найден или пуст. Загружаются данные по умолчанию.")
        return default

    def save_data(self, data, file_path):
        """Сохраняет данные в файл JSON."""
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add_vehicle(self, name, capacity, speed):
        """Добавляет транспортное средство и сохраняет в файл."""
        new_vehicle = {"name": name, "capacity": capacity, "speed": speed}
        self.vehicles.append(new_vehicle)
        self.save_data(self.vehicles, self.vehicles_file)

    def add_route(self, start, end, distance):
        """Добавляет маршрут и сохраняет в файл."""
        route_index = len(self.routes) + 1
        new_route = {"index": route_index, "start": start, "end": end, "distance": distance}
        self.routes.append(new_route)
        self.save_data(self.routes, self.routes_file)
        print(f"Маршрут {start} -> {end} с индексом {route_index} успешно добавлен.")

    def show_routes(self):
        """Отображает все маршруты."""
        if not self.routes:
            print("Нет доступных маршрутов!")
            return
        print("\nДоступные маршруты:")
        for route in self.routes:
            print(f"{route['index']}. {route['start']} -> {route['end']} ({route['distance']} км)")

    def select_optimal_route(self, index):
        """Позволяет выбрать оптимальный маршрут по индексу."""
        route = next((route for route in self.routes if route["index"] == index), None)
        if route:
            print(f"\nВы выбрали маршрут: {route['start']} -> {route['end']} ({route['distance']} км).")
            best_vehicle = self.find_optimal_vehicle(route)
            if best_vehicle:
                print(f"Используемое транспортное средство: {best_vehicle['name']} (грузоподъемность: {best_vehicle['capacity']} кг, скорость: {best_vehicle['speed']} км/ч).")
            else:
                print("Нет подходящего транспорта для выбранного маршрута.")
        else:
            print(f"Маршрут с индексом {index} не найден!")

    def find_optimal_vehicle(self, route):
        best_vehicle = min(
            (vehicle for vehicle in self.vehicles if vehicle["capacity"] >= route.get("weight", 0)),
            key=lambda v: route["distance"] / v["speed"],
            default=None
        )
        return best_vehicle


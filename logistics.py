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

    def find_optimal_route(self):
        """Находит все возможные комбинации маршрутов и транспортных средств с расчетом времени."""
        if not self.routes or not self.vehicles:
            print("Нет доступных маршрутов или транспортных средств!")
            return []

        results = []
        for route in self.routes:
            for idx, vehicle in enumerate(self.vehicles, start=1):
                time = route["distance"] / vehicle["speed"]
                results.append({
                    "route_index": route["index"],
                    "vehicle_index": idx,
                    "route": f"{route['start']} -> {route['end']}",
                    "vehicle": vehicle["name"],
                    "time": time
                })
        return results

    def select_optimal_route(self):
        """Отображает результаты расчета времени маршрутов и позволяет выбрать лучший вариант."""
        results = self.find_optimal_route()
        if not results:
            return

        print("\nДоступные комбинации маршрутов и транспортных средств:")
        for idx, result in enumerate(results, start=1):
            print(f"{idx}. Маршрут {result['route']} с транспортом {result['vehicle']} займет {result['time']:.2f} часов.")

        try:
            choice = int(input("\nВведите номер выбранного варианта: ").strip())
            if 1 <= choice <= len(results):
                selected = results[choice - 1]
                print(f"\nВы выбрали маршрут {selected['route']} с транспортом {selected['vehicle']}.")
                print(f"Время в пути: {selected['time']:.2f} часов.")
            else:
                print("Ошибка: выбранный номер вне диапазона!")
        except ValueError:
            print("Ошибка: введите числовой номер варианта!")



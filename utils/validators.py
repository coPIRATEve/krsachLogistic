#validators.py
def is_positive_number(value):
    """Проверяет, является ли значение положительным числом."""
    try:
        float_value = float(value)
        if float_value > 0:
            return True
        return False
    except ValueError:
        return False

def validate_weight(weight):
    """Проверяет корректность ввода веса груза."""
    if not is_positive_number(weight):
        return "Вес груза должен быть положительным числом!"
    return None

def validate_distance(distance):
    """Проверяет корректность ввода расстояния."""
    if not is_positive_number(distance):
        return "Расстояние должно быть положительным числом!"
    return None

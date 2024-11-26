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

def validate_distance(distance):
    if not is_positive_number(distance):
        return "Расстояние должно быть положительным числом!"
    return None

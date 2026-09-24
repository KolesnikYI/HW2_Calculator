def sum(x: float, y: float) -> float:
    """Функция для сложения двух элементов."""
    return ...


def subtract(x: float, y: float) -> float:
    """Функция для вычитания `y` из `x`."""
    return ...


def multiply(x: float, y: float) -> float:
    """Функция для перемножения двух элементов."""
    return x * y


def divide(x: float, y: float) -> float:
    """Функция для деления `x` на `y`."""
    return ...


def main(input_string: str) -> float:
    """Функция оркестратор - выполняет калькуляцию."""
    first_number, action, second_number = input_string.split()
    x, y = float(first_number), float(second_number)
    if action == "+":
        result = sum(x, y)
    elif action == "-":
        result = subtract(x, y)
    elif action == "*":
        result = multiply(x, y)
    else:
        result = divide(x, y)
    return result


if __name__ == "__main__":
    print(main(input()))

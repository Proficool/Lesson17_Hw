# import pytest
# from app.app import add, subtract, multiply, divide


# def test_add():
#     """Тестирует функцию сложения."""
#     assert add(2, 3) == 5
#     assert add(-1, 1) == 0
#     assert add(0, 0) == 0


# def test_subtract():
#     """Тестирует функцию вычитания."""
#     assert subtract(10, 5) == 5
#     assert subtract(3, 7) == -4
#     assert subtract(0, 0) == 0 

# def test_multiply():
#     """Тестирует функцию умножения."""
#     assert multiply(2, 3) == 6
#     assert multiply(-1, 5) == -5
#     assert multiply(0, 100) == 0

# def test_divide():
#     """Тестирует функцию деления."""
#     assert divide(10, 2) == 5
#     assert divide(9, 3) == 3
#     with pytest.raises(ValueError):
#         divide(5, 0)

'''УЛУЧШИЛ, ИСПОЛЬЗОВАВ ПАПРАМЕТРИЗАЦИЮ'''

import pytest
import sys
sys.path.append("D:/TeachMeSkills/TeachMeSkills/TMS/Lesson17_Hw/app")
from app import add, subtract, multiply, divide

# Тестируем функцию сложения
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),  # Положительные числа
    (-1, 1, 0),  # Положительное и отрицательное число
    (0, 0, 0),  # Нули
    (-3, -2, -5),  # Два отрицательных числа
])
def test_add(a, b, expected):
    """Тест функции сложения с различными комбинациями чисел."""
    assert add(a, b) == expected

# Тестируем функцию вычитания
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),  # Положительные числа
    (3, 7, -4),  # Первое число меньше второго
    (0, 0, 0),  # Нули
    (-3, -7, 4),  # Отрицательные числа
])
def test_subtract(a, b, expected):
    """Тест функции вычитания с различными комбинациями чисел."""
    assert subtract(a, b) == expected

# Тестируем функцию умножения
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),  # Положительные числа
    (-1, 5, -5),  # Одно отрицательное число
    (0, 100, 0),  # Умножение на ноль
    (-3, -2, 6),  # Два отрицательных числа
])
def test_multiply(a, b, expected):
    """Тест функции умножения с различными комбинациями чисел."""
    assert multiply(a, b) == expected

# Тестируем функцию деления
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),  # Положительные числа
    (9, 3, 3),  # Деление нацело
    (-6, 2, -3),  # Отрицательное делимое
    (0, 5, 0),  # Ноль в числителе
])
def test_divide(a, b, expected):
    """Тест функции деления с различными комбинациями чисел."""
    assert divide(a, b) == expected

# Тестируем деление на ноль
@pytest.mark.parametrize("a, b", [
    (5, 0),  # Положительное число делится на 0
    (-5, 0),  # Отрицательное число делится на 0
])
def test_divide_by_zero(a, b):
    """Тест деления на ноль. Ожидается ValueError."""
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        divide(a, b)

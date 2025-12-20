'''
You are given a non-negative floating-point number celsius, rounded to two decimal places, which represents a temperature measured in degrees Celsius.

Your task is to convert this temperature into Kelvin and Fahrenheit scales and return the result as an array:
    - ans = [kelvin, fahrenheit]

The answer will be accepted if it is within 10⁻⁵ of the correct value.

Conversion formulas:
    - Kelvin = celsius + 273.15
    - Fahrenheit = celsius × 1.80 + 32.00

Return the array ans.

Examples:
Input: celsius = 36.50
Output: [309.65000, 97.70000]

Input: celsius = 122.11
Output: [395.26000, 251.79800]

Дано неотрицательное вещественное число celsius, округлённое до двух знаков после запятой, которое обозначает температуру в градусах Цельсия.

Необходимо перевести эту температуру в Кельвины и градусы Фаренгейта и вернуть результат в виде массива:
    - ans = [kelvin, fahrenheit]

Ответ считается корректным, если его погрешность не превышает 10⁻⁵.

Формулы перевода:
    - Кельвины = celsius + 273.15
    - Градусы Фаренгейта = celsius × 1.80 + 32.00

Верните массив ans.

Примеры:
Ввод: celsius = 36.50
Вывод: [309.65000, 97.70000]

Ввод: celsius = 122.11
Вывод: [395.26000, 251.79800]
'''

from typing import List

def convert_temperature(celsius: float) -> List[float]:
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00
    return [kelvin, fahrenheit]
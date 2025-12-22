'''
You are given four integers: length, width, height, and mass, which represent the dimensions and mass of a box.

Your task is to determine the category of the box and return it as a string.

The box is considered "Bulky" if at least one of the following conditions is true:
    - Any dimension of the box is greater than or equal to 10⁴, or
    - The volume of the box is greater than or equal to 10⁹.

The box is considered "Heavy" if:
    - Its mass is greater than or equal to 100.

Based on these conditions, classify the box as follows:
    - "Both" - if the box is both Bulky and Heavy;
    - "Bulky" - if the box is Bulky but not Heavy;
    - "Heavy" - if the box is Heavy but not Bulky;
    - "Neither" - if the box is neither Bulky nor Heavy.

Note that the volume of the box is calculated as:
    - volume = length × width × height

Examples:
Input: length = 1000, width = 35, height = 700, mass = 300
Output: "Heavy"

Input: length = 200, width = 50, height = 800, mass = 50
Output: "Neither"

Даны четыре целых числа: length, width, height и mass, которые обозначают размеры и массу коробки.

Необходимо определить категорию коробки и вернуть её в виде строки.

Коробка считается «Bulky», если выполняется хотя бы одно из условий:
    - Любое из измерений коробки больше или равно 10⁴, или
    - Объём коробки больше или равен 10⁹.

Коробка считается «Heavy» (тяжёлой), если:
    - Её масса больше или равна 100.

Категория коробки определяется следующим образом:
    - "Both" - коробка одновременно Bulky и Heavy;
    - "Bulky" - коробка Bulky, но не Heavy;
    - "Heavy" - коробка Heavy, но не Bulky;
    - "Neither" - коробка не является ни Bulky, ни Heavy.

Объём коробки вычисляется по формуле:
    - объём = length × width × height

Примеры:
Ввод: length = 1000, width = 35, height = 700, mass = 300
Вывод: "Heavy"

Ввод:  length = 200, width = 50, height = 800, mass = 50
Вывод: "Neither"
'''

def categorize_box(length: int, width: int, height: int, mass: int) -> str:
    is_bulky = (
        length >= 10**4 or
        width >= 10**4 or
        height >= 10**4 or
        length * width * height >= 10**9
    )

    is_heavy = mass >= 100

    if is_bulky and is_heavy:
        return "Both"
    if is_bulky:
        return "Bulky"
    if is_heavy:
        return "Heavy"
    return "Neither"
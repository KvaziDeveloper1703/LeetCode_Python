'''
There are n rings, and each ring is colored red (R), green (G), or blue (B). The rings are placed on ten rods, labeled from 0 to 9.

You are given a string rings of length 2n describing how the rings are distributed.

Each pair of characters represents one ring:
    - The first character of the pair is the ring’s color;
    - The second character is the rod number where the ring is placed.

Your task is to return the number of rods that have at least one ring of each color - red, green, and blue.

Examples:
Input: rings = "B0B6G0R6R0R6G9"
Output: 1

Input: rings = "B0R0G0R9R0B0G0"
Output: 1

Есть n колец, и каждое кольцо имеет цвет красный (R), зелёный (G) или синий (B). Кольца размещены на десяти стержнях, пронумерованных от 0 до 9.

Вам дана строка rings длины 2n, описывающая расположение колец.

Каждые два символа представляют одно кольцо:
    - Первый символ пары — это цвет кольца;
    - Второй символ — это номер стержня, на котором размещено кольцо.

Нужно вернуть количество стержней, на которых есть кольца всех трёх цветов: красные, зелёные и синие.

Примеры:
Ввод: rings = "B0B6G0R6R0R6G9"
Вывод: 1

Ввод: rings = "B0R0G0R9R0B0G0"
Вывод: 1
'''

def count_points(rings: str) -> int:
    rods = {str(i): set() for i in range(10)}

    for i in range(0, len(rings), 2):
        color = rings[i]
        rod = rings[i + 1]
        rods[rod].add(color)

    count = 0
    for rod in rods.values():
        if len(rod) == 3:
            count += 1

    return count
'''
Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n.
Two 1s are considered adjacent if there are only 0s between them.
The distance between them is the absolute difference in their bit positions.

If there are no two adjacent 1's, return 0.

Examples:
Input: n = 22
Output: 2

Input: n = 8
Output: 0

Дано положительное целое число n. Найдите и верните максимальное расстояние между любыми двумя соседними единицами (1) в двоичном представлении числа n.
Соседними считаются такие две единицы, между которыми находятся только нули.
Расстояние между ними — это разность их позиций в битовой записи.

Если в двоичном представлении n нет двух единиц, верните 0.

Примеры:
Ввод: n = 22
Вывод: 2

Ввод: n = 8
Вывод: 0
'''

def binary_gap(n: int) -> int:
    binary = bin(n)[2:]
    previous = -1
    max_distance = 0

    for i, bit in enumerate(binary):
        if bit == '1':
            if previous != -1:
                max_distance = max(max_distance, i - previous)
            previous = i

    return max_distance
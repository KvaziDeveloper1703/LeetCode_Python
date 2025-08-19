'''
Given two integers n and start.

Create an array numbers of length n, where: numbers[i]=start+2⋅i for 0≤i<n

Return the result of the bitwise XOR of all elements in the array numbers.

Examples:
Input: n = 5, start = 0
Output: 8

Input: n = 4, start = 3
Output: 8

Даны два целых числа n и start.

Создайте массив numbers длины n, где: numbers[i]=start+2⋅i при 0≤i<n

Верните результат побитового XOR всех элементов массива numbers.

Примеры:
Ввод: n = 5, start = 0
Вывод: 8

Ввод: n = 4, start = 3
Вывод: 8
'''

def xor_operation(n: int, start: int) -> int:
    result = 0
    for i in range(n):
        result ^= start + 2 * i
    return result
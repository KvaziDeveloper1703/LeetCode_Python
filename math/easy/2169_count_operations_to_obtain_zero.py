'''
You are given two non-negative integers numbers_1 and numbers_2.

In one operation:
    - If numbers_1 ≥ numbers_2, subtract numbers_2 from numbers_1;
    - Otherwise, subtract numbers_1 from numbers_2.

Your task is to determine how many such operations are needed until either numbers_1 = 0 or numbers_2 = 0.

Examples:
Input: numbers_1 = 2, numbers_2 = 3
Output: 3

Input: numbers_1 = 10, numbers_2 = 10
Output: 1

Вам даны два неотрицательных целых числа numbers_1 и numbers_2.

За одну операцию:
    - Если numbers_1 ≥ numbers_2, вычитается numbers_2 из numbers_1;
    - Иначе вычитается numbers_1 из numbers_2.

Ваша задача - определить, сколько таких операций потребуется, пока numbers_1 = 0 или numbers_2 = 0.

Примеры:
Ввод: numbers_1 = 2, numbers_2 = 3
Вывод: 3

Ввод: numbers_1 = 10, numbers_2 = 10
Вывод: 1
'''

def count_operations(numbers_1: int, numbers_2: int) -> int:
    number_of_operations = 0
    while numbers_1 != 0 and numbers_2 != 0:
        if numbers_1 >= numbers_2:
            numbers_1 -= numbers_2
        else:
            numbers_2 -= numbers_1
        number_of_operations += 1
    return number_of_operations
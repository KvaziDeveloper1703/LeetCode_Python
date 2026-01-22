'''
You are given two positive integers n and k.

You are allowed to perform the following operation on n: Choose any bit in the binary representation of n that is equal to 1, and change it to 0.

Return the minimum number of such changes needed to make n equal to k. If it is impossible, return -1.

Examples:
Input: n = 13, k = 4
Output: 2

Input: n = 21, k = 21
Output: 0

Даны два положительных целых числа n и k.

Разрешается выполнять над числом n следующую операцию: Выбрать любой бит в двоичном представлении n, который равен 1, и заменить его на 0.

Нужно вернуть минимальное количество таких изменений, чтобы получить n = k. Если сделать это невозможно, вернуть -1.

Примеры:
Ввод: n = 13, k = 4
Вывод: 2

Ввод: n = 21, k = 21
Вывод: 0
'''

def min_сhanges(number: int, target: int) -> int:
    if (target & ~number) != 0:
        return -1
    return (number & ~target).bit_count()
'''
You are given a positive integer n.

Return the smallest positive integer that is a multiple of both n and 2.

Examples:
Input: n = 5
Output: 10

Input: n = 6
Output: 6

Вам дано положительное целое число n.

Необходимо найти и вернуть наименьшее положительное целое число, которое является кратным одновременно числам n и 2.

Примеры:
Ввод: n = 5
Вывод: 10

Ввод: n = 6
Вывод: 6
'''

def smallest_even_multiple(n: int) -> int:
    if n % 2 == 0:
        return n
    return n * 2
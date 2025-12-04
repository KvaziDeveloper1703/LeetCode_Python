'''
You are given a positive integer number.

Return how many positive integers less than or equal to number have an even digit sum.

The digit sum of a number is the sum of all its digits.

Examples:
Input: number = 4
Output: 2

Input: number = 30
Output: 14

Дано положительное целое число number.

Нужно вернуть количество положительных чисел, которые не превышают number и имеют чётную сумму цифр.

Сумма цифр числа - это сумма всех его цифр.

Примеры:
Ввод: number = 4
Вывод: 2

Ввод: number = 30
Вывод: 14
'''

def count_even(numbers: int) -> int:
    def digit_sum(x):
        s = 0
        while x > 0:
            s += x % 10
            x //= 10
        return s

    count = 0
    for i in range(1, numbers + 1):
        if digit_sum(i) % 2 == 0:
            count += 1
    return count
'''
You are given two positive integers n and m.

Define two integers as follows:
    - num1: the sum of all integers in the range [1, n] (inclusive) that are not divisible by m;
    - num2: the sum of all integers in the range [1, n] (inclusive) that are divisible by m.

Return the value of: num1 - num2.

Examples:
Input: n = 10, m = 3
Output: 19

Input: n = 5, m = 6
Output: 15

Вам даны два положительных целых числа n и m.

Определим два числа следующим образом:
    - num1 - сумма всех целых чисел на отрезке [1, n] (включительно), которые не делятся на m;
    - num2 - сумма всех целых чисел на отрезке [1, n] (включительно), которые делятся на m.

Верните значение: num1 - num2.

Примеры:
Ввод: n = 10, m = 3
Вывод: 19

Ввод: n = 5, m = 6
Вывод: 15
'''

def difference_of_sums(n: int, m: int) -> int:
    total_sum = n * (n + 1) // 2
    count_divisible = n // m
    divisible_sum = m * count_divisible * (count_divisible + 1) // 2

    return total_sum - 2 * divisible_sum
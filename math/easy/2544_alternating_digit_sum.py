'''
You are given a positive integer n.

Each digit of n is assigned a sign according to the following rules:
    - The most significant digit has a positive sign;
    - Every subsequent digit has the opposite sign of the digit immediately to its left.

Your task is to return the sum of all digits with their assigned signs.

Examples:
Input: n = 521
Output: 4

Input: n = 111
Output: 1

Дано положительное целое число n.

Каждой цифре числа n присваивается знак по следующим правилам:
    - Старшая цифра имеет положительный знак;
    - Каждая следующая цифра получает противоположный знак по отношению к соседней слева.

Необходимо вернуть сумму всех цифр с учётом назначенных знаков.

Примеры:
Ввод: n = 521
Вывод: 4

Ввод: n = 111
Вывод: 1
'''

def alternate_digit_sum(n: int) -> int:
    digits = str(n)
    total_sum = 0
    sign = 1

    for digit in digits:
        total_sum += sign * int(digit)
        sign *= -1

    return total_sum
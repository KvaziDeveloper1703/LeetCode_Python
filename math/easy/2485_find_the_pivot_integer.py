'''
Given a positive integer n, find an integer x (called the pivot integer) such that:
    - The sum of all integers from 1 to x (inclusive) is equal to
    - The sum of all integers from x to n (inclusive).

Return the pivot integer x. If no such integer exists, return -1.

It is guaranteed that for a given input there is at most one pivot integer.

Examples:
Input: n = 8
Output: 6

Input: n = 1
Output: 1

Дано положительное целое число n.

Необходимо найти целое число x (называемое опорным числом), такое что:
    - сумма всех целых чисел от 1 до x (включительно) равна
    - сумме всех целых чисел от x до n (включительно).

Верните опорное число x. Если такого числа не существует, верните -1.

Гарантируется, что для каждого входного значения существует не более одного опорного числа.

Примеры:
Ввод: n = 8
Вывод: 6

Ввод: n = 1
Вывод: 1
'''

def pivot_integer(n: int) -> int:
    total = n * (n + 1) // 2

    x = int(total ** 0.5)
    if x * x == total:
        return x
    return -1
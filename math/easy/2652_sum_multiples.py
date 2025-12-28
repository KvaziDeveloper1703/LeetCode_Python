'''
Given a positive integer n, find the sum of all integers in the range [1, n] that are divisible by 3, 5, or 7.

Return an integer representing the sum of all numbers in the given range that satisfy this condition.

Examples:
Input: n = 7
Output: 21

Input: n = 10
Output: 40

Дано положительное целое число n. Необходимо найти сумму всех целых чисел в диапазоне от 1 до n включительно, которые делятся на 3, 5 или 7.

Верните целое число - сумму всех чисел в указанном диапазоне, удовлетворяющих условию.

Примеры:
Ввод: n = 7
Вывод: 21

Ввод: n = 10
Вывод: 40
'''

def sum_of_multiples(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            total += i
    return total
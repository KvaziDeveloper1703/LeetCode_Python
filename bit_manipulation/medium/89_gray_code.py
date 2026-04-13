'''
An n-bit Gray code sequence is a sequence of 2**n integers where:
    + Every integer is in the inclusive range [0, 2**n-1],
    + The first integer is 0,
    + No integer appears more than once in the sequence,
    + The binary representation of every pair of adjacent integers differs by exactly one bit, and
    + The binary representation of the first and last integers also differs by exactly one bit.

Given an integer n, return any valid n-bit Gray code sequence.

Example:
Input: n = 2
Output: [0, 1, 3, 2]

N-битная последовательность Грея — это последовательность из 2**n целых чисел, которая удовлетворяет следующим условиям:
    + Каждое число находится в диапазоне [0, 2**n-1],
    + Первое число в последовательности — 0,
    + Ни одно число не повторяется в последовательности,
    + Двоичное представление каждой пары соседних чисел отличается ровно на один бит,
    + Двоичное представление первого и последнего чисел также отличается ровно на один бит.

Дано целое число n. Верните любую допустимую n-битную последовательность Грея.

Пример:
Ввод: n = 2
Вывод: [0, 1, 3, 2]
'''

def gray_code(n: int):
    result = []
    for i in range(2 ** n):
        gray = i ^ (i // 2)
        result.append(gray)
    return result
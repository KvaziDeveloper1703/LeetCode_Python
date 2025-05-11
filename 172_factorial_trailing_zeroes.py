'''
Given an integer n, return the number of trailing zeroes in the factorial of n.
A trailing zero is a 0 at the end of the number. These are created by factors of 10, which come from multiplying 2 × 5. 
Since there are usually more 2s than 5s in the factorization of n!, the number of trailing zeros is determined by the number of times 5 appears as a factor in the numbers from 1 to n.

Example:
Input: n = 3
Output: 0

Дано целое число n. Верните количество нулей на конце факториала числа n.
Концевые нули в факториале появляются из множителей 10, а 10 = 2 × 5. 
Поскольку множителей 2 всегда больше, чем 5, нужно просто посчитать, сколько раз 5 встречается в разложении чисел от 1 до n.

Пример:
Ввод: n = 3
Вывод: 0
'''

def trailing_zeroes(N: int) -> int:
    count = 0
    while N >= 5:
        N //= 5
        count += N
    return count
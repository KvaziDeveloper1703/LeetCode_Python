'''
The Fibonacci numbers, commonly denoted as F(n), form a sequence called the Fibonacci sequence. Each number is the sum of the two preceding ones, starting from 0 and 1. 
Formally:
    + F(0) = 0;
    + F(1) = 1;
    + F(n) = F(n - 1) + F(n - 2), for n > 1.

Given an integer n, calculate and return F(n).

Examples:
Input: n = 2
Output: 1

Input: n = 3
Output: 2

Числа Фибоначчи, обычно обозначаемые как F(n), образуют последовательность, называемую последовательностью Фибоначчи. Каждое число является суммой двух предыдущих, начиная с 0 и 1. 
Формально:
    + F(0) = 0;
    + F(1) = 1;
    + F(n) = F(n - 1) + F(n - 2), для n > 1.

Дан целочисленный параметр n. Вычислите и верните значение F(n).

Примеры:
Ввод: n = 2
Вывод: 1

Ввод: n = 3
Вывод: 2
'''

memo = {}

def fibonacci(number: int) -> int:
    if number in memo:
        return memo[number]
    if number == 0:
        result = 0
    elif number == 1:
        result = 1
    else:
        result = fibonacci(number - 1) + fibonacci(number - 2)
    
    memo[number] = result
    
    return result
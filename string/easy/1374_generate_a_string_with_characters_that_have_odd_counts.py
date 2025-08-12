'''
Given an integer n. Return a string of length n such that each character in the string appears an odd number of times.
The string must contain only lowercase English letters. If there are multiple valid strings, you may return any of them.

Examples:
Input:  n = 4
Output: "pppz"

Input:  n = 2
Output: "xy"

Вам дано целое число n. Верните строку длины n, в которой каждый символ встречается нечётное количество раз.
Строка должна содержать только строчные буквы английского алфавита. Если существует несколько подходящих строк, можно вернуть любую из них.

Примеры:
Ввод:  n = 4
Вывод: "pppz"

Ввод:  n = 2
Вывод: "xy"
'''

def generate_the_string(n: int) -> str:
    if n % 2 == 1:
        return "a" * n
    else:
        return "a" * (n - 1) + "b"
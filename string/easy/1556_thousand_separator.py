'''
Given an integer n. Add a dot (".") as the thousands separator and return the result as a string.

Examples:
Input: n = 987
Output: "987"

Input: n = 1234
Output: "1.234"

Дано целое число n. Необходимо вставить точку (".") в качестве разделителя тысяч и вернуть результат в виде строки.

Примеры:
Ввод: n = 987
Вывод: "987"

Ввод: n = 1234
Вывод: "1.234"
'''

def thousand_separator(n: int) -> str:
    return f"{n:,}".replace(",", ".")
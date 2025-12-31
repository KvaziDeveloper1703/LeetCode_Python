'''
You are given a string s. You can perform the following operations any number of times:
    - Choose an index i in the string and let c = s[i]. Delete the closest occurrence of character c to the left of index i, if such a character exists.
    - Choose an index i in the string and let c = s[i]. Delete the closest occurrence of character c to the right of index i, if such a character exists.

Your goal is to minimize the length of the string after performing zero or more operations.

Return an integer representing the minimum possible length of the string.

Examples:
Input: s = "aaabc"
Output: 3

Input: s = "cbbd"
Output: 3

Дана строка s. Вы можете выполнять следующие операции любое количество раз:
    - Выберите индекс i в строке и пусть c = s[i]. Удалите ближайшее вхождение символа c слева от позиции i, если оно существует.
    - Выберите индекс i в строке и пусть c = s[i]. Удалите ближайшее вхождение символа c справа от позиции i, если оно существует.

Ваша задача - минимизировать длину строки, выполнив ноль или более операций.

Верните число - минимально возможную длину строки.

Примеры:
Ввод: s = "aaabc"
Вывод: 3

Ввод: s = "cbbd"
Вывод: 3
'''

def minimized_string_length(s: str) -> int:
    return len(set(s))
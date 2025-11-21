'''
You are given a 0-indexed string s where all characters at even indices are lowercase English letters, and all characters at odd indices are digits.

You need to apply an operation shift(c, x), where c is a character and x is a digit. shift(c, x) returns the character that is x positions after c in the alphabet.

For example:
    - shift('a', 5) = 'f'
    - shift('x', 0) = 'x'

For every odd index i, replace the digit s[i] with shift(s[i-1], s[i]).

Return the final string after all digits have been replaced. It is guaranteed that shift(s[i-1], s[i]) will never go past 'z'.

Examples:
Input: s = "a1c1e1"
Output: "abcdef"

Input: s = "a1b2c3d4e"
Output: "abbdcfdhe"

Дана строка s с индексацией с 0. На чётных позициях строки находятся строчные буквы английского алфавита, а на нечётных — цифры.

Нужно выполнить операцию shift(c, x), где c - символ, а x - цифра. Операция shift(c, x) возвращает символ, который стоит на x позиций позже, чем c в алфавите.

Например:
    - shift('a', 5) = 'f'
    - shift('x', 0) = 'x'

Для каждого нечётного индекса i нужно заменить цифру s[i] на результат shift(s[i−1], s[i]).

Верните строку после замены всех цифр. Гарантируется, что shift(s[i−1], s[i]) никогда не выйдет за предел 'z'.

Примеры:
Ввод: s = "a1c1e1"
Вывод: "abcdef"

Ввод: s = "a1b2c3d4e"
Вывод: "abbdcfdhe"
'''

def replace_digits(s: str) -> str:
    result = []

    for index in range(len(s)):
        if index % 2 == 0:
            result.append(s[index])
        else:
            previous_character = s[index - 1]
            shift_value = int(s[index])
            new_character = chr(ord(previous_character) + shift_value)
            result.append(new_character)

    return "".join(result)
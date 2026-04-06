'''
A valid number can be:
    - An integer with an optional sign (+ or -);
    - A decimal number with an optional sign;
    - Either of the above followed by an optional exponent part.

A string s is considered a valid number if it follows one of these forms. The number may start with an optional sign (+ or -).
An integer consists of one or more digits.
A decimal number can be written as digits followed by a dot, digits followed by a dot and digits, or a dot followed by digits.
The exponent part, if present, is represented by 'e' or 'E' and must be followed by a valid integer, which may also include an optional sign.
The string must contain at least one digit, and all digits must be in the range from 0 to 9.

Examples:
Input: s = "0"
Output: true

Input: s = "e"
Output: false

Корректное число может быть:
    - Целым числом с необязательным знаком (+ или -);
    - Десятичным числом с необязательным знаком;
    - Любым из этих вариантов с необязательной экспонентой.

Строка s считается корректным числом, если она соответствует одной из этих форм. Число может начинаться с необязательного знака (+ или -).
Целое число состоит из одной или более цифр.
Десятичное число может быть записано как цифры с точкой, цифры с точкой и последующими цифрами или точка с последующими цифрами.
Экспонента, если она присутствует, задаётся символом 'e' или 'E' и должна сопровождаться корректным целым числом с возможным знаком.
В строке должна присутствовать хотя бы одна цифра, и все цифры должны быть в диапазоне от 0 до 9.

Примеры:
Ввод: s = "0"
Вывод: true

Ввод: s = "e"
Вывод: false
'''

def is_number(s: str) -> bool:
    s = s.strip()

    has_digit = False
    has_dot = False
    has_exp = False

    for i, ch in enumerate(s):
        if ch.isdigit():
            has_digit = True
        elif ch in ['+', '-']:
            if i > 0 and s[i - 1] not in ['e', 'E']:
                return False
        elif ch == '.':
            if has_dot or has_exp:
                return False
            has_dot = True
        elif ch in ['e', 'E']:
            if has_exp or not has_digit:
                return False
            has_exp = True
            has_digit = False
        else:
            return False

    return has_digit
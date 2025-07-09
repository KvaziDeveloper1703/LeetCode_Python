'''
Given two integers representing the numerator and denominator of a fraction. Return the fraction as a string.
    + If the fractional part is repeating, enclose the repeating part in parentheses;
    + If there are multiple correct answers, any one is acceptable;
    + It is guaranteed that the length of the output string will be less than 10,000 for all inputs.

Examples:
Input: numerator = 1, denominator = 2
Output: "0.5"

Input: numerator = 2, denominator = 1
Output: "2"

Даны два целых числа — числитель и знаменатель дроби. Верните результат деления в виде строки.
    + Если дробная часть повторяется, заключите повторяющуюся часть в скобки;
    + Если возможно несколько правильных ответов — можно вернуть любой из них;
    + Гарантируется, что длина строки-ответа не превышает 10 000 символов.

Примеры:
Ввод: numerator = 1, denominator = 2
Вывод: "0.5"

Ввод: numerator = 2, denominator = 1
Вывод: "2"
'''

def fraction_to_decimal(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return "0"

    result = []

    if (numerator < 0) ^ (denominator < 0):
        result.append("-")

    numerator = abs(numerator)
    denominator = abs(denominator)
    integer_part = numerator // denominator
    result.append(str(integer_part))
    remainder = numerator % denominator

    if remainder == 0:
        return "".join(result)

    result.append(".")
    remainder_map = {}

    while remainder != 0:
        if remainder in remainder_map:
            insert_index = remainder_map[remainder]
            result.insert(insert_index, "(")
            result.append(")")
            break

        remainder_map[remainder] = len(result)
        remainder *= 10
        result.append(str(remainder // denominator))
        remainder %= denominator

    return "".join(result)
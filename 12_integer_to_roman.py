'''
Roman numerals use the symbols I, V, X, L, C, D, and M to represent numbers. To convert an integer to a Roman numeral, follow these rules:
+ Symbols are added from largest to smallest values;
+ For numbers like 4, 9, 40, 90, 400, and 900, use the subtractive form (e.g., 4 = IV, 900 = CM);
+ You can repeat symbols like I, X, C, and M up to 3 times, but never repeat V, L, or D;
+ Always convert each digit starting from the highest place value (thousands, hundreds, tens, units).

Given an integer number, convert it to its Roman numeral representation.

Examples:
Input: num = 3749
Output: "MMMDCCXLIX"

Input: num = 58
Output: "LVIII"

Input: num = 1994
Output: "MCMXCIV"

Римские цифры используют символы I, V, X, L, C, D и M для обозначения чисел. Чтобы преобразовать целое число в римское, следуйте этим правилам:
+ Символы записываются от большего к меньшему значению;
+ Для чисел вроде 4, 9, 40, 90, 400 и 900 используется вычитание (например, 4 = IV, 900 = CM);
+ Символы I, X, C и M можно повторять не более трёх раз подряд, а V, L и D — никогда не повторяются;
+ Преобразование начинается с наибольшего разряда числа (тысячи, сотни, десятки, единицы).

Дано целое число — преобразуйте его в римскую запись.

Примеры:
Ввод: num = 3749
Вывод: "MMMDCCXLIX"

Ввод: num = 58
Вывод: "LVIII"

Ввод: num = 1994
Вывод: "MCMXCIV"
'''

def integer_to_roman(number: int) -> str:
    value_to_symbol = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
        ]

    result = []
    for value, symbol in value_to_symbol:
        while number >= value:
            result.append(symbol)
            number -= value

    return ''.join(result)
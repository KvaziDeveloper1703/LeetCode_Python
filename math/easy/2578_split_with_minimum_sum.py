'''
You are given a positive integer number. Split it into two non-negative integers number1 and number2 such that:
    - The concatenation of number1 and number2 is a permutation of number. In other words, for each digit, the total number of occurrences of that digit in number1 and number2 is equal to the number of occurrences of that digit in number;
    - Both number1 and number2 may contain leading zeros.

Return the minimum possible sum of number1 and number2.

Notes:
    - It is guaranteed that number does not contain leading zeros;
    - The order of digits in number1 and number2 may differ from the order of digits in number.

Examples:
Input: number = 4325
Output: 59

Input: number = 687
Output: 75

Дано положительное целое число number. Разделите его на два неотрицательных целых числа number1 и number2 так, чтобы:
    - Конкатенация чисел number1 и number2 являлась перестановкой цифр числа number. Иными словами, суммарное количество вхождений каждой цифры в number1 и number2 должно совпадать с количеством её вхождений в number;
    - Числа number1 и number2 могут содержать ведущие нули.

Верните минимально возможную сумму чисел number1 и number2.

Примечания:
    - Гарантируется, что число number не содержит ведущих нулей;
    - Порядок цифр в number1 и number2 может отличаться от порядка цифр в number.

Примеры:
Ввод: number = 4325
Вывод: 59

Ввод: number = 687
Вывод: 75
'''

def split_number(number: int) -> int:
    digits = sorted(str(number))

    number1 = []
    number2 = []

    for i, digit in enumerate(digits):
        if i % 2 == 0:
            number1.append(digit)
        else:
            number2.append(digit)

    return int("".join(number1)) + int("".join(number2))
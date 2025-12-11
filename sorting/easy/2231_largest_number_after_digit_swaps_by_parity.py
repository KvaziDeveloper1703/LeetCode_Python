'''
You are given a positive integer number.

You are allowed to swap any two digits of number as long as they have the same parity.

You may perform any number of swaps.

Return the largest possible value of number that can be obtained after these swaps.

Examples:
Input: number = 1234
Output: 3412

Input: number = 65875
Output: 87655

Дано положительное целое число number.

Можно менять местами любые две цифры числа number, если их чётность совпадает.

Количество перестановок не ограничено.

Нужно вернуть наибольшее возможное значение, которое можно получить из числа number после таких обменов.

Примеры:
Ввод: number = 1234
Вывод: 3412

Ввод: number = 65875
Вывод: 87655
'''

def largest_integer(number: int) -> int:
    digits = list(map(int, str(number)))

    even_digits = sorted([digit for digit in digits if digit % 2 == 0], reverse=True)
    odd_digits = sorted([digit for digit in digits if digit % 2 == 1], reverse=True)

    even_index = 0
    odd_index = 0

    result_digits = []

    for digit in digits:
        if digit % 2 == 0:
            result_digits.append(even_digits[even_index])
            even_index += 1
        else:
            result_digits.append(odd_digits[odd_index])
            odd_index += 1

    return int("".join(map(str, result_digits)))
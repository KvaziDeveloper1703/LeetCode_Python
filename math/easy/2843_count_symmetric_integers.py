'''
You are given two positive integers low and high.

An integer x is called symmetric if:
    - x consists of an even number of digits (2 × n digits),
    - the sum of the first n digits is equal to the sum of the last n digits.

Numbers with an odd number of digits are never symmetric.

Your task is to return the number of symmetric integers in the inclusive range [low, high].

Examples:
Input: low = 1, high = 100
Output: 9

Input: low = 1200, high = 1230
Output: 4

Вам даны два положительных целых числа low и high.

Целое число x называется симметричным, если:
    - оно состоит из чётного количества цифр (2 × n цифр),
    - сумма первых n цифр равна сумме последних n цифр.

Числа с нечётным количеством цифр никогда не являются симметричными.

Необходимо вернуть количество симметричных чисел в диапазоне [low, high] включительно.

Примеры:
Ввод: low = 1, high = 100
Вывод: 9

Ввод: low = 1200, high = 1230
Вывод: 4
'''

def count_symmetric_integers(low: int, high: int) -> int:
    symmetric_count = 0

    for number in range(low, high + 1):
        number_as_string = str(number)
        number_length = len(number_as_string)

        if number_length % 2 != 0:
            continue

        half_length = number_length // 2
        left_part_sum = sum(int(digit) for digit in number_as_string[:half_length])
        right_part_sum = sum(int(digit) for digit in number_as_string[half_length:])

        if left_part_sum == right_part_sum:
            symmetric_count += 1

    return symmetric_count
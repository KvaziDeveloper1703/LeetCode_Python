'''
You are given a positive four-digit integer number. Using the digits of number, split them into two new integers new1 and new2.
All four digits must be used, and you may distribute them in any order. Leading zeros are allowed in both new1 and new2.

For example, if number = 2932, the digits are: two 2’s, one 9, and one 3. Possible pairs include:
[22, 93], [23, 92], [223, 9], [2, 329], etc.

Return the minimum possible sum of new1 + new2.

Examples:
Input: number = 2932
Output: 52

Input: number = 4009
Output: 13

Дано положительное четырёхзначное число number. Используя его цифры, нужно составить два новых числа new1 и new2.
Все четыре цифры должны быть использованы, порядок произвольный. В обоих числах допускаются ведущие нули.

Например, если number = 2932, доступны цифры: две двойки, девятка и тройка. Возможные пары:
[22, 93], [23, 92], [223, 9], [2, 329] и другие.

Нужно вернуть минимально возможную сумму new1 + new2.

Примеры:
Ввод: number = 2932
Вывод: 52

Ввод: number = 4009
Вывод: 13
'''

def minimum_sum(numbers: int) -> int:
    digit_list = [int(single_digit) for single_digit in str(numbers)]
    sorted_digits = sorted(digit_list)

    first_new_number = sorted_digits[0] * 10 + sorted_digits[2]
    second_new_number = sorted_digits[1] * 10 + sorted_digits[3]

    final_sum = first_new_number + second_new_number
    return final_sum
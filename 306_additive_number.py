'''
An additive number is a string whose digits can form an additive sequence.

A valid additive sequence must:
+ Contain at least three numbers.
+ Each number (starting from the third) must be the sum of the previous two.
+ No number in the sequence should have leading zeros.

Given a string consisting only of digits, return true if it can form an additive number, otherwise return false.

Examples:
Input: "112358"
Output: true

Аддитивное число — это строка, состоящая из цифр, которая может быть разбита на последовательность чисел, удовлетворяющую следующим условиям:
+ Последовательность должна содержать как минимум три числа.
+ Начиная с третьего числа, каждое число должно быть суммой двух предыдущих.
+ В последовательности не допускаются ведущие нули (например, "1, 2, 03" или "1, 02, 3" — неверные последовательности).

Дана строка, содержащая только цифры. Верните true, если она представляет аддитивное число, и false в противном случае.

Примеры:
Ввод: "112358"
Вывод: true
'''

def is_additive_number(number: str) -> bool:
    total_length = len(number)

    for first_end in range(1, total_length):
        for second_end in range(first_end + 1, total_length):
            first_number_str = number[:first_end]
            second_number_str = number[first_end:second_end]

            if (len(first_number_str) > 1 and first_number_str[0] == '0') or \
               (len(second_number_str) > 1 and second_number_str[0] == '0'):
                continue

            first_number = int(first_number_str)
            second_number = int(second_number_str)
            remaining_digits = number[second_end:]

            while remaining_digits:
                next_number = first_number + second_number
                next_number_str = str(next_number)

                if not remaining_digits.startswith(next_number_str):
                    break

                remaining_digits = remaining_digits[len(next_number_str):]
                first_number, second_number = second_number, next_number

            if not remaining_digits:
                return True

    return False
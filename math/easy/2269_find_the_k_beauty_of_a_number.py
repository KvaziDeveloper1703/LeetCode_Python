'''
The k-beauty of an integer number is defined as the number of its substrings (when number is treated as a string) that satisfy the following conditions:
    - The substring has a length of k;
    - The integer value of the substring is a divisor of number.

Notes:
    - Leading zeros in substrings are allowed;
    - The value 0 is not considered a divisor of any number;
    - A substring is a contiguous sequence of characters within a string.

Given two integers number and k, return the k-beauty of number.

k-красота числа number - это количество его подстрок (если рассматривать number как строку), которые удовлетворяют следующим условиям:
    - Длина подстроки равна k;
    - Числовое значение подстроки является делителем числа number.

Примечания:
    - Ведущие нули в подстроках допускаются;
    - Число 0 не является делителем ни одного числа;
    - Подстрока - это непрерывная последовательность символов в строке.

Даны два целых числа number и k. Требуется вернуть k-красоту числа number.
'''

def divisor_substrings(number: int, k: int) -> int:
    number_str = str(number)
    count = 0

    for i in range(len(number_str) - k + 1):
        substring = number_str[i:i + k]
        value = int(substring)

        if value != 0 and number % value == 0:
            count += 1

    return count
'''
Given a positive integer number that only contains the digits 6 and 9.

You are allowed to change at most one digit:
    + You can change a 6 to a 9;
    + You can change a 9 to a 6.

Return the maximum number you can get after performing at most one digit change.

Examples:
Input: number = 9669
Output: 9969

Input: number = 9996
Output: 9999

Дано положительное целое число number, которое состоит только из цифр 6 и 9.

Разрешено изменить не более одной цифры:
    + Цифру 6 можно заменить на 9;
    + Цифру 9 можно заменить на 6.

Нужно вернуть максимальное число, которое можно получить после одной замены.

Примеры:
Ввод: number = 9669
Вывод: 9969

Ввод: number = 9996
Вывод: 9999
'''

def maximum_69_number(number: int) -> int:
    number_str = list(str(number))
    for i in range(len(number_str)):
        if number_str[i] == '6':
            number_str[i] = '9'
            break
    return int(''.join(number_str))
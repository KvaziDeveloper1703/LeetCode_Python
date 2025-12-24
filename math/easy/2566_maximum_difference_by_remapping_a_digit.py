'''
You are given an integer number. Bob will secretly choose one digit and remap it to another digit.

Return the difference between the maximum and minimum values Bob can obtain by remapping exactly one digit in number.

Rules:
    - When Bob remaps a digit d1 to another digit d2, all occurrences of d1 in number are replaced with d2;
    - Bob can remap a digit to itself - in this case, number does not change;
    - Bob may use different remappings to obtain the maximum and minimum values;
    - The resulting number may contain leading zeroes.

Examples:
Input: number = 11891
Output: 99009

Input: number = 90
Output: 99

Вам дано целое число number. Боб тайно выбирает одну цифру и заменяет её на другую цифру.

Необходимо вернуть разницу между максимальным и минимальным значениями, которые Боб может получить, выполнив ровно одну замену цифры в числе number.

Правила:
    - При замене цифры d1 на цифру d2 все вхождения d1 в числе number заменяются на d2;
    - Разрешается заменить цифру саму на себя - в этом случае число number не изменится;
    - Для получения максимального и минимального значений можно использовать разные замены;
    - В результате могут появляться ведущие нули.

Примеры:
Ввод: number = 11891
Вывод: 99009

Ввод: number = 90
Вывод: 99
'''

def min_max_difference(number: int) -> int:
    number_as_string = str(number)

    digit_for_maximum = None
    for digit in number_as_string:
        if digit != '9':
            digit_for_maximum = digit
            break

    if digit_for_maximum is None:
        maximum_value = number
    else:
        maximum_value = int(number_as_string.replace(digit_for_maximum, '9'))

    digit_for_minimum = None
    for digit in number_as_string:
        if digit != '0':
            digit_for_minimum = digit
            break

    if digit_for_minimum is None:
        minimum_value = number
    else:
        minimum_value = int(number_as_string.replace(digit_for_minimum, '0'))

    return maximum_value - minimum_value
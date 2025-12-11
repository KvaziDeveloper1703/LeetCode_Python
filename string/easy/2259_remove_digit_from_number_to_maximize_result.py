'''
You are given a string number that represents a positive integer, and a character digit.

You must remove exactly one occurrence of digit from number so that the resulting string represents the maximum possible value in decimal form.
It is guaranteed that digit appears at least once in number.

Return the string obtained after removing the optimal occurrence of digit.

Вам дана строка number, представляющая положительное целое число, и символ digit.

Нужно удалить ровно одно вхождение digit из строки number так, чтобы получившаяся строка представляла максимально возможное десятичное число.
Гарантируется, что digit встречается в number как минимум один раз.

Верните строку, полученную после удаления оптимального вхождения digit.
'''

def remove_digit(number: str, digit: str) -> str:
    best_result = ""

    for index in range(len(number)):
        if number[index] == digit:
            current_result = number[:index] + number[index + 1:]
            if current_result > best_result:
                best_result = current_result

    return best_result
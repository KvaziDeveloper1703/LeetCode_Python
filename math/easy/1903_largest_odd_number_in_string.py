'''
You are given a string number that represents a large integer.
Return the largest odd-valued integer that appears as a non-empty substring of number.
If no odd substring exists, return an empty string "".

A substring is a contiguous sequence of characters in a string.

Examples:
Input: number = "52"
Output: "5"

Input: number = "4206"
Output: ""

Дана строка number, представляющая большое целое число.
Верните наибольшее нечётное число, которое является непустой подстрокой строки number.
Если нечётной подстроки не существует, верните пустую строку "".

Подстрока - это непрерывная последовательность символов строки.

Примеры:
Ввод: number = "52"
Вывод: "5"

Ввод: number = "4206"
Вывод: ""
'''

def largest_odd_number(number: str) -> str:
    for index in range(len(number) - 1, -1, -1):
        if int(number[index]) % 2 == 1:
            return number[:index + 1]
    return ""
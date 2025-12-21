'''
The value of an alphanumeric string is defined as follows:
    - If the string consists of digits only, its value is the base-10 numeric representation of the string;
    - Otherwise, its value is equal to the length of the string.

You are given an array strs consisting of alphanumeric strings.

Return the maximum value among all strings in the array.

Examples:
Input: strs = ["alic3", "bob", "3", "4", "00000"]
Output: 5

Input: strs = ["1", "01", "001", "0001"]
Output: 1

Значение алфавитно-цифровой строки определяется следующим образом:
    - Если строка состоит только из цифр, её значение равно числовому значению в десятичной системе счисления;
    - В противном случае значение строки равно её длине.

Дан массив strs, состоящий из алфавитно-цифровых строк.

Необходимо вернуть максимальное значение среди всех строк массива.

Примеры:
Ввод: strs = ["alic3", "bob", "3", "4", "00000"]
Вывод: 5

Ввод: strs = ["1", "01", "001", "0001"]
Вывод: 1
'''

def maximum_value(strings: list[str]) -> int:
    maximum_value = 0

    for current_string in strings:
        if current_string.isdigit():
            current_value = int(current_string)
        else:
            current_value = len(current_string)

        maximum_value = max(maximum_value, current_value)

    return maximum_value
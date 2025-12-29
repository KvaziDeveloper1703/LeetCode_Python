'''
You are given a positive integer number, represented as a string.

Your task is to remove all trailing zeros from number and return the resulting number as a string.

Return the string representation of the integer number after removing all zeros at the end of the number.

Examples:
Input: number = "51230100"
Output: "512301"

Input: number = "123"
Output: "123"

Дано положительное целое число number, представленное в виде строки.

Необходимо удалить все концевые нули числа number и вернуть получившееся число в виде строки.

Вернуть строковое представление числа number после удаления всех нулей, стоящих в конце строки.

Примеры:
Ввод: number = "51230100"
Вывод: "512301"

Ввод: number = "123"
Вывод: "123"
'''

def remove_trailing_zeros(number: str) -> str:
    return number.rstrip('0')
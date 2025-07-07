'''
You are a product manager leading a team to develop a new product. Unfortunately, the latest version failed the quality check.
Since each version is built upon the previous one, all versions after a bad version are also bad.
You are given n versions, numbered from 1 to n, and you need to find the first bad version that caused all subsequent versions to fail.
An API bool is_bad_version(version) is provided, which returns True if the version is bad and False otherwise.
Implement a function to find the first bad version. Try to minimize the number of API calls.

Examples:
Input: n = 5, bad = 4
Output: 4

Input: n = 1, bad = 1
Output: 1

Вы — менеджер продукта и руководите командой, разрабатывающей новый продукт. К сожалению, последняя версия продукта не прошла проверку качества.
Поскольку каждая версия разрабатывается на основе предыдущей, все версии после плохой тоже являются плохими.
У вас есть n версий, пронумерованных от 1 до n. Ваша задача — найти первую плохую версию, из-за которой испортились все последующие.
У вас уже есть API-функция bool is_bad_version(version), которая возвращает True, если версия плохая, и False, если хорошая.
Реализуйте функцию, чтобы найти первую плохую версию. Постарайтесь минимизировать количество вызовов API.

Примеры:
Ввод: n = 5, bad = 4
Вывод: 4

Ввод: n = 1, bad = 1
Вывод: 1
'''

def first_bad_version(n: int) -> int:
    left, right = 1, n
        
    while left < right:
        middle = (left + right) // 2
        if is_bad_version(middle):
            right = middle
        else:
            left = middle + 1
        
    return left
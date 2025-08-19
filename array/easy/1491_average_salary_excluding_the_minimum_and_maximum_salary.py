'''
Given an array of unique integers salary, where salary[i] represents the salary of the i-th employee.

Return the average salary of employees, excluding the minimum and maximum salary.

The answer will be accepted if it is within 10^-5 of the actual result.

Examples:
Input: salary = [4000, 3000, 1000, 2000]
Output: 2500.00000

Input: salary = [1000, 2000, 3000]
Output: 2000.00000

Вам дан массив уникальных целых чисел salary, где salary[i] — это зарплата i-го сотрудника.

Необходимо вернуть среднее значение зарплат сотрудников, исключив минимальную и максимальную зарплаты.

Ответ будет засчитан, если погрешность не превышает 10^-5.

Примеры:
Ввод: salary = [4000, 3000, 1000, 2000]
Вывод: 2500.00000

Ввод: salary = [1000, 2000, 3000]
Вывод: 2000.00000
'''

from typing import List

def average(salary: List[int]) -> float:
    total = sum(salary)
    min_salary = min(salary)
    max_salary = max(salary)

    total -= (min_salary + max_salary)
    count = len(salary) - 2
    return total / count
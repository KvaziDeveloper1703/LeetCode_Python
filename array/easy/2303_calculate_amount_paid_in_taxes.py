'''
You are given a 0-indexed 2D integer array brackets, where brackets[i] = [upper_i, percent_i] means that the i-th tax bracket has an upper income limit of upper_i and is taxed at a rate of percent_i.

The tax brackets are sorted in increasing order of upper bound, meaning upper_{i-1} < upper_i for all 0 < i < brackets.length.

Taxes are calculated as follows:
    - The first upper_0 dollars of income are taxed at a rate of percent_0;
    - The next upper_1 - upper_0 dollars are taxed at a rate of percent_1;
    - The next upper_2 - upper_1 dollars are taxed at a rate of percent_2;
    - And so on.

You are also given an integer income, which represents the total amount of money you earned.

Return the total amount of tax that you have to pay. Answers with an absolute error of at most 10⁻⁵ will be accepted.

Examples:
Input: brackets = [[3, 50], [7, 10], [12, 25]], income = 10
Output: 2.65000

Input: brackets = [[1, 0], [4, 25], [5, 50]], income = 2
Output: 0.25000

Дан двумерный целочисленный массив brackets с индексацией с нуля, где brackets[i] = [upper_i, percent_i] означает, что i-й налоговый диапазон имеет верхнюю границу дохода upper_i и облагается налогом по ставке percent_i процентов.

Налоговые диапазоны отсортированы по возрастанию верхней границы дохода, то есть upper_{i-1} < upper_i для всех 0 < i < brackets.length.

Налог рассчитывается следующим образом:
    - Первые upper_0 долларов дохода облагаются налогом по ставке percent_0;
    - Следующие upper_1 − upper_0 долларов — по ставке percent_1;
    - Следующие upper_2 − upper_1 долларов — по ставке percent_2;
    - И так далее.

Также дано целое число income, которое обозначает общий полученный доход.

Необходимо вернуть суммарную сумму налога, которую нужно заплатить. Ответ считается корректным, если абсолютная погрешность не превышает 10⁻⁵.

Примеры:
Ввод: brackets = [[3, 50], [7, 10], [12, 25]], income = 10
Вывод: 2.65000

Ввод: brackets = [[1, 0], [4, 25], [5, 50]], income = 2
Вывод: 0.25000
'''

from typing import List

def calculate_tax(brackets: List[List[int]], income: int) -> float:
    total_tax = 0.0
    previous_upper = 0

    for upper_bound, percent in brackets:
        if income <= previous_upper:
            break

        taxable_amount = min(income, upper_bound) - previous_upper
        total_tax += taxable_amount * (percent / 100)

        previous_upper = upper_bound

    return total_tax
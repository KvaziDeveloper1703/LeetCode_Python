'''
Given an integer n. Group all integers from 1 to n by the sum of their digits.

Return the number of groups that have the largest size.

Examples:
Input: n = 13
Output: 4

Input: n = 2
Output: 2

Дано целое число n. Разделите все числа от 1 до n на группы по сумме их цифр.

Нужно вернуть количество групп, имеющих наибольший размер.

Примеры:
Ввод:  n = 13
Вывод: 4

Ввод:  n = 2
Вывод: 2
'''

from typing import Dict

def count_largest_group(n: int) -> int:
    def digit_sum(value: int) -> int:
        total = 0
        while value > 0:
            total += value % 10
            value //= 10
        return total

    group_sizes: Dict[int, int] = {}
    for number in range(1, n + 1):
        s = digit_sum(number)
        group_sizes[s] = group_sizes.get(s, 0) + 1

    max_size = max(group_sizes.values())
    largest_groups_count = sum(1 for size in group_sizes.values() if size == max_size)
    return largest_groups_count
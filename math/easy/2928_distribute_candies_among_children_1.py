'''
You are given two positive integers n and limit.

Determine the total number of different ways to distribute n candies among 3 children, such that no child receives more than limit candies.

Each distribution is represented as an ordered triple (a,b,c), where: a+b+c=n, 0 ≤ a,b,c ≤ limit.

Examples:
Input: n = 5, limit = 2
Output: 3

Input: n = 3, limit = 3
Output: 10

Даны два положительных целых числа n и limit.

Найдите общее количество способов распределить n конфет между 3 детьми так, чтобы ни один ребёнок не получил больше limit конфет.

Каждое распределение задаётся упорядоченной тройкой (a,b,c), где: a+b+c=n, 0 ≤ a,b,c ≤ limit.

Примеры:
Ввод: n = 5, limit = 2
Вывод: 3

Ввод: n = 3, limit = 3
Вывод: 10
'''

def distribute_candies(n: int, limit: int) -> int:
    count = 0

    for a in range(min(limit, n) + 1):
        for b in range(min(limit, n - a) + 1):
            c = n - a - b
            if c <= limit:
                count += 1

    return count
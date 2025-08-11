'''
You are given an integer n. Return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that:
    + runs in O(n) time,
    + and uses O(1) extra space.

Examples:
Input: n = 13
Output: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

Input: n = 2
Output: [1, 2]

Вам дано целое число n. Верните все числа от 1 до n, отсортированные в лексикографическом порядке (как в словаре).

Требуется реализовать алгоритм, который:
    + работает за O(n) по времени,
    + использует O(1) дополнительной памяти.

Примеры:
Ввод: n = 13
Вывод: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

Ввод: n = 2
Вывод: [1, 2]
'''

def lexical_order(n: int) -> list[int]:
    result = []

    def dfs(current: int):
        if current > n:
            return
        result.append(current)
        for i in range(10):
            next_number = current * 10 + i
            if next_number > n:
                return
            dfs(next_number)

    for i in range(1, 10):
        dfs(i)

    return result
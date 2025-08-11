'''
You are given an integer n. Your task is to return the number of structurally unique Binary Search Trees that can be formed with n distinct values from 1 to n.

Examples:
Input: n = 3
Output: 5

Input: n = 1
Output: 1

Дано целое число n. Необходимо определить количество структурно уникальных бинарных деревьев поиска, которые можно построить, используя n различных значений от 1 до n.

Примеры:
Ввод: n = 3
Вывод: 5

Ввод: n = 1
Вывод: 1
'''

def number_of_trees(n: int) -> int:
    number_of_unique_bsts = [0] * (n + 1)
    number_of_unique_bsts[0] = 1
    number_of_unique_bsts[1] = 1

    for total_nodes in range(2, n + 1):
        for root in range(1, total_nodes + 1):
            left_subtree_size = root - 1
            right_subtree_size = total_nodes - root
            number_of_unique_bsts[total_nodes] += (
                number_of_unique_bsts[left_subtree_size] * number_of_unique_bsts[right_subtree_size]
            )

    return number_of_unique_bsts[n]
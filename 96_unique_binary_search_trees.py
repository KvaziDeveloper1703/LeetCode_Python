'''
You are given an integer n. Your task is to return the number of structurally unique Binary Search Trees (BSTs) that can be formed with n distinct values from 1 to n.

Examples:
Input: n = 3
Output: 5

Input: n = 1
Output: 1

Дано целое число n. Необходимо определить количество структурно уникальных бинарных деревьев поиска (BST), которые можно построить, используя n различных значений от 1 до n.

Примеры:
Ввод: n = 3
Вывод: 5

Ввод: n = 1
Вывод: 1
'''

def num_trees(n: int) -> int:
    num_unique_bsts = [0] * (n + 1)
    num_unique_bsts[0] = 1
    num_unique_bsts[1] = 1

    for total_nodes in range(2, n + 1):
        for root in range(1, total_nodes + 1):
            left_subtree_size = root - 1
            right_subtree_size = total_nodes - root
            num_unique_bsts[total_nodes] += (
                num_unique_bsts[left_subtree_size] * num_unique_bsts[right_subtree_size]
            )

    return num_unique_bsts[n]
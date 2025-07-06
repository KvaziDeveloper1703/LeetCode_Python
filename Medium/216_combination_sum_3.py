'''
Find all unique combinations of k numbers that add up to a target sum n, subject to the following constraints:
    + Only numbers from 1 to 9 can be used.
    + Each number can be used at most once in a combination.
    + Return a list of all valid combinations. The same combination should not appear more than once, and the order of combinations in the list does not matter.

Examples:
Input: k = 3, n = 7
Output: [[1, 2, 4]]

Input: k = 3, n = 9
Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]

Найдите все уникальные комбинации из k чисел, сумма которых равна заданному числу n, при соблюдении следующих условий:
    + Используются только числа от 1 до 9.
    + Каждое число может использоваться не более одного раза.
    + Необходимо вернуть список всех допустимых комбинаций, без повторяющихся. Порядок комбинаций в списке не важен.

Примеры:
Ввод: k = 3, n = 7
Вывод: [[1, 2, 4]]

Ввод: k = 3, n = 9
Вывод: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
'''

from typing import List

def combination_sum_3(number_count: int, target_sum: int) -> List[List[int]]:
    valid_combinations = []

    def backtrack(start_number: int, current_combination: List[int], current_sum: int):
        if len(current_combination) == number_count:
            if current_sum == target_sum:
                valid_combinations.append(current_combination[:])
            return
        
        for next_number in range(start_number, 10):
            if current_sum + next_number > target_sum:
                break
            current_combination.append(next_number)
            backtrack(next_number + 1, current_combination, current_sum + next_number)
            current_combination.pop()
    
    backtrack(1, [], 0)
    return valid_combinations
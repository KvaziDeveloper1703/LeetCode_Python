'''
You are given an array numbers consisting of positive integers and an integer k.

In one operation, you can remove the last element of the array and add it to your collection.

Your goal is to collect all elements 1, 2, ..., k.

Return the minimum number of operations required to collect all these elements.

Examples:
Input: numbers = [3,1,5,4,2], k = 2
Output: 4

Input: numbers = [3,1,5,4,2], k = 5
Output: 5

Вам дан массив numbers, состоящий из положительных целых чисел, и целое число k.

За одну операцию вы можете удалить последний элемент массива и добавить его в свою коллекцию.

Необходимо собрать все элементы 1, 2, ..., k.

Верните минимальное количество операций, необходимых для этого.

Примеры:
Ввод: numbers = [3,1,5,4,2], k = 2
Вывод: 4

Ввод: numbers = [3,1,5,4,2], k = 5
Вывод: 5
'''

from typing import List

def min_operations(numbers: List[int], k: int) -> int:
    required_numbers = set(range(1, k + 1))
    operation_count = 0

    for current_number in reversed(numbers):
        operation_count += 1
        if current_number in required_numbers:
            required_numbers.remove(current_number)
            if not required_numbers:
                return operation_count

    return operation_count
'''
You are given an array of integers numbers.

You may repeatedly perform the following operation:
    - Remove the first two elements of the array numbers;
    - The score of the operation is the sum of the two removed elements.

You can perform this operation only while the array contains at least two elements.

All performed operations must have the same score.

Return the maximum number of operations that can be performed.

Examples:
Input: numbers = [3,2,1,4,5]
Output: 2

Input: numbers = [1,5,3,3,4,1,3,2,2,3]
Output: 2

Дан массив целых чисел numbers.

Вы можете многократно выполнять следующую операцию:
    - Удалить первые два элемента массива numbers;
    - Счёт операции равен сумме двух удалённых элементов.

Операцию можно выполнять, пока в массиве есть как минимум два элемента.

При этом счёт всех операций должен быть одинаковым.

Верните максимальное количество операций, которое можно выполнить.

Примеры:
Ввод: numbers = [3,2,1,4,5]
Вывод: 2

Ввод: numbers = [1,5,3,3,4,1,3,2,2,3]
Вывод: 2
'''

from typing import List

def max_operations(numbers: List[int]) -> int:
    if len(numbers) < 2:
        return 0

    target_sum = numbers[0] + numbers[1]
    operations_count = 0
    index = 0

    while index + 1 < len(numbers):
        if numbers[index] + numbers[index + 1] != target_sum:
            break
        operations_count += 1
        index += 2

    return operations_count
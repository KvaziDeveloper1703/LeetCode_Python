'''
You are given a 0-indexed array numbers of size n consisting of non-negative integers.

You must perform exactly n - 1 operations on this array.

In the i-th operation (0 ≤ i ≤ n - 2), apply the following rule to the element numbers[i]:
    - If numbers[i] is equal to numbers[i + 1], then:
        - multiply numbers[i] by 2;
        - set numbers[i + 1] to 0.
    - Otherwise, do nothing.

All operations are applied sequentially, from left to right, meaning each operation uses the current state of the array after the previous operations.

After completing all operations, shift all zeros to the end of the array, while preserving the order of the non-zero elements.

Return the resulting array.

Examples:
Input: numbers = [1, 2, 2, 1, 1, 0]
Output: [1, 4, 2, 0, 0, 0]

Input: numbers = [0, 1]
Output: [1, 0]

Дан 0-индексированный массив numbers длины n, состоящий из неотрицательных целых чисел.

Необходимо выполнить ровно n - 1 операций.

В i-й операции (0 ≤ i ≤ n - 2) выполняется следующее действие над элементом numbers[i]:
    - Если numbers[i] равно numbers[i + 1], то:
        - умножить numbers[i] на 2;
        - присвоить numbers[i + 1] значение 0.
    - В противном случае операция пропускается.

Все операции выполняются последовательно, слева направо, с учётом изменений массива после каждой операции.

После выполнения всех операций необходимо переместить все нули в конец массива, сохранив относительный порядок ненулевых элементов.

Верните получившийся массив.

Примеры:
Ввод: numbers = [1, 2, 2, 1, 1, 0]
Вывод: [1, 4, 2, 0, 0, 0]

Ввод: numbers = [0, 1]
Вывод: [1, 0]
'''

from typing import List

def apply_operations(numbers: List[int]) -> List[int]:
    length = len(numbers)

    for index in range(length - 1):
        if numbers[index] == numbers[index + 1]:
            numbers[index] *= 2
            numbers[index + 1] = 0

    non_zero_elements = []
    zero_count = 0

    for number in numbers:
        if number == 0:
            zero_count += 1
        else:
            non_zero_elements.append(number)

    return non_zero_elements + [0] * zero_count
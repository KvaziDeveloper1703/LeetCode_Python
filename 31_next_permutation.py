'''
A permutation of an array of integers is any arrangement of its elements in a sequence. 
For example, for arr = [1,2,3], all possible permutations include [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

The next permutation of an array is the next lexicographically greater arrangement of its elements. 
If no such greater permutation exists, you must rearrange the array into the lowest possible order, which is the ascending order.

Your task is: given an array of integers nums, modify it in-place to become its next permutation. You must do this using only constant extra memory.

Examples:
Input: numbers = [1,2,3]
Output: [1,3,2]

Input: numbers = [3,2,1]
Output: [1,2,3]

Перестановка массива целых чисел — это любое упорядочивание его элементов в последовательность. 
Например, для arr = [1,2,3] возможны следующие перестановки: [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1].

Следующая перестановка — это лексикографически следующая. 
Если такой перестановки не существует, массив нужно преобразовать в наименьший возможный порядок — то есть отсортировать по возрастанию.

Ваша задача: по данному массиву nums найти его следующую перестановку.
Изменения должны быть выполнены на месте, с использованием только постоянной дополнительной памяти.

Примеры:
Ввод: numbers = [1,2,3]
Вывод: [1,3,2]

Ввод: numbers = [3,2,1]
Вывод: [1,2,3]
'''

from typing import List

def next_permutation(numbers: List[int]) -> None:
    i = len(numbers) - 2
    while i >= 0 and numbers[i] >= numbers[i + 1]:
        i -= 1
    if i >= 0:
        j = len(numbers) - 1
        while numbers[j] <= numbers[i]:
            j -= 1
        numbers[i], numbers[j] = numbers[j], numbers[i]
    left, right = i + 1, len(numbers) - 1
    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1
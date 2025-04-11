'''
You are given a sorted integer array numbers (in non-decreasing order). Modify the array in-place so that each unique element appears at most twice, while preserving the relative order of the elements.
Since it's not possible to change the size of the array in some programming languages, you should place the result in the first part of the array nums. More formally:
+ Let k be the number of elements after removing extra duplicates;
+ The first k elements of numbers should contain the final result;
+ The remaining elements beyond the first k positions do not matter.

You must not use any extra space — the algorithm should run in-place with O(1) extra memory.
Return the value of k.

Examples:
Input: numbers = [1, 1, 1, 2, 2, 3]
Output: 5, numbers = [1, 1, 2, 2, 3, _]

Input: numbers = [0, 0, 1, 1, 1, 1, 2, 3, 3]
Output: 7, numbers = [0, 0, 1, 1, 2, 3, 3, _, _]

Дан отсортированный по неубыванию массив целых чисел numbers.
Необходимо изменить массив на месте так, чтобы каждое уникальное число встречалось не более двух раз, при этом сохранив относительный порядок элементов.
Так как в некоторых языках программирования нельзя менять размер массива, результат нужно разместить в первых k элементах массива numbers. Формально:
+ Пусть k — количество элементов после удаления лишних повторов;
+ Первые k элементов массива должны содержать итоговый результат;
+ Остальные элементы после позиции k могут быть любыми — они не имеют значения.

Нельзя использовать дополнительную память — алгоритм должен работать на месте с O(1) дополнительной памяти.
Верните значение k.

Примеры:
Вход: numbers = [1, 1, 1, 2, 2, 3]
Выход: 5, numbers = [1, 1, 2, 2, 3, _]

Вход: numbers = [0, 0, 1, 1, 1, 1, 2, 3, 3]
Выход: 7, numbers = [0, 0, 1, 1, 2, 3, 3, _, _]
'''

from typing import List

def remove_duplicates(numbers: List[int]) -> int:
    if len(numbers) <= 2:
        return len(numbers)

    write_index = 2

    for read_index in range(2, len(numbers)):
        if numbers[read_index] != numbers[write_index - 2]:
            numbers[write_index] = numbers[read_index]
            write_index += 1

    return write_index
'''
You are given a sorted integer array numbers in non-decreasing order. Your task is to remove duplicates in-place so that each unique element appears only once, and the relative order of the elements is preserved.
After removing the duplicates, return the number of unique elements, denoted as k.

Requirements:
    + Modify the array numbers in-place so that the first k elements contain the unique elements in their original order;
    + The remaining elements beyond index k - 1 do not matter — you can leave them as-is;
    + Return the value of k.

Examples:
Input: numbers = [1, 1, 2]
Output: 2, numbers = [1, 2, _]

Input: numbers = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 5, numbers = [0, 1, 2, 3, 4, _, _, _, _, _]

Дан отсортированный по неубыванию массив целых чисел numbers. Ваша задача — удалить дубликаты на месте, чтобы каждый уникальный элемент встречался только один раз, при этом сохраняя относительный порядок элементов.
После удаления дубликатов верните количество уникальных элементов — обозначим его как k.

Требования:
    + Измените массив numbers на месте так, чтобы первые k элементов содержали уникальные значения в исходном порядке;
    + Остальная часть массива может содержать любые значения — она не имеет значения;
    + Верните значение k.

Примеры:
Ввод: numbers = [1, 1, 2]
Вывод: 2, numbers = [1, 2, _]

Ввод: numbers = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Вывод: 5, numbers = [0, 1, 2, 3, 4, _, _, _, _, _]
'''

from typing import List

def remove_duplicates(numbers: List[int]) -> int:
    if not numbers:
        return 0

    write_index = 1

    for read_index in range(1, len(numbers)):
        if numbers[read_index] != numbers[write_index - 1]:
            numbers[write_index] = numbers[read_index]
            write_index += 1

    return write_index
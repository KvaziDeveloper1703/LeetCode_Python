'''
You are given an integer array numbers and an integer value. Your task is to remove all occurrences of value from the array in-place. The relative order of the elements may change.
After removing all instances of value, return the number of elements that remain, denoted as k.

Requirements:
    + Modify the array numbers in-place such that the first k elements are the elements not equal to value;
    + The remaining elements beyond index k - 1 do not matter — you can leave them as-is;
    + Return the value of k.

Examples:
Input: numbers = [3, 2, 2, 3], value = 3
Output: 2, numbers = [2, 2, _, _]

Input: numbers = [0, 1, 2, 2, 3, 0, 4, 2], value = 2
Output: 5, numbers = [0, 1, 4, 0, 3, _, _, _]

Дан массив целых чисел numbers и целое число value. Ваша задача — удалить все вхождения значения value из массива на месте. При этом относительный порядок элементов может измениться.
После удаления всех вхождений value верните количество оставшихся элементов — обозначим его как k.

Требования:
    + Измените массив numbers на месте так, чтобы первые k элементов не были равны value;
    + Остальные элементы массива не имеют значения — можно оставить как есть;
    + Верните значение k.

Примеры:
Ввод: numbers = [3, 2, 2, 3], value = 3
Выход: 2, numbers = [2, 2, _, _]

Ввод: numbers = [0, 1, 2, 2, 3, 0, 4, 2], value = 2
Выход: 5, numbers = [0, 1, 4, 0, 3, _, _, _]
'''

from typing import List

def remove_element(numbers: List[int], value: int) -> int:
    write_index = 0

    for read_index in range(len(numbers)):
        if numbers[read_index] != value:
            numbers[write_index] = numbers[read_index]
            write_index += 1

    return write_index
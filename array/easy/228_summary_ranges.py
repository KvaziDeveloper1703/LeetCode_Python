'''
You are given a sorted unique integer array numbers. A range [a, b] is the set of all integers from a to b.
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of numbers is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in numbers.

Each range [a, b] in the list should be output as:
    + "a->b" if a != b
    + "a" if a == b

Examples:
Input: numbers = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

Input: numbers = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]

Дан отсортированный массив уникальных целых чисел numbers.
Диапазон [a, b] — это множество всех целых чисел от a до b включительно.
Необходимо вернуть наименьший отсортированный список диапазонов, которые в точности покрывают все числа в массиве. 
То есть каждое число из массива должно входить ровно в один из диапазонов, и не должно быть такого целого числа x, которое принадлежит какому-либо диапазону, но отсутствует в массиве numbers.

Каждый диапазон [a, b] в итоговом списке нужно выводить так:
    + "a->b", если a != b
    + "a", если a == b

Примеры:
Ввод: numbers = [0,1,2,4,5,7]
Вывод: ["0->2","4->5","7"]

Ввод: numbers = [0,2,3,4,6,8,9]
Вывод: ["0","2->4","6","8->9"]
'''

from typing import List

def summary_ranges(numbers: List[int]) -> List[str]:
    if not numbers:
        return []

    result = []
    start = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1] + 1:
            if start == numbers[i - 1]:
                result.append(str(start))
            else:
                result.append(f"{start}->{numbers[i - 1]}")
            start = numbers[i]

    if start == numbers[-1]:
        result.append(str(start))
    else:
        result.append(f"{start}->{numbers[-1]}")

    return result
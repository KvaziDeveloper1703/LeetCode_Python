'''
You are given an array of integers numbers.

Your task is to sort the array based on the following rules:
- Numbers with a lower frequency come first;
- If two numbers have the same frequency, they should be sorted in decreasing numerical order.

Return the sorted array.

Examples:
Input: numbers = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]

Input: numbers = [2,3,1,3,2]
Output: [1,3,3,2,2]

Дан массив целых чисел numbers.

Необходимо отсортировать его по следующим правилам:
- Числа, которые встречаются реже, должны идти раньше;
- Если несколько чисел имеют одинаковую частоту, то их нужно отсортировать по убыванию значения.

Верните отсортированный массив.

Примеры:
Ввод: numbers = [1,1,2,2,2,3]
Вывод: [3,1,1,2,2,2]

Ввод: numbers = [2,3,1,3,2]
Вывод: [1,3,3,2,2]
'''

from typing import List

def frequency_sort(numbers: List[int]) -> List[int]:
    frequency = {}
    for x in numbers:
        if x in frequency:
            frequency[x] += 1
        else:
            frequency[x] = 1

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if frequency[numbers[i]] > frequency[numbers[j]] or (frequency[numbers[i]] == frequency[numbers[j]] and numbers[i] < numbers[j]):
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers
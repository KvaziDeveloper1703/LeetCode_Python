'''
You are given a 0-indexed integer array numbers and an integer key, which is guaranteed to appear in the array.

For each unique integer target in the array, count how many times target appears immediately after key.

In other words, count the number of indices i such that:
    - 0≤i≤numbers.length−2;
    - numbers[i]=key;
    - numbers[i+1]=target.

Return the target with the highest count.

It is guaranteed that exactly one such target has the maximum count.

Examples:
Input: numbers = [1,100,200,1,100], key = 1
Output: 100

Input: numbers = [2,2,2,2,3], key = 2
Output: 2

Вам дан целочисленный массив numbers, индексируемый с нуля, а также целое число key, которое гарантированно присутствует в массиве.

Для каждого уникального числа target из массива нужно подсчитать, сколько раз target встречается сразу после key.

То есть найти количество индексов i, для которых выполняются условия:
    - 0≤i≤numbers.length−2;
    - numbers[i]=key;
    - numbers[i+1]=target.

Верните то число target, которое встречается после key чаще всего.

Гарантируется, что такое число единственное.

Примеры:
Ввод: numbers = [1,100,200,1,100], key = 1
Вывод: 100

Ввод: numbers = [2,2,2,2,3], key = 2
Вывод: 2
'''

from typing import List

def most_frequent(numbers: List[int], key: int) -> int:
    frequency_by_target: dict[int, int] = {}

    for index in range(len(numbers) - 1):
        if numbers[index] == key:
            current_target = numbers[index + 1]
            frequency_by_target[current_target] = (
                frequency_by_target.get(current_target, 0) + 1
            )

    most_frequent_target = max(frequency_by_target, key=frequency_by_target.get)
    return most_frequent_target
'''
You are given an integer array numbers of length n and two integers k and x.

The x-sum of an array is defined as follows:
    - Count the frequency of each distinct element in the array;
    - Keep only the elements that belong to the top x most frequent elements;
        - If multiple elements have the same frequency, the element with the larger value is considered more frequent.
    - The x-sum is the sum of all occurrences of the selected elements;
    - If the array contains fewer than x distinct elements, the x-sum is simply the sum of the entire array.

Your task is to return an array answer of length n - k + 1, where answer[i] is the x-sum of the subarray numbers[i..i + k - 1].

Examples:
Input: numbers = [1,1,2,2,3,4,2,3], k = 6, x = 2
Output: [6, 10, 12]

Input: numbers = [3,8,7,8,7,5], k = 2, x = 2
Output: [11, 15, 15, 15, 12]

Дан массив целых чисел numbers длины n и два целых числа k и x.

X-сумма массива вычисляется следующим образом:
    - Подсчитывается количество вхождений каждого элемента массива;
    - Оставляются только элементы, входящие в топ x самых частых элементов;
        - Если несколько элементов встречаются одинаковое количество раз, более частым считается элемент с большим значением.
    - X-сумма равна сумме всех вхождений выбранных элементов;
    - Если в массиве меньше x различных элементов, x-сумма равна сумме всего массива.

Необходимо вернуть массив answer длины n - k + 1, где answer[i] - это x-сумма подмассива numbers[i..i + k - 1].

Примеры:
Ввод: numbers = [1,1,2,2,3,4,2,3], k = 6, x = 2
Вывод: [6, 10, 12]

Ввод: numbers = [3,8,7,8,7,5], k = 2, x = 2
Вывод: [11, 15, 15, 15, 12]
'''

from typing import List
from collections import Counter

def find_x_sum(numbers: List[int], k: int, x: int) -> List[int]:
    result = []

    for left_index in range(len(numbers) - k + 1):
        window = numbers[left_index:left_index + k]
        frequency_map = Counter(window)

        if len(frequency_map) <= x:
            result.append(sum(window))
            continue

        sorted_elements = sorted(frequency_map.items(), key=lambda item: (item[1], item[0]), reverse=True)
        
        current_sum = 0
        for value, frequency in sorted_elements[:x]:
            current_sum += value * frequency

        result.append(current_sum)

    return result
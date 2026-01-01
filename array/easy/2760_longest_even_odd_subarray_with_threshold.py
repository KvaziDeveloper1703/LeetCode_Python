'''
You are given a 0-indexed integer array numbers and an integer threshold.

Find the maximum length of a subarray of numbers that starts at index l and ends at index r (0 ≤ l ≤ r < numbers.length) and satisfies all of the following conditions:
    - numbers[l] is even: numbers[l] % 2 == 0;
    - For every index i in the range [l, r - 1], the parity of consecutive elements alternates: numbers[i] % 2 != numbers[i + 1] % 2;
    - Every element in the subarray is less than or equal to threshold: numbers[i] <= threshold   for all i in [l, r].

Return an integer representing the length of the longest subarray that satisfies these conditions.

Examples:
Input: numbers = [3, 2, 5, 4], threshold = 5
Output: 3

Input: numbers = [1, 2], threshold = 2
Output: 1

Дан 0-индексированный массив целых чисел numbers и целое число threshold.

Необходимо найти максимальную длину подмассива массива numbers, начинающегося в индексе l и заканчивающегося в индексе r (0 ≤ l ≤ r < numbers.length), который удовлетворяет всем следующим условиям:
    - Первый элемент подмассива является чётным: numbers[l] % 2 == 0;
    - Для всех индексов i в диапазоне [l, r - 1] чётность соседних элементов чередуется: numbers[i] % 2 != numbers[i + 1] % 2;
    - Все элементы подмассива не превышают значение threshold: numbers[i] <= threshold   для всех i в [l, r].

Вернуть целое число - длину наибольшего подмассива, удовлетворяющего указанным условиям.

Примеры:
Ввод: numbers = [3, 2, 5, 4], threshold = 5
Вывод: 3

Ввод: numbers = [1, 2], threshold = 2
Вывод: 1
'''

from typing import List

def longest_alternating_subarray(numbers: List[int], threshold: int) -> int:
    maximum_length = 0
    current_length = 0

    for index in range(len(numbers)):
        current_number = numbers[index]

        if current_number > threshold:
            current_length = 0
            continue

        if current_length == 0:
            if current_number % 2 == 0:
                current_length = 1
                maximum_length = max(maximum_length, current_length)
        else:
            previous_number = numbers[index - 1]

            if (current_number % 2) != (previous_number % 2):
                current_length += 1
                maximum_length = max(maximum_length, current_length)
            else:
                current_length = 1 if current_number % 2 == 0 else 0

    return maximum_length
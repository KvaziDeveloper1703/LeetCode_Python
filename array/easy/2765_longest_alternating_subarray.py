'''
You are given a 0-indexed integer array numbers.

A subarray s of length m is called alternating if it satisfies the following conditions:
    - m > 1;
    - s[1] = s[0] + 1;
    - The differences between consecutive elements alternate between +1 and -1, that is:
        - s[1] - s[0] = 1;
        - s[2] - s[1] = -1;
        - s[3] - s[2] = 1;
        - s[4] - s[3] = -1;
        - and so on, up to s[m - 1] - s[m - 2] = (-1)^m.

In other words, the subarray has the form: [s0, s1, s0, s1, ..., s(m-1)], where s1 = s0 + 1.

Return the maximum length of all alternating subarrays in numbers. If no such subarray exists, return -1.

Examples:
Input: numbers = [2, 3, 4, 3, 4]
Output: 4

Input: numbers = [4, 5, 6]
Output: 2

Дан 0-индексированный массив целых чисел numbers.

Подмассив s длины m называется чередующимся, если выполняются следующие условия:
    - m > 1;
    - s[1] = s[0] + 1;
    - разности между соседними элементами чередуются между +1 и -1, а именно:
        - s[1] - s[0] = 1;
        - s[2] - s[1] = -1;
        - s[3] - s[2] = 1;
        - s[4] - s[3] = -1;
        - и так далее, вплоть до s[m - 1] - s[m - 2] = (-1)^m.

Иными словами, подмассив имеет вид: [s0, s1, s0, s1, ..., s(m-1)], где s1 = s0 + 1.

Необходимо вернуть максимальную длину всех чередующихся подмассивов в массиве numbers. Если ни одного такого подмассива не существует, вернуть -1.

Примеры:
Ввод:numbers = [2, 3, 4, 3, 4]
Вывод: 4

Ввод: numbers = [4, 5, 6]
Вывод: 2
'''

from typing import List

def alternating_subarray(numbers: List[int]) -> int:
    maximum_length = -1
    length_of_numbers = len(numbers)

    for left_index in range(length_of_numbers):
        expected_difference = 1
        right_index = left_index

        while (right_index + 1 < length_of_numbers and numbers[right_index + 1] - numbers[right_index] == expected_difference):
            right_index += 1
            expected_difference *= -1

        current_length = right_index - left_index + 1
        if current_length > 1:
            maximum_length = max(maximum_length, current_length)

    return maximum_length
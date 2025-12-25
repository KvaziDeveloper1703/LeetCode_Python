'''
You are given a 0-indexed integer array numbers of size n.

Define two arrays left_sum and right_sum such that:
    - left_sum[i] is the sum of all elements to the left of index i in the array numbers. If there are no such elements, then left_sum[i] = 0;
    - right_sum[i] is the sum of all elements to the right of index i in the array numbers. If there are no such elements, then right_sum[i] = 0.

Return an integer array answer of size n, where: answer[i] = |left_sum[i] - right_sum[i]|

Examples:
Input: numbers = [10, 4, 8, 3]
Output: [15, 1, 11, 22]

Input: numbers = [1]
Output: [0]

Дан целочисленный массив numbers с нумерацией с нуля размером n.

Определим два массива left_sum и right_sum:
    - left_sum[i] - сумма всех элементов слева от индекса i в массиве numbers. Если таких элементов нет, то left_sum[i] = 0;
    - right_sum[i] - сумма всех элементов справа от индекса i в массиве numbers. Если таких элементов нет, то right_sum[i] = 0.

Верните целочисленный массив answer размером n, где: answer[i] = |left_sum[i] - right_sum[i]|

Примеры:
Ввод: numbers = [10, 4, 8, 3]
Вывод: [15, 1, 11, 22]

Ввод: numbers = [1]
Вывод: [0]
'''

from typing import List

def left_right_difference(numbers: List[int]) -> List[int]:
    total_sum = sum(numbers)
    left_sum = 0
    answer = []

    for number in numbers:
        right_sum = total_sum - left_sum - number
        answer.append(abs(left_sum - right_sum))
        left_sum += number

    return answer
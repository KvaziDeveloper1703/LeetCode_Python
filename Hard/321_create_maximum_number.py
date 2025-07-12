'''
Given two integer arrays numbers_1 and numbers_2 of lengths m and n respectively. These arrays represent the digits of two numbers.
You are also given an integer k.

Create the maximum number of length k (where k ≤ m + n) by selecting digits from the two arrays. The relative order of the digits from the same array must be preserved.

Return an array of k digits representing the answer.

Examples:
Input: numbers_1 = [3,4,6,5], numbers_2 = [9,1,2,5,8,3], k = 5
Output: [9,8,6,5,3]

Input: numbers_1 = [6,7], numbers_2 = [6,0,4], k = 5
Output: [6,7,6,0,4]

Input: numbers_1 = [3,9], numbers_2 = [8,9], k = 3
Output: [9,8,9]

Даны два массива целых чисел numbers_1 и numbers_2 длиной m и n соответственно. Эти массивы представляют собой цифры двух чисел.
Также дано целое число k.

Необходимо составить максимальное число длины k (где k ≤ m + n), выбирая цифры из двух массивов. При этом относительный порядок цифр из одного и того же массива должен сохраняться.

Верните массив из k цифр, представляющий полученное максимальное число.

Примеры:
Ввод: numbers_1 = [3,4,6,5], numbers_2 = [9,1,2,5,8,3], k = 5
Вывод: [9,8,6,5,3]

Ввод: numbers_1 = [6,7], numbers_2 = [6,0,4], k = 5
Вывод: [6,7,6,0,4]

Ввод: numbers_1 = [3,9], numbers_2 = [8,9], k = 3
Вывод: [9,8,9]
'''

from typing import List

def max_number(numbers_1: List[int], numbers_2: List[int], k: int) -> List[int]:

    def pick_max_subsequence(numbers, t):
        stack = []
        drop = len(numbers) - t

        for number in numbers:
            while drop and stack and stack[-1] < number:
                stack.pop()
                drop -= 1
            stack.append(number)
        return stack[:t]

    def merge(sequence_1, sequence_2):
        result = []

        while sequence_1 or sequence_2:
            if sequence_1 > sequence_2:
                result.append(sequence_1.pop(0))
            else:
                result.append(sequence_2.pop(0))
        return result

    max_result = []

    for i in range(max(0, k - len(numbers_2)), min(k, len(numbers_1)) + 1):
        j = k - i
        subsequence_1 = pick_max_subsequence(numbers_1, i)
        subsequence_2 = pick_max_subsequence(numbers_2, j)
        candidate = merge(subsequence_1[:], subsequence_2[:])
        max_result = max(max_result, candidate)

    return max_result
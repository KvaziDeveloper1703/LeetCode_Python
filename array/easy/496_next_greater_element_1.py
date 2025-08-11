'''
The next greater element of an element x in an array is the first element to the right of x in the same array that is greater than x.
You are given two distinct 0-indexed integer arrays numbers_1 and numbers_2, where numbers_1 is a subset of numbers_2.
For each 0 <= i < numbers_1.length, find the index j such that numbers_1[i] == numbers_2[j], and then determine the next greater element for numbers_2[j] in numbers_2. If there is no next greater element, the answer for this query is -1.
Return an array ans of length numbers_1.length where ans[i] is the next greater element as described above.

Examples:
Input: numbers_1 = [4,1,2], numbers_2 = [1,3,4,2]
Output: [-1,3,-1]

Input: numbers_1 = [2,4], numbers_2 = [1,2,3,4]
Output: [3,-1]

Следующим большим элементом для элемента x в массиве называют первый элемент справа от x в том же массиве, который больше x.
Даны два различных целочисленных массива с индексами от 0: numbers_1 и numbers_2, где numbers_1 является подмножеством numbers_2.
Для каждого 0 <= i < numbers_1.length найдите индекс j такой, что numbers_1[i] == numbers_2[j], и определите следующий больший элемент для numbers_2[j] в массиве numbers_2. Если следующего большего элемента нет, ответом для этого запроса будет -1.
Верните массив ans длиной numbers_1.length, где ans[i] — это найденный следующий больший элемент для numbers_1[i].

Примеры:
Ввод: numbers_1 = [4,1,2], numbers_2 = [1,3,4,2]
Вывод: [-1,3,-1]

Ввод: numbers_1 = [2,4], numbers_2 = [1,2,3,4]
Вывод: [3,-1]
'''

from typing import List

def next_greater_element(numbers_1: List[int], numbers_2: List[int]) -> List[int]:
    next_greater = {}
    stack = []

    for number in numbers_2:
        while stack and stack[-1] < number:
            next_greater[stack.pop()] = number
        stack.append(number)

    for number in stack:
        next_greater[number] = -1

    return [next_greater[number] for number in numbers_1]
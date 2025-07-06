'''
You are given an array of integers numbers containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in the array, but it may appear more than once.
Return the repeated number.

Constraints:
    + Do not modify the input array.
    + Use only constant extra space.
    + The time complexity must be less than O(n²).

Examples:
Input: numbers = [1,3,4,2,2]
Output: 2

Input: numbers = [3,1,3,4,2]
Output: 3

Дан массив целых чисел numbers, содержащий n + 1 элемент, где каждый элемент находится в диапазоне от 1 до n включительно.
В массиве ровно одно число повторяется.
Найдите и верните повторяющееся число.

Ограничения:
    + Нельзя изменять массив.
    + Можно использовать только константную дополнительную память.
    + Временная сложность должна быть лучше чем O(n²).

Примеры:
Ввод: numbers = [1,3,4,2,2]
Вывод: 2

Ввод: numbers = [3,1,3,4,2]
Вывод: 3
'''

from typing import List

def findDuplicate(numbers: List[int]) -> int:
    slow = numbers[0]
    fast = numbers[0]
    while True:
        slow = numbers[slow]
        fast = numbers[numbers[fast]]
        if slow == fast:
            break
    slow = numbers[0]
    while slow != fast:
        slow = numbers[slow]
        fast = numbers[fast]
    
    return slow
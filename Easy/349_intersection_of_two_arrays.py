'''
Given two integer arrays numbers_1 and numbers_2, return an array of their intersection.
Each element in the result must be unique, and you can return the result in any order.

Examples:
Input: numbers_1 = [1,2,2,1], numbers_2 = [2,2]
Output: [2]

Input: numbers_1 = [4,9,5], numbers_2 = [9,4,9,8,4]
Output: [9,4]

Даны два массива целых чисел numbers_1 и numbers_2. Верни массив их пересечения.
Каждый элемент в результате должен быть уникальным, и порядок элементов может быть любым.

Примеры:
Ввод: numbers_1 = [1,2,2,1], numbers_2 = [2,2]
Вывод: [2]

Ввод: numbers_1 = [4,9,5], numbers_2 = [9,4,9,8,4]
Вывод: [9,4]
'''

def intersection(numbers_1: List[int], numbers_2: List[int]) -> List[int]:
    result = []
    for number in numbers_1:
        if number in numbers_2 and number not in result:
            result.append(number)
    return result
'''
Given two integer arrays numbers_1 and numbers_2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays.
You may return the result in any order.

Examples:
Input: numbers_1 = [1,2,2,1], numbers_2 = [2,2]
Output: [2,2]

Input: numbers_1 = [4,9,5], numbers_2 = [9,4,9,8,4]
Output: [4,9]

Даны два массива целых чисел numbers_1 и numbers_2. Верни массив их пересечения.
Каждый элемент в результате должен встречаться столько раз, сколько он встречается в обоих массивах.
Порядок элементов в ответе может быть любым.

Примеры:
Ввод: numbers_1 = [1,2,2,1], numbers_2 = [2,2]
Вывод: [2,2]

Ввод: numbers_1 = [4,9,5], numbers_2 = [9,4,9,8,4]
Вывод: [4,9]
'''

def intersect(numbers_1: List[int], numbers_2: List[int]) -> List[int]:
    result = []
    counts = {}

    for number in numbers_1:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    for number in numbers_2:
        if number in counts and counts[number] > 0:
            result.append(number)
            counts[number] -= 1

    return result
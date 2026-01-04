'''
You are given a 0-indexed 2D integer array numbers, where each element represents the position of a car parked on a number line.

For each index i, numbers[i] = [startᵢ, endᵢ], where:
    - startᵢ is the starting point of the i-th car,
    - endᵢ is the ending point of the i-th car.

A car occupies all integer points from startᵢ to endᵢ inclusive.

Your task is to return the number of distinct integer points on the number line that are covered by at least one car.

Examples:
Input: numbers = [[3,6],[1,5],[4,7]]
Output: 7

Input: numbers = [[1,3],[5,8]]
Output: 7

Вам дан двумерный массив целых чисел с нумерацией от нуля numbers, где каждый элемент описывает положение автомобиля, припаркованного на числовой прямой.

Для каждого индекса i: numbers[i] = [startᵢ, endᵢ], где:
    - startᵢ - начальная точка i-го автомобиля,
    - endᵢ - конечная точка i-го автомобиля.

Автомобиль занимает все целочисленные точки на отрезке от startᵢ до endᵢ включительно.

Необходимо вернуть количество различных целых точек на числовой прямой, которые покрыты хотя бы одним автомобилем.

Примеры:
Ввод: numbers = [[3,6],[1,5],[4,7]]
Вывод: 7

Ввод: numbers = [[1,3],[5,8]]
Вывод: 7
'''

def number_of_points(numbers: list[list[int]]) -> int:
    covered_points = set()

    for start, end in numbers:
        for point in range(start, end + 1):
            covered_points.add(point)

    return len(covered_points)
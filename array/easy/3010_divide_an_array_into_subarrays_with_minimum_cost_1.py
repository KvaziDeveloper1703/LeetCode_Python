'''
You are given an integer array numbers of length n.
The cost of a subarray is defined as the value of its first element.
You must divide the array numbers into three disjoint contiguous subarrays.
Return the minimum possible sum of the costs of these three subarrays.

Examples:
Input: numbers = [1, 2, 3, 12]
Output: 6

Input: numbers = [5, 4, 3]
Output: 12

Вам дан массив целых чисел numbers длины n.
Стоимость подмассива определяется как значение его первого элемента.
Необходимо разбить массив numbers на три непересекающихся непрерывных подмассива.
Верните минимально возможную сумму стоимостей этих трёх подмассивов.

Примеры:
Ввод: numbers = [1, 2, 3, 12]
Вывод: 6

Ввод: numbers = [5, 4, 3]
Вывод: 12
'''

def minimum_cost(numbers: list[int]) -> int:
    n = len(numbers)
    answer = float('inf')

    for i in range(1, n - 1):
        for j in range(i + 1, n):
            answer = min(answer, numbers[0] + numbers[i] + numbers[j])

    return answer
'''
Given an array numbers of n integers, return an array of all the unique quadruplets [numbers[a], numbers[b], numbers[c], numbers[d]] such that:
    + 0 <= a, b, c, d < n;
    + a, b, c, and d are distinct;
    + numbers[a] + numbers[b] + numbers[c] + numbers[d] == target.

You may return the answer in any order.

Example:
Input: numbers = [1, 0, -1, 0, -2, 2], target = 0
Output: [   [-2, -1, 1, 2], 
            [-2, 0, 0, 2], 
            [-1, 0, 0, 1]
    ]

Дан массив целых чисел numbers длиной n. Необходимо вернуть все уникальные кортежи [numbers[a], numbers[b], numbers[c], numbers[d]] такие, что:
    + 0 <= a, b, c, d < n;
    + a, b, c и d — различные индексы;
    + numbers[a] + numbers[b] + numbers[c] + numbers[d] == target.

Ответ можно вернуть в любом порядке.

Пример:
Ввод: numbers = [1, 0, -1, 0, -2, 2], target = 0
Вывод: [[-2, -1, 1, 2], 
        [-2, 0, 0, 2], 
        [-1, 0, 0, 1]
    ]
'''

def four_sum(numbers: list[int], target: int) -> list[list[int]]:
    numbers.sort()
    result = []
    n = len(numbers)

    for i in range(n - 3):
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and numbers[j] == numbers[j - 1]:
                continue

            left, right = j + 1, n - 1
            while left < right:
                current_sum = numbers[i] + numbers[j] + numbers[left] + numbers[right]

                if current_sum == target:
                    result.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                    while left < right and numbers[left] == numbers[left + 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return result
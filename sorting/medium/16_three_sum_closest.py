'''
Given an integer array numbers of length n and an integer target, find three integers in numbers such that their sum is closest to target.
Return the sum of the three integers.

Example:
Input: numbers = [-1, 2, 1, -4], target = 1
Output: 2

Дан массив целых чисел numbers длиной n и целое число target. Необходимо найти три числа в массиве, сумма которых наиболее близка к числу target.
Верните сумму этих трёх чисел.

Пример:
Ввод: numbers = [-1, 2, 1, -4], target = 1
Вывод: 2
'''

def three_sum_closest(numbers: list[int], target: int) -> int:
    numbers.sort()
    closest_sum = numbers[0] + numbers[1] + numbers[2]

    for i in range(len(numbers) - 2):
        left, right = i + 1, len(numbers) - 1
        while left < right:
            current_sum = numbers[i] + numbers[left] + numbers[right]
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum
    return closest_sum
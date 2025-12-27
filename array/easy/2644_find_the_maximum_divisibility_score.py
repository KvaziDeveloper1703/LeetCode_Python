'''
You are given two integer arrays numbers and divisors.

For each element divisors[i], define its divisibility score as the number of indices j such that numbers[j] is divisible by divisors[i].

Return the integer from the divisors array that has the maximum divisibility score.

If multiple integers have the same maximum score, return the smallest such integer.

Examples:
Input: numbers = [2, 9, 15, 50], divisors = [5, 3, 7, 2]
Output: 2

Input: numbers = [4, 7, 9, 3, 9], divisors = [5, 2, 3]
Output: 3

Даны два массива целых чисел: numbers и divisors.

Для каждого элемента divisors[i] определим оценку делимости как количество индексов j, для которых numbers[j] делится на divisors[i] без остатка.

Необходимо вернуть элемент массива divisors, имеющий максимальную оценку делимости.

Если несколько элементов имеют одинаковую максимальную оценку, верните наименьший из них.

Примеры:
Ввод: numbers = [2, 9, 15, 50], divisors = [5, 3, 7, 2]
Вывод: 2

Ввод: numbers = [4, 7, 9, 3, 9], divisors = [5, 2, 3]
Вывод: 3
'''

from typing import List

def max_div_score(numbers: List[int], divisors: List[int]) -> int:
    maximum_divisibility_score = -1
    best_divisor = None

    for current_divisor in divisors:
        current_score = 0

        for number in numbers:
            if number % current_divisor == 0:
                current_score += 1

        if (current_score > maximum_divisibility_score or (current_score == maximum_divisibility_score and (best_divisor is None or current_divisor < best_divisor))):
            maximum_divisibility_score = current_score
            best_divisor = current_divisor

    return best_divisor
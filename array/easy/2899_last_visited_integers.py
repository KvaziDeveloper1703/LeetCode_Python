'''
You are given an integer array numbers, where each element numbers[i] is either a positive integer or -1.

For every occurrence of -1, you need to determine the corresponding last visited integer.

To do this, define two initially empty arrays: seen and ans.

Iterate through the array numbers from left to right and apply the following rules:
    - If a positive integer is encountered, prepend it to the front of the array seen;
    - If -1 is encountered:
        - Let k be the number of consecutive -1s encountered so far;
        - If k is less than or equal to the length of seen, append the k-th element of seen to ans;
        - If k is greater than the length of seen, append -1 to ans.

After processing all elements, return the array ans.

Examples:
Input: numbers = [1,2,-1,-1,-1]
Output: [2,1,-1]

Input: numbers = [1,-1,2,-1,-1]
Output: [1,2,1]

Вам дан массив целых чисел numbers, где каждый элемент numbers[i] — это либо положительное целое число, либо -1.

Для каждого вхождения -1 необходимо определить соответствующее последнее посещённое число.

Для этого определим два изначально пустых массива: seen и ans.

Проходите массив numbers слева направо и применяйте следующие правила:
    - Если встречается положительное число, добавьте его в начало массива seen;
    - Если встречается -1:
        - Пусть k - количество последовательных -1, встреченных к текущему моменту;
        - Если k меньше либо равно длине массива seen, добавьте в ans k-й элемент массива seen;
        - Если k больше длины массива seen, добавьте в ans значение -1.

После обработки всего массива верните массив ans.

Примеры:
Ввод: numbers = [1,2,-1,-1,-1]
Вывод: [2,1,-1]

Ввод: numbers = [1,-1,2,-1,-1]
Вывод: [1,2,1]
'''

from typing import List

def last_visited_integers(numbers: List[int]) -> List[int]:
    seen = []
    result = []
    consecutive_minus_ones = 0

    for current_value in numbers:
        if current_value != -1:
            seen.insert(0, current_value)
            consecutive_minus_ones = 0
        else:
            consecutive_minus_ones += 1
            if consecutive_minus_ones <= len(seen):
                result.append(seen[consecutive_minus_ones - 1])
            else:
                result.append(-1)

    return result
'''
In the town of Digitville, there was a list of numbers called numbers, containing integers from 0 to n - 1.
Each number was supposed to appear exactly once, but two mischievous numbers appeared one extra time, making the array longer than expected.

Your task is to find these two sneaky numbers.

Return an array of size 2 containing the two numbers.

Examples:
Input: numbers = [0, 1, 1, 0]
Output: [0, 1]

Input: numbers = [0, 3, 2, 1, 3, 2]
Output: [2, 3]

В городе Digitville был список чисел numbers, который должен был содержать все целые числа от 0 до n - 1.
Каждое число должно было встречаться ровно один раз, но два «хитрых» числа повторились ещё один раз, из-за чего массив стал длиннее, чем должен был быть.

Ваша задача - найти эти два повторяющихся числа.

Верните массив размера 2, содержащий эти два числа.

Примеры:
Ввод: numbers = [0, 1, 1, 0]
Вывод: [0, 1]

Ввод: numbers = [0, 3, 2, 1, 3, 2]
Вывод: [2, 3]
'''

from typing import List
from collections import Counter

def get_sneaky_numbers(numbers: List[int]) -> List[int]:
    count = Counter(numbers)
    result = []

    for number, freq in count.items():
        if freq == 2:
            result.append(number)

    return result
'''
You are given a 0-indexed circular array of strings words and a string target.

A circular array means that the last element is connected to the first one.

Formally:
    - The next element of words[i] is words[(i + 1) % n];
    - The previous element of words[i] is words[(i - 1 + n) % n] where n is the length of the array words.

Starting from startIndex, you can move to either:
    - the next word, or
    - the previous word,
    - moving one step at a time.

Your task is to return the minimum number of steps required to reach a word equal to target.

If the string target does not exist in the array words, return -1.

Examples:
Input: words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
Output: 1

Input: words = ["a","b","leetcode"], target = "leetcode", startIndex = 0
Output: 1

Дан циклический массив строк words, индексированный с нуля, и строка target.

Циклический массив означает, что конец массива соединён с его началом.

Формально:
    - Следующий элемент после words[i] - это words[(i + 1) % n];
    - Предыдущий элемент перед words[i] - это words[(i - 1 + n) % n], где n - длина массива words.

Начиная с позиции startIndex, за один шаг можно:
    - перейти к следующему слову, либо
    - перейти к предыдущему слову.

Необходимо найти минимальное количество шагов, чтобы добраться до строки, равной target.

Если строки target нет в массиве words, верните -1.

Примеры:
Ввод: words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
Вывод: 1

Ввод: words = ["a","b","leetcode"], target = "leetcode", startIndex = 0
Вывод: 1
'''

from typing import List

def closest_target(words: List[str], target: str, startIndex: int) -> int:
    array_length = len(words)
    minimum_distance = float("inf")

    for index, word in enumerate(words):
        if word == target:
            clockwise_distance = (index - startIndex) % array_length
            counterclockwise_distance = (startIndex - index) % array_length
            minimum_distance = min(
                minimum_distance,
                clockwise_distance,
                counterclockwise_distance
            )

    if minimum_distance == float("inf"):
        return -1

    return minimum_distance
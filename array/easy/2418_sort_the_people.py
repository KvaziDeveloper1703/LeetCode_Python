'''
You are given an array of strings names and an array of integers heights.

The array heights contains distinct positive integers, and both arrays have the same length n.

For each index i, names[i] represents the name of the i-th person, and heights[i] represents their height.

Your task is to return the array names, sorted in descending order based on the corresponding values in heights.

Examples:
Input: names = ["Mary", "John", "Emma"], heights = [180, 165, 170]
Output: ["Mary", "Emma", "John"]

Input: names = ["Alice", "Bob", "Bob"], heights = [155, 185, 150]
Output: ["Bob", "Alice", "Bob"]

Вам даны массив строк names и массив целых чисел heights.

Массив heights содержит различные положительные числа, и оба массива имеют одинаковую длину n.

Для каждого индекса i:
    - names[i] - имя i-го человека,
    - heights[i] - его рост.

Необходимо вернуть массив names, отсортированный по убыванию роста соответствующих людей.

Примеры:
Ввод: names = ["Mary", "John", "Emma"], heights = [180, 165, 170]
Вывод: ["Mary", "Emma", "John"]

Ввод: names = ["Alice", "Bob", "Bob"], heights = [155, 185, 150]
Вывод: ["Bob", "Alice", "Bob"]
'''

from typing import List

def sort_people(names: List[str], heights: List[int]) -> List[str]:
    people = []

    for index in range(len(names)):
        height = heights[index]
        name = names[index]
        people.append((height, name))

    people.sort(key=lambda person: person[0], reverse=True)

    sorted_names = []

    for person in people:
        sorted_names.append(person[1])

    return sorted_names
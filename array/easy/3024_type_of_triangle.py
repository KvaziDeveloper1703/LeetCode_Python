'''
You are given a 0-indexed integer array numbers of length 3, where each element represents the length of a side.

Determine whether these three values can form a valid triangle. If they cannot, return "none".

If a triangle can be formed, classify it according to the following definitions:
    - Equilateral - all three sides have equal length;
    - Isosceles - exactly two sides have equal length;
    - Scalene - all three sides have different lengths.

Return a string representing the type of triangle that can be formed.

Examples:
Input: numbers = [3, 3, 3]
Output: "equilateral"

Input: numbers = [3, 4, 5]
Output: "scalene"

Вам дан целочисленный массив numbers с индексацией от 0, состоящий из трёх элементов, каждый из которых представляет длину стороны.

Необходимо определить, могут ли эти три значения образовать корректный треугольник. Если нет — вернуть строку "none".

Если треугольник можно построить, классифицируйте его следующим образом:
    - Равносторонний - все три стороны равны;
    - Равнобедренный - ровно две стороны равны;
    - Разносторонний - все стороны имеют разную длину.

Верните строку, обозначающую тип треугольника.

Примеры:
Ввод: numbers = [3, 3, 3]
Вывод: "equilateral"

Ввод: numbers = [3, 4, 5]
Вывод: "scalene"
'''

from typing import List

def triangle_type(numbers: List[int]) -> str:
    a, b, c = sorted(numbers)

    if a + b <= c:
        return "none"

    if a == b == c:
        return "equilateral"
    elif a == b or b == c:
        return "isosceles"
    else:
        return "scalene"
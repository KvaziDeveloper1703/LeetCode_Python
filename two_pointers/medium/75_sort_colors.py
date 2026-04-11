'''
You are given an array numbers with n objects colored red, white, or blue, represented by integers:
    + 0 for red,
    + 1 for white,
    + 2 for blue.

Sort the array in-place so that objects of the same color are adjacent, with the colors in the order: red, white, then blue. You must not use the library's sort function.

Дан массив numbers, содержащий n элементов, каждый из которых обозначает цвет: красный, белый или синий. Цвета представлены числами:
    + 0 — красный,
    + 1 — белый,
    + 2 — синий.

Отсортируйте массив на месте так, чтобы одинаковые цвета шли рядом, а порядок цветов был: красный, затем белый, затем синий. Нельзя использовать встроенные функции сортировки.
'''

from typing import List

def sort_colors(numbers: List[int]) -> None:
    low, mid, high = 0, 0, len(numbers) - 1

    while mid <= high:
        if numbers[mid] == 0:
            numbers[low], numbers[mid] = numbers[mid], numbers[low]
            low += 1
            mid += 1
        elif numbers[mid] == 1:
            mid += 1
        else:
            numbers[mid], numbers[high] = numbers[high], numbers[mid]
            high -= 1
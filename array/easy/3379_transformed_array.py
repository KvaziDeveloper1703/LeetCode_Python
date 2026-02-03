'''
You are given an integer array numbers that represents a circular array. Your task is to create a new array result of the same length.

For each index i, do the following independently:
    - If numbers[i] > 0:
        - Start at index i and move numbers[i] steps to the right in the circular array;
        - Set result[i] to the value at the position where you land.

    - If numbers[i] < 0:
        - Start at index i and move |numbers[i]| steps to the left in the circular array;
        - Set result[i] to the value at the position where you land.

    - If numbers[i] = 0:
        - Set result[i] = numbers[i].

Return the array result.

Examples:
Input: numbers = [3, -2, 1, 1]
Output: [1, 1, 1, 3]

Input: numbers = [-1, 4, -1]
Output: [-1, -1, 4]

Дан массив целых чисел numbers, который является циклическим (circular). Нужно создать новый массив result той же длины.

Для каждого индекса i выполняются независимые действия:
    - Если numbers[i] > 0:
        - Начните с индекса i и сделайте numbers[i] шагов вправо по циклическому массиву;
        - Запишите в result[i] значение элемента, на котором вы остановились.

    - Если numbers[i] < 0:
        - Начните с индекса i и сделайте |numbers[i]| шагов влево по циклическому массиву;
        - Запишите в result[i] значение элемента, на котором вы остановились.

    - Если numbers[i] = 0:
        - Тогда result[i] = numbers[i].

Верните массив result.

Примеры:
Ввод: numbers = [3, -2, 1, 1]
Вывод: [1, 1, 1, 3]

Ввод: numbers = [-1, 4, -1]
Вывод: [-1, -1, 4]
'''

from typing import List

def construct_transformed_array(numbers: List[int]) -> List[int]:
    array_length = len(numbers)
    result = [0] * array_length

    for index in range(array_length):
        step = numbers[index]

        if step == 0:
            result[index] = 0
        else:
            new_index = (index + step) % array_length
            result[index] = numbers[new_index]

    return result
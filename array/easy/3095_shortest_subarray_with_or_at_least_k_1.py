'''
You are given an array numbers consisting of non-negative integers and an integer k.
A subarray is called special if the bitwise OR of all its elements is greater than or equal to k.
Return the length of the shortest special non-empty subarray of numbers.
If no such subarray exists, return -1.

Дан массив numbers, состоящий из неотрицательных целых чисел, и целое число k.
Подмассив называется особым, если побитовое ИЛИ (OR) всех его элементов не меньше k.
Нужно вернуть длину самого короткого непустого особого подмассива массива numbers.
Если такого подмассива не существует - вернуть -1.
'''

from typing import List

def minimum_subarray_length(numbers: List[int], k: int) -> int:
    array_length = len(numbers)

    if k == 0:
        return 1

    bit_counters = [0] * 32

    def add_number_to_window(number: int) -> None:
        for bit_index in range(32):
            if number & (1 << bit_index):
                bit_counters[bit_index] += 1

    def remove_number_from_window(number: int) -> None:
        for bit_index in range(32):
            if number & (1 << bit_index):
                bit_counters[bit_index] -= 1

    def calculate_window_or_value() -> int:
        window_or_value = 0
        for bit_index in range(32):
            if bit_counters[bit_index] > 0:
                window_or_value |= (1 << bit_index)
        return window_or_value

    minimum_length = float("inf")
    left_pointer = 0

    for right_pointer in range(array_length):
        add_number_to_window(numbers[right_pointer])

        while left_pointer <= right_pointer and calculate_window_or_value() >= k:
            current_window_length = right_pointer - left_pointer + 1
            minimum_length = min(minimum_length, current_window_length)

            remove_number_from_window(numbers[left_pointer])
            left_pointer += 1

    return minimum_length if minimum_length != float("inf") else -1
'''
There is a hidden integer array my_array that contains n non-negative integers.

This array was encoded into another array encoded of length n-1, where: encoded[i] = my_array[i]XORarray[i+1]

For example, if my_array = [1, 0, 2, 1], then encoded = [1, 2, 3].

You are given the array encoded, and an integer first, which represents the first element of the original array: my_array[0]=first

Your task is to reconstruct the original array my_array.

It can be shown that the answer always exists and is unique.

Существует скрытый целочисленный массив my_array, состоящий из n неотрицательных чисел.

Этот массив был закодирован в другой массив encoded длины n−1, где выполняется правило: encoded[i] = my_array[i] XOR my_array[i+1].

Например, если my_array = [1, 0, 2, 1], то encoded = [1, 2, 3].

Вам дан массив encoded, а также целое число first, которое является первым элементом исходного массива: my_array[0] = first.

Ваша задача - восстановить исходный массив my_array.

Гарантируется, что решение существует и является единственным.
'''

from typing import List

def decode(encoded: List[int], first: int) -> List[int]:
    my_array = [first]
    for value in encoded:
        my_array.append(my_array[-1] ^ value)
    return my_array
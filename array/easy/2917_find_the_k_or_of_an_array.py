'''
You are given an integer array numbers and an integer k.

Let us define the K-or operation as an extension of the standard bitwise OR operation.

In K-or, a bit position in the result is set to 1 if at least k numbers in the array numbers have a 1 in that bit position.

Your task is to return the K-or of the array numbers.

Examples:
Input: numbers = [7, 12, 9, 8, 9, 15], k = 4
Output: 9

Input: numbers = [2, 12, 1, 11, 4, 5], k = 6
Output: 0

Дан целочисленный массив numbers и целое число k.

Введём операцию K-or, которая является расширением стандартной побитовой операции OR.

В операции K-or бит в результирующем числе устанавливается в 1, если как минимум k чисел из массива numbers имеют значение 1 в этом битовом разряде.

Необходимо вернуть результат операции K-or для массива numbers.

Примеры:
Ввод: numbers = [7, 12, 9, 8, 9, 15], k = 4
Вывод: 9

Ввод: numbers = [2, 12, 1, 11, 4, 5], k = 6
Вывод: 0
'''

from typing import List

def find_k_or(numbers: List[int], k: int) -> int:
    result = 0

    for bit_position in range(32):
        count_with_bit = 0

        for number in numbers:
            if (number >> bit_position) & 1:
                count_with_bit += 1

        if count_with_bit >= k:
            result |= (1 << bit_position)

    return result
'''
You are given a 0-indexed array numbers of length n that contains distinct positive integers.

A right shift operation moves each element at index i to index (i + 1) % n.

Your task is to return the minimum number of right shifts required to sort the array numbers in strictly increasing order.

If it is not possible to sort the array using only right shifts, return -1.

Examples:
Input: numbers = [3,4,5,1,2]
Output: 2

Input: numbers = [1,3,5]
Output: 0

Вам дан массив положительных целых чисел с нумерацией от нуля numbers длины n, содержащий различные элементы.

Операция сдвига вправо определяется следующим образом: каждый элемент с индексом i перемещается на позицию (i + 1) % n.

Необходимо вернуть минимальное количество сдвигов вправо, необходимых для сортировки массива numbers по возрастанию.

Если отсортировать массив, используя только сдвиги вправо, невозможно, верните -1.

Примеры:
Ввод: numbers = [3,4,5,1,2]
Вывод: 2

Ввод: numbers = [1,3,5]
Вывод: 0
'''

def minimum_right_shifts(numbers: list[int]) -> int:
    length = len(numbers)
    sorted_numbers = sorted(numbers)

    if numbers == sorted_numbers:
        return 0

    for shifts in range(1, length + 1):
        numbers = [numbers[-1]] + numbers[:-1]
        if numbers == sorted_numbers:
            return shifts

    return -1
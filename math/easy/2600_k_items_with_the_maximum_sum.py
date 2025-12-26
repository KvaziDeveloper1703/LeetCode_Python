'''
There is a bag that contains items. Each item has a number written on it: 1, 0, or -1.

You are given four non-negative integers:
    - number_of_ones
    - number_of_zeros
    - number_of_negative_ones
    - number_of_items_to_pick

Initially, the bag contains:
    - number_of_ones items with value 1,
    - number_of_zeros items with value 0,
    - number_of_negative_ones items with value -1.

You must select exactly number_of_items_to_pick items from the bag.

Return the maximum possible sum of the numbers written on the selected items.

Examples:
Input: number_of_ones = 3, number_of_zeros = 2, number_of_negative_ones = 0, number_of_items_to_pick = 2
Output: 2

Input: number_of_ones = 3, number_of_zeros = 2, number_of_negative_ones = 0, number_of_items_to_pick = 4
Output: 3

Есть мешок с предметами. На каждом предмете записано одно из чисел: 1, 0 или -1.

Даны четыре неотрицательных целых числа:
    - number_of_ones
    - number_of_zeros
    - number_of_negative_ones
    - number_of_items_to_pick

Изначально в мешке находится:
    - number_of_ones предметов со значением 1,
    - number_of_zeros предметов со значением 0,
    - number_of_negative_ones предметов со значением -1.

Необходимо выбрать ровно number_of_items_to_pick предметов из мешка.

Верните максимально возможную сумму чисел, записанных на выбранных предметах.

Примеры:
Ввод: number_of_ones = 3, number_of_zeros = 2, number_of_negative_ones = 0, number_of_items_to_pick = 2
Вывод: 2

Ввод: number_of_ones = 3, number_of_zeros = 2, number_of_negative_ones = 0, number_of_items_to_pick = 4
Вывод: 3
'''

def k_items_with_maximum_sum(number_of_ones: int, number_of_zeros: int, number_of_negative_ones: int, number_of_items_to_pick: int) -> int:
    taken_ones = min(number_of_ones, number_of_items_to_pick)
    number_of_items_to_pick -= taken_ones

    taken_zeros = min(number_of_zeros, number_of_items_to_pick)
    number_of_items_to_pick -= taken_zeros

    taken_negative_ones = min(number_of_negative_ones, number_of_items_to_pick)

    return taken_ones - taken_negative_ones
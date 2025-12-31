'''
You are given a 0-indexed permutation of n integers called numbers.

A permutation is called semi-ordered if:
    - the first element equals 1, and
    - the last element equals n.

You are allowed to perform the following operation any number of times:
    - Choose two adjacent elements in numbers and swap them.

Your task is to make numbers a semi-ordered permutation using the minimum number of operations.

Return the minimum number of operations required.

A permutation is a sequence of integers from 1 to n of length n, where each number appears exactly once.

Examples:
Input: numbers = [2,1,4,3]
Output: 2

Input: numbers = [2,4,1,3]
Output: 3

Дана 0-индексированная перестановка из n целых чисел numbers.

Перестановка называется полуупорядоченной, если:
    - первый элемент равен 1, и
    - последний элемент равен n.

Вы можете выполнять следующую операцию неограниченное количество раз:
    - Выберите два соседних элемента в массиве numbers и поменяйте их местами.

Необходимо привести numbers к полуупорядоченной перестановке, используя минимальное количество операций.

Верните минимальное число операций, необходимое для этого.

Перестановка - это последовательность чисел от 1 до n длины n, в которой каждое число встречается ровно один раз.

Примеры:
Ввод: numbers = [2,1,4,3]
Вывод: 2

Ввод: numbers = [2,4,1,3]
Вывод: 3
'''

from typing import List

def semi_ordered_permutation(numbers: List[int]) -> int:
    length = len(numbers)

    position_of_one = numbers.index(1)
    position_of_last = numbers.index(length)

    operations_count = (
        position_of_one +
        (length - 1 - position_of_last)
    )

    if position_of_one > position_of_last:
        operations_count -= 1

    return operations_count
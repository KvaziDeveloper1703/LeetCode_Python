'''
You are given an integer n.

A 0-indexed integer array numbers of length n + 1 is generated using the following rules:
- numbers[0] = 0;
- numbers[1] = 1'
- numbers[2 * i] = numbers[i], when 2 <= 2 * i <= n;
- numbers[2 * i + 1] = numbers[i] + numbers[i + 1], when 2 <= 2 * i + 1 <= n.

Return the maximum integer in the array numbers.

Examples:
Input: n = 7
Output: 3

Input: n = 2
Output: 1

Дано целое число n.

Создаётся массив целых чисел numbers длиной n + 1, по следующим правилам:
- numbers[0] = 0;
- numbers[1] = 1;
- numbers[2 * i] = numbers[i], если 2 <= 2 * i <= n;
- numbers[2 * i + 1] = numbers[i] + numbers[i + 1], если 2 <= 2 * i + 1 <= n.

Нужно вернуть максимальное число в массиве numbers.

Примеры:
Ввод: n = 7
Вывод: 3

Ввод: n = 2
Вывод: 1
'''

def get_maximum_generated(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    numbers = [0] * (n + 1)
    numbers[1] = 1

    for i in range(1, n // 2 + 1):
        if 2 * i <= n:
            numbers[2 * i] = numbers[i]
        if 2 * i + 1 <= n:
            numbers[2 * i + 1] = numbers[i] + numbers[i + 1]

    return max(numbers)
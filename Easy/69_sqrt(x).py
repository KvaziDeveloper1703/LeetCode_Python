'''
Given a non-negative integer n, return the square root of n, rounded down to the nearest integer. The result must also be non-negative.

Example:
Input: n = 4
Output: 2

Дано неотрицательное целое число n. Требуется вернуть квадратный корень из n, округлённый вниз до ближайшего целого. Результат должен быть также неотрицательным.

Пример:
Ввод: n = 4
Вывод: 2
'''

def sqrt(n: int) -> int:
    if n < 2:
        return n
    
    left = 1
    right = n // 2
    
    while left <= right:
        middle = (left + right) // 2
        square = middle * middle
        if square == n:
            return middle
        elif square < n:
            left = middle + 1
        else:
            right = middle - 1
    
    return right
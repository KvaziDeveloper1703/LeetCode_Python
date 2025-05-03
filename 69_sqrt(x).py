'''
Given a non-negative integer x, return the square root of x, rounded down to the nearest integer. The result must also be non-negative.

Example:
Input: x = 4
Output: 2

Дано неотрицательное целое число x. Требуется вернуть квадратный корень из x, округлённый вниз до ближайшего целого. Результат должен быть также неотрицательным.

Пример:
Ввод: x = 4
Вывод: 2
'''

def my_sqrt(x: int) -> int:
    if x < 2:
        return x
    
    left = 1
    right = x // 2
    
    while left <= right:
        middle = (left + right) // 2
        square = middle * middle
        if square == x:
            return middle
        elif square < x:
            left = middle + 1
        else:
            right = middle - 1
    
    return right
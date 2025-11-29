'''
Reversing an integer means writing its digits in reverse order.

Return True if reversed2 is equal to numbers; otherwise, return False.

Examples:
Input: numbers = 526
Output: True

Input: numbers = 1800
Output: False

Переворот числа означает запись его цифр в обратном порядке.

Верните True, если reversed2 равно numbers; иначе верните False.

Примеры:
Ввод: numbers = 526
Вывод: True

Ввод: numbers = 1800
Вывод: False
'''

def is_same_after_reversals(numbers: int) -> bool:
    if numbers == 0:
        return True
    return numbers % 10 != 0
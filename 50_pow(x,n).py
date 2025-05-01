'''
Implement pow(x, n), which calculates x raised to the power n.

Example:
Input: x = 2.00000, n = 10
Output: 1024.00000

Реализуй функцию pow(x, n), которая вычисляет x в степени n.

Пример:
Ввод: x = 2.00000, n = 10
Вывод: 1024.00000
'''

def my_pow(base: float, exponent: int) -> float:
    def fast_power(base_value, exponent_value):
        if exponent_value == 0:
            return 1.0
        half_result = fast_power(base_value, exponent_value // 2)
        if exponent_value % 2 == 0:
            return half_result * half_result
        else:
            return half_result * half_result * base_value
    
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    
    return fast_power(base, exponent)
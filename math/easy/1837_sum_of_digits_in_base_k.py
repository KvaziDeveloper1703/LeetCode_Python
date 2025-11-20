'''
You are given an integer n and a base k.
Convert n from base 10 to base k, then return the sum of its digits in base 10.

After conversion, each digit of the number in base k should be treated as a normal base-10 integer when summing.

Examples:
Input: n = 34, k = 6
Output: 9

Input: n = 10, k = 10
Output: 1

Дано число n в десятичной системе счисления и основание k.
Нужно перевести число n из десятичной системы в систему с основанием k, а затем вернуть сумму его цифр.

После перевода каждую цифру числа в системе k нужно рассматривать как обычное десятичное число при сложении.

Примеры:
Ввод: n = 34, k = 6
Вывод: 9

Ввод: n = 10, k = 10
Вывод: 1
'''

def sum_base(n: int, k: int) -> int:
    digit_sum = 0

    while n > 0:
        digit_sum += n % k
        n //= k
    
    return digit_sum
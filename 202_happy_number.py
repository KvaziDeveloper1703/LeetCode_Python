'''
Write an algorithm to determine if a number n is a happy number.
A happy number is defined by the following process:
+ Starting with any positive integer, replace the number by the sum of the squares of its digits;
+ Repeat the process until the number equals 1, or it loops endlessly in a cycle which does not include 1;
+ Numbers that end in 1 are happy, while numbers that fall into a cycle (not including 1) are not.

Return true if n is a happy number, and false if not.

Examples:
Input: n = 19
Output: true

Input: n = 2
Output: false

Напишите алгоритм, который определяет, является ли число n счастливым числом.
Счастливое число определяется следующим образом:
+ Начав с любого положительного целого числа, заменяйте его суммой квадратов его цифр;
+ Повторяйте процесс до тех пор, пока число не станет равным 1, или пока процесс не начнёт бесконечно повторяться в цикле, который не содержит 1;
+ Числа, которые в итоге становятся 1, считаются счастливыми;
+ Числа, попадающие в цикл без единицы — не являются счастливыми.

Верните true, если n — счастливое число, и false — если нет.

Примеры:
Ввод: n = 19
Вывод: true

Ввод: n = 2
Вывод: false
'''

def is_happy(number: int) -> bool:
    def get_sum_of_squares(num: int) -> int:
        return sum(int(digit) ** 2 for digit in str(num))

    seen_numbers = set()

    while number != 1:
        number = get_sum_of_squares(number)

        if number in seen_numbers:
            return False

        seen_numbers.add(number)

    return True
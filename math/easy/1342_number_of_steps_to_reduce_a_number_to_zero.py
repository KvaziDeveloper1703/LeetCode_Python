"""
Given an integer number, return the number of steps required to reduce it to zero.

You must follow these rules:
    + If the current number is even, divide it by 2;
    + If the current number is odd, subtract 1 from it.

Repeat the process until the number becomes 0, and return the total number of steps taken.

Examples:
Input: number = 14
Output: 6

Input: number = 8
Output: 4

Дано целое число number. Необходимо вернуть количество шагов, необходимых для того, чтобы уменьшить его до нуля, следуя следующим правилам:
    + Если текущее число чётное, разделите его на 2;
    + Если текущее число нечётное, вычтите из него 1.

Повторяйте процесс, пока число не станет равно 0, и верните общее количество выполненных шагов.

Примеры:
Ввод: number = 14
Вывод: 6

Ввод: number = 8
Вывод: 4
"""

def number_of_steps_to_zero(number: int) -> int:
    step_count = 0

    while number > 0:
        if number % 2 == 0:
            number //= 2
        else:
            number -= 1
        step_count += 1

    return step_count
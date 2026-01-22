'''
You are given an array of positive integers numbers.

Alice and Bob are playing a game. Alice can choose one of the following options:
    - take all single-digit numbers from numbers, or
    - take all double-digit numbers from numbers

All remaining numbers are given to Bob.

Alice wins if the sum of her chosen numbers is strictly greater than the sum of Bob’s numbers.

Return true if Alice can win this game, otherwise return false.

Examples:
Input: numbers = [1, 2, 3, 4, 10]
Output: false

Input: numbers = [1, 2, 3, 4, 5, 14]
Output: true

Дан массив положительных целых чисел numbers.

Алиса и Боб играют в игру. Алиса может выбрать только один вариант:
    - взять все однозначные числа из массива numbers, или
    - взять все двузначные числа из массива numbers

Все остальные числа получает Боб.

Алиса выигрывает, если сумма её чисел строго больше суммы чисел Боба.

Верни true, если Алиса может выиграть, иначе верни false.

Примеры:
Ввод: numbers = [1, 2, 3, 4, 10]
Вывод: false

Ввод: numbers = [1, 2, 3, 4, 5, 14]
Вывод: true
'''

def can_alice_win(numbers: list[int]) -> bool:
    single_digit_sum = 0
    double_digit_sum = 0
    total_sum = sum(numbers)

    for number in numbers:
        if number < 10:
            single_digit_sum += number
        elif number < 100:
            double_digit_sum += number

    return single_digit_sum > total_sum - single_digit_sum or double_digit_sum > total_sum - double_digit_sum
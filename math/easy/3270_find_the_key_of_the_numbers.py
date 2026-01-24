'''
You are given three positive integers number_1, number_2, and number_3.

The key of these three numbers is defined as a four-digit number, created by the following rules:
    - If any number has fewer than 4 digits, pad it with leading zeros until it becomes 4 digits long;
    - For each position i, take the smallest digit among the i-th digits of number_1, number_2, and number_3;
    - The key is formed by these 4 chosen digits;
    - Return the key as an integer without leading zeros.

Examples:
Input: number_1 = 1, number_2 = 10, number_3 = 1000
Output: 0

Input: number_1 = 987, number_2 = 879, number_3 = 798
Output: 777

Даны три положительных целых числа number_1, number_2 и number_3.

Определим ключ этих трёх чисел как четырёхзначное число, которое строится по правилам:
    - Если какое-то число содержит меньше 4 цифр, то слева дописываются нули, пока длина не станет 4;
    - Для каждой позиции i берётся минимальная цифра среди i-й цифры чисел number_1, number_2 и number_3;
    - Из этих 4 цифр составляется ключ;
    - Верните ключ как число без ведущих нулей.

Примеры:
Ввод: number1 = 1, number2 = 10, number3 = 1000
Вывод: 0

Ввод: number1 = 987, number2 = 879, number3 = 798
Вывод: 777
'''

def generate_key(number_1: int, number_2: int, number_3: int) -> int:
    first_number = str(number_1).zfill(4)
    second_number = str(number_2).zfill(4)
    third_number = str(number_3).zfill(4)

    key_digits = []

    for index in range(4):
        smallest_digit = min(first_number[index], second_number[index], third_number[index])
        key_digits.append(smallest_digit)

    key_string = "".join(key_digits)
    return int(key_string)
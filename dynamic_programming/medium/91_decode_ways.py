'''
You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:
    + "1" → 'A'
    + "2" → 'B'
    + ...
    + "25" → 'Y'
    + "26" → 'Z'

There can be multiple ways to decode the message because some digit groupings overlap.

For example, the string "11106" can be decoded as:
    + "AAJF" with grouping (1, 1, 10, 6)
    + "KJF" with grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid, because "06" is not a valid code.

Given a string S containing only digits, return the number of ways to decode it. If no valid decoding exists, return 0. All test cases are guaranteed to fit in a 32-bit integer.

Examples:
Input: S = "12"
Output: 2

Input: S = "226"
Output: 3

Вы перехватили секретное сообщение, закодированное в виде строки из цифр. Расшифровка происходит по следующему правилу:
    + "1" → 'A'
    + "2" → 'B'
    + ...
    + "25" → 'Y'
    + "26" → 'Z'

Некоторые группы цифр могут перекрываться, поэтому существует несколько способов расшифровать сообщение.

Например, строку "11106" можно расшифровать так:
    + "AAJF" — разбиение на (1, 1, 10, 6)
    + "KJF" — разбиение на (11, 10, 6)
Разбиение (1, 11, 06) недопустимо, так как "06" не является корректным кодом (нельзя использовать числа с ведущими нулями).

Дана строка s, содержащая только цифры. Верните количество способов, которыми её можно расшифровать. Если ни одного способа нет — верните 0. Все тесты гарантировано помещаются в 32-битное целое число.

Примеры:
Ввод: s = "12"
Вывод: 2

Ввод: s = "226"
Вывод: 3
'''

def num_decodings(encoded_string: str) -> int:
    if not encoded_string or encoded_string[0] == '0':
        return 0

    length = len(encoded_string)
    decoding_ways = [0] * (length + 1)
    decoding_ways[0] = 1
    decoding_ways[1] = 1

    for index in range(2, length + 1):
        if encoded_string[index - 1] != '0':
            decoding_ways[index] += decoding_ways[index - 1]
        two_digit_number = int(encoded_string[index - 2:index])

        if 10 <= two_digit_number <= 26:
            decoding_ways[index] += decoding_ways[index - 2]

    return decoding_ways[length]
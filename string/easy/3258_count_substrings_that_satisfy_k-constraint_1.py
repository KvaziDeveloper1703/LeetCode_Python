'''
You are given a binary string s and an integer k.

A binary string satisfies the k-constraint if at least one of the following conditions is true:
    - The number of 0's in the string is at most k;
    - The number of 1's in the string is at most k.

Return an integer equal to the number of substrings of s that satisfy the k-constraint.

Examples:
Input: s = "10101", k = 1
Output: 12

Input: s = "1010101", k = 2
Output: 25

Дана бинарная строка s и целое число k.

Бинарная строка удовлетворяет k-ограничению, если выполняется хотя бы одно из условий:
    - Количество символов 0 в строке не превышает k;
    - Количество символов 1 в строке не превышает k.

Нужно вернуть число подстрок строки s, которые удовлетворяют k-ограничению.

Примеры:
Ввод: s = "10101", k = 1
Вывод: 12

Ввод: s = "1010101", k = 2
Вывод: 25
'''

def count_k_constraint_substrings(s: str, k: int) -> int:
    left_index = 0
    zero_count = 0
    one_count = 0
    total_substrings = 0

    for right_index in range(len(s)):
        if s[right_index] == '0':
            zero_count += 1
        else:
            one_count += 1

        while zero_count > k and one_count > k:
            if s[left_index] == '0':
                zero_count -= 1
            else:
                one_count -= 1
            left_index += 1

        total_substrings += right_index - left_index + 1

    return total_substrings
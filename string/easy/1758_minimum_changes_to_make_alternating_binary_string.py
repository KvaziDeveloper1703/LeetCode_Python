'''
You are given a string s consisting only of the characters '0' and '1'. In one operation, you may change any '0' to '1' or any '1' to '0'.

A string is called alternating if no two adjacent characters are the same. For example, "010" is alternating, but "0100" is not.

Return the minimum number of operations required to make s alternating.

Examples:
Input: s = "0100"
Output: 1

Input: s = "10"
Output: 0

Дана строка s, состоящая только из символов '0' и '1'. За одну операцию можно заменить любой '0' на '1' или любой '1' на '0'.

Строка называется чередующейся, если никакие два соседних символа в ней не совпадают. Например, строка "010" является чередующейся, а "0100" — нет.

Верните минимальное количество операций, необходимое, чтобы сделать строку s чередующейся.

Примеры:
Ввод: s = "0100"
Вывод: 1

Ввод: s = "10"
Вывод: 0.
'''

def min_operations(s: str) -> int:
    length_of_string = len(s)
    mismatches_pattern_start_with_zero = 0
    mismatches_pattern_start_with_one = 0

    for index in range(length_of_string):
        expected_char_for_zero_start = "0" if index % 2 == 0 else "1"
        expected_char_for_one_start = "1" if index % 2 == 0 else "0"

        if s[index] != expected_char_for_zero_start:
            mismatches_pattern_start_with_zero += 1
        if s[index] != expected_char_for_one_start:
            mismatches_pattern_start_with_one += 1

    return min(mismatches_pattern_start_with_zero, mismatches_pattern_start_with_one)
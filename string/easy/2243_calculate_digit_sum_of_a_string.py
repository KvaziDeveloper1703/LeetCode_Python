'''
You are given a digit string s and an integer k.

A round can be performed as long as the length of s is greater than k. In each round:
    - Split s into consecutive groups of length k. The last group may contain fewer than k characters;
    - For every group, replace it with the string representation of the sum of its digits. Example: "346" → "13" because 3 + 4 + 6 = 13;
    - Concatenate all resulting groups to form a new string.

Repeat this process while the new string is longer than k.

Return the final string after no more rounds can be performed.

Вам дана строка s, состоящая из цифр, и целое число k.

Раунд можно выполнить, если длина строки s больше k. В каждом раунде:
    - Разбейте строку s на подряд идущие группы длиной k. Последняя группа может быть короче k;
    - Каждую группу замените строкой, равной сумме цифр в этой группе. Пример: "346" → "13", так как 3 + 4 + 6 = 13;
    - Объедините все полученные строки в одну новую строку.

Повторяйте процесс, пока длина новой строки больше k.

Верните итоговую строку, когда новые раунды больше невозможны.
'''

def digit_sum(s: str, k: int) -> str:
    string_number = s
    group_size = k

    while len(string_number) > group_size:
        new_string_parts = []

        for index in range(0, len(string_number), group_size):
            group_substring = string_number[index:index + group_size]
            group_digit_sum = sum(int(character) for character in group_substring)
            new_string_parts.append(str(group_digit_sum))

        string_number = "".join(new_string_parts)

    return string_number
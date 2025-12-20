'''
You are given an array of strings words, where all strings have the same length n.

For each string words[i], define its difference integer array difference[i] of length n − 1 as follows:
    - Difference[i][j] = position(words[i][j + 1]) − position(words[i][j]), where 0 ≤ j ≤ n − 2;
    - The position of a letter is its index in the English alphabet: 'a' → 0, 'b' → 1, ..., 'z' → 25.

Find and return the string whose difference integer array is different from the others.

Examples:
Input: words = ["adc", "wzy", "abc"]
Output: "abc"

Input: words = ["aaa", "bob", "ccc", "ddd"]
Output: "bob"

Дан массив строк words, при этом все строки имеют одинаковую длину n.

Для каждой строки words[i] определяется массив разностей difference[i] длины n - 1, где:
    - Difference[i][j] = позиция(words[i][j + 1]) - позиция(words[i][j]), где 0 ≤ j ≤ n - 2;
    - Позиция буквы - это её номер в английском алфавите: 'a' → 0, 'b' → 1, ..., 'z' → 25.

Найдите и верните строку, массив разностей которой отличается от остальных.

Примеры:
Ввод: words = ["adc", "wzy", "abc"]
Вывод: "abc"

Ввод: words = ["aaa", "bob", "ccc", "ddd"]
Вывод: "bob"
'''

from typing import List

def odd_string(words: List[str]) -> str:
    def difference_array(word: str):
        return tuple(
            ord(word[index + 1]) - ord(word[index])
            for index in range(len(word) - 1)
        )

    first_difference = difference_array(words[0])
    second_difference = difference_array(words[1])
    third_difference = difference_array(words[2])

    if first_difference == second_difference or first_difference == third_difference:
        common_difference = first_difference
    else:
        common_difference = second_difference

    for word in words:
        if difference_array(word) != common_difference:
            return word
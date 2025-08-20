'''
Given a string S and an integer array indices of the same length.
The string S will be shuffled so that the character at position i moves to position indices[i] in the new string.

Return the shuffled string.

Examples:
Input: S = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"

Input: S = "abc", indices = [0,1,2]
Output: "abc"

Дана строка S и целочисленный массив indices такой же длины.
Строка S будет перемешана так, что символ на позиции i переместится в позицию indices[i] в новой строке.

Нужно вернуть получившуюся перемешанную строку.

Примеры:
Ввод: S = "codeleet", indices = [4,5,6,7,0,2,1,3]
Вывод: "leetcode"

Ввод: S = "abc", indices = [0,1,2]
Вывод: "abc"
'''

from typing import List

def restore_string(S: str, indices: List[int]) -> str:
    result = [''] * len(S)
    for character, position in zip(S, indices):
        result[position] = character
    return ''.join(result)
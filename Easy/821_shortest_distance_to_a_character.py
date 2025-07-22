'''
Given a string S and a character C that is guaranteed to appear at least once in S.

Return an array of integers answer, where answer.length == S.length and answer[i] represents the shortest distance from index i to the closest occurrence of character C in the string S.

Examples:
Input: S = "loveleetcode", C = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]

Input: S = "aaab", C = "b"
Output: [3,2,1,0]

Дана строка S и символ C, который гарантированно встречается хотя бы один раз в этой строке.

Необходимо вернуть массив целых чисел answer длиной, равной длине строки S, где answer[i] — это минимальное расстояние от индекса i до ближайшего вхождения символа C в строке S.

Примеры:
Ввод: S = "loveleetcode", C = "e"
Вывод: [3,2,1,0,1,0,0,1,2,2,1,0]

Ввод: S = "aaab", C = "b"
Вывод: [3,2,1,0]
'''

from typing import List

def shortest_to_character(S: str, target_character: str) -> List[int]:
    length = len(S)
    distances = [0] * length
    last_seen_left = float('-inf')

    for i in range(length):
        if S[i] == target_character:
            last_seen_left = i
        distances[i] = i - last_seen_left if last_seen_left != float('-inf') else float('inf')

    last_seen_right = float('inf')

    for i in range(length - 1, -1, -1):
        if S[i] == target_character:
            last_seen_right = i
        distances[i] = min(distances[i], last_seen_right - i if last_seen_right != float('inf') else float('inf'))

    return distances
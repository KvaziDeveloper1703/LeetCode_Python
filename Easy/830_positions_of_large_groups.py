'''
Given a string S consisting of lowercase letters. The characters in this string form consecutive groups of the same letter.
Each group can be described by an interval [start, end], where start and end are the inclusive indices of the first and last characters in the group.
A group is considered large if it contains three or more characters.

Return a list of intervals representing all large groups in the string. The result must be sorted in increasing order by the starting index.

Examples:
Input: S = "abbxxxxzzy"
Output: [[3,6]]

Input: S = "abc"
Output: []

Дана строка S, состоящая из строчных букв английского алфавита. Символы в этой строке образуют последовательные группы одинаковых букв.
Каждая группа может быть описана интервалом [start, end], где start и end — это включительно индексы начала и конца группы.
Группа считается большой, если она содержит три или более символов.

Необходимо вернуть список интервалов всех больших групп в строке. Результат должен быть отсортирован по возрастанию начального индекса.

Примеры:
Ввод: s = "abbxxxxzzy"
Вывод: [[3,6]]

Ввод: s = "abc"
Вывод: []
'''

from typing import List

def large_group_positions(self, S: str) -> List[List[int]]:
    result = []
    start = 0

    for i in range(1, len(S) + 1):
        if i == len(S) or S[i] != S[start]:
            if i - start >= 3:
                result.append([start, i - 1])
            start = i

    return result
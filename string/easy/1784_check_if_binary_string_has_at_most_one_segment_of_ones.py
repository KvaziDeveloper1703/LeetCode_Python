'''
You are given a binary string s with no leading zeros.
Return True if s contains at most one contiguous segment of ones. Otherwise, return False.

Examples:
Input: s = "1001"
Output: False

Input: s = "110"
Output: True

Дана двоичная строка s без ведущих нулей.
Верните True, если в строке есть не более одного непрерывного сегмента из единиц. В противном случае верните False.

Примеры:
Ввод: s = "1001"
Вывод: False

Ввод: s = "110"
Вывод: True
'''

def check_ones_segment(s: str) -> bool:
    count_segments = 0
    previous = '0'

    for current in s:
        if current == '1' and previous == '0':
            count_segments += 1
        previous = current

    return count_segments <= 1
'''
You are given a binary string s.

Return True if the longest contiguous segment of 1s is strictly longer than the longest contiguous segment of 0s. Otherwise, return False.

Дана двоичная строка s.

Верните True, если самый длинный непрерывный сегмент из 1 строго длиннее, чем самый длинный непрерывный сегмент из 0. В противном случае верните False.
'''

def check_zero_ones(s: str) -> bool:
    max_ones = max_zeros = 0
    current_ones = current_zeros = 0

    for char in s:
        if char == '1':
            current_ones += 1
            current_zeros = 0
        else:
            current_zeros += 1
            current_ones = 0

        max_ones = max(max_ones, current_ones)
        max_zeros = max(max_zeros, current_zeros)

    return max_ones > max_zeros
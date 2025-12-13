'''
You are given a 0-indexed string number of length n, consisting only of digits.

Return True if for every index i such that 0 ≤ i < n, the digit i appears in the string number exactly number[i] times. Otherwise, return False.

Вам дана строка number с нулевой индексацией длины n, состоящая только из цифр.

Необходимо вернуть True, если для каждого индекса i (0 ≤ i < n) цифра i встречается в строке number ровно number[i] раз. В противном случае верните False.
'''

def digit_count(number: str) -> bool:
    counts = [0] * 10

    for digit in number:
        counts[int(digit)] += 1

    for i in range(len(number)):
        if counts[i] != int(number[i]):
            return False

    return True
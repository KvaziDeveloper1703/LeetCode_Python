'''
A string is considered good if it contains no repeated characters.

Given a string s, return the number of good substrings of length 3 in s.

Note that if the same substring appears multiple times in different positions, each occurrence must be counted separately.

A substring is a contiguous sequence of characters within a string.

Строка считается хорошей, если в ней нет повторяющихся символов.

Дана строка s. Нужно вернуть количество хороших подстрок длины 3 в строке s.

Заметьте, что если одинаковая подстрока встречается несколько раз в разных местах строки, каждое появление нужно учитывать.

Подстрока - это непрерывная последовательность символов в строке.
'''

def count_good_substrings(s: str) -> int:
    count = 0

    for i in range(len(s) - 2):
        substring = s[i:i+3]
        if len(set(substring)) == 3:
            count += 1

    return count
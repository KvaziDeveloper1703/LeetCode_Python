'''
You are given a string s and a pattern string p, where p contains exactly one '*' character.
The '*' character can be replaced with any sequence of characters.
Return true if it is possible to replace '*' so that the pattern p becomes a substring of s. Otherwise, return false.

Examples:
Input: s = "leetcode", p = "ee*e"
Output: true

Input: s = "car", p = "c*v"
Output: false

Даны строка s и шаблон p, в котором содержится ровно один символ '*'.
Символ '*' можно заменить на любую последовательность символов.
Верните true, если можно заменить '*' так, чтобы строка p стала подстрокой строки s. В противном случае верните false.

Примеры:
Ввод: s = "leetcode", p = "ee*e"
Вывод: true

Ввод: s = "car", p = "c*v"
Вывод: false
'''

def has_match(self, s, p):
    parts = p.split('*')
    left = parts[0]
    right = parts[1]

    for i in range(len(s)):
        if s.startswith(left, i):
            if right in s[i + len(left):]:
                return True
    return False
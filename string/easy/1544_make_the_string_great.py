'''
Given a string S consisting of lowercase and uppercase English letters.

A good string is defined as a string that does not contain two adjacent characters S[i] and S[i+1] such that:
    + 0 <= i <= S.length - 2;
    + S[i] is a lowercase letter and S[i+1] is the same letter in uppercase, or vice versa.

To make the string good, you can repeatedly remove such adjacent pairs of characters that make the string bad. You can continue this process until no such pair exists.

Return the resulting string after it becomes good. The answer is guaranteed to be unique.

Examples:
Input: S = "leEeetcode"
Output: "leetcode"

Input: S = "abBAcC"
Output: ""

Дана строка S, состоящая из английских букв в верхнем и нижнем регистре.

Хорошая строка - это строка, которая не содержит двух соседних символов S[i] и S[i+1], таких что:
    + 0 <= i <= S.length - 2;
    + S[i] — буква в нижнем регистре, а S[i+1] — та же буква в верхнем регистре.

Чтобы сделать строку хорошей, можно многократно удалять такие пары соседних символов, которые делают строку плохой. Процесс повторяется, пока строка не станет хорошей.

Верните строку после того, как она станет хорошей. Гарантируется, что ответ будет единственным.

Примеры
Ввод: S = "leEeetcode"
Вывод: "leetcode"

Ввод: S = "abBAcC"
Вывод: ""
'''

def make_good(S: str) -> str:
    stack = []
    for character in S:
        if stack and abs(ord(stack[-1]) - ord(character)) == 32:
            stack.pop()
        else:
            stack.append(character)
    return "".join(stack)
'''
Given a string S and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string.
    + If there are fewer than k characters left at the end, reverse all of them.
    + If there are at least k but fewer than 2k characters left, reverse the first k characters and leave the rest as they are.

Examples:
Input: S = "abcdefg", k = 2
Output: "bacdfeg"

Input: S = "abcd", k = 2
Output: "bacd"

Дана строка S и целое число k. Необходимо выполнить следующую операцию:
    + Для каждых 2k символов строки (считая от начала) перевернуть (реверсировать) первые k символов.

Кроме того:
    + Если в конце остаётся меньше чем k символов, перевернуть их все.
    + Если в конце остаётся хотя бы k, но меньше чем 2k символов, перевернуть первые k символов, а остальные оставить без изменений.

Примеры:
Ввод: S = "abcdefg", k = 2
Вывод: "bacdfeg"

Ввод: S = "abcd", k = 2
Вывод: "bacd"
'''

def reverse_str(self, S: str, k: int) -> str:
    S = list(S)
    for i in range(0, len(S), 2 * k):
        S[i:i+k] = reversed(S[i:i+k])
    return ''.join(S)
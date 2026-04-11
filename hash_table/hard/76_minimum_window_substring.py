'''
You are given two strings S and T, of lengths m and n respectively.
Your task is to find the smallest substring of S that contains all the characters of T, including duplicates.
Return this minimum window substring. If no such substring exists, return an empty string "".

Examples:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Input: S = "a", T = "a"
Output: "a"

Даны две строки S и T длиной m и n соответственно.
Ваша задача — найти наименьшую подстроку в строке S, которая содержит все символы строки T, включая повторы.
Верните эту минимальную подстроку. Если такой подстроки не существует — верните пустую строку "".

Примеры:
Ввод: S = "ADOBECODEBANC", T = "ABC"
Вывод: "BANC"

Ввод: S = "a", T = "a"
Вывод: "a"
'''

from collections import Counter, defaultdict

def min_window(S: str, T: str) -> str:
    if not S or not T:
        return ""

    t_count = Counter(T)
    window_count = defaultdict(int)

    have, need = 0, len(t_count)
    result = [-1, -1]
    result_length = float("inf")
    left = 0

    for right in range(len(S)):
        character = S[right]
        window_count[character] += 1

        if character in t_count and window_count[character] == t_count[character]:
            have += 1

        while have == need:
            if (right - left + 1) < result_length:
                result = [left, right]
                result_length = right - left + 1

            window_count[S[left]] -= 1
            if S[left] in t_count and window_count[S[left]] < t_count[S[left]]:
                have -= 1
            left += 1

    start_index, end_index = result
    return S[start_index:end_index+1] if result_length != float("inf") else ""
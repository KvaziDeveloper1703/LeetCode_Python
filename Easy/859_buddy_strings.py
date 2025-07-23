'''
Given two strings S and goal, return True if you can make S equal to goal by swapping exactly two different letters in S. Otherwise, return False.

Swapping means choosing two different indices i and j in S and exchanging the characters at those positions.

Examples:
Input: S = "ab", goal = "ba"
Output: True

Input: S = "ab", goal = "ab"
Output: False

Даны две строки S и goal. Верните True, если можно сделать строки равными, поменяв местами ровно две разные буквы в строке S. В противном случае верните False.

Обмен — это выбор двух различных индексов i и j в строке S и перестановка символов на этих позициях.

Примеры:
Ввод: S = "ab", goal = "ba"
Вывод: True

Ввод: S = "ab", goal = "ab"
Вывод: False
'''

def buddy_strings(S: str, goal: str) -> bool:
    if len(S) != len(goal):
        return False

    if S == goal:
        unique_chars = set(S)
        return len(unique_chars) < len(S)

    mismatched_pairs = []
    for char_s, char_goal in zip(S, goal):
        if char_s != char_goal:
            mismatched_pairs.append((char_s, char_goal))

    if len(mismatched_pairs) != 2:
        return False

    first_pair, second_pair = mismatched_pairs
    return first_pair == (second_pair[1], second_pair[0])
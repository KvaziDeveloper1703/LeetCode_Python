'''
You are given two strings s and t, where:
    - each character appears at most once in s;
    - t is a permutation of s.

The permutation difference between s and t is defined as: the sum of the absolute differences between the index of each character in s and the index of the same character in t.
Return the permutation difference between s and t.

Даны две строки s и t, такие что:
    - каждый символ встречается в строке s не более одного раза;
    - строка t является перестановкой строки s.

Разность перестановок между s и t определяется как: сумма модулей разностей индексов каждого символа в s и индекса этого же символа в t.
Нужно вернуть значение разности перестановок между s и t.
'''

def find_permutation_difference(s: str, t: str) -> int:
    character_to_index_in_s = {character: index for index, character in enumerate(s)}

    permutation_difference = 0
    for index_in_t, character in enumerate(t):
        index_in_s = character_to_index_in_s[character]
        permutation_difference += abs(index_in_s - index_in_t)

    return permutation_difference
'''
You are given two strings s1 and s2 of equal length.
A string swap is an operation where you pick two indices in a string and swap the characters at those positions.

Return True if you can make the two strings equal by performing at most one swap on exactly one of the strings. Otherwise, return False.

Examples:
Input: s1 = "bank", s2 = "kanb"
Output: True

Input: s1 = "attack", s2 = "defend"
Output: False

Даны две строки s1 и s2 одинаковой длины.
Обмен в строке - это операция, при которой вы выбираете два индекса в строке и меняете местами символы на этих позициях.

Верните True, если вы можете сделать обе строки одинаковыми, выполнив не более одной операции обмена в одной из строк. В противном случае верните False.

Примеры:
Ввод: s1 = "bank", s2 = "kanb"
Вывод: True

Ввод: s1 = "attack", s2 = "defend"
Вывод: False
'''

def are_almost_equal(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    difference_indices = []
    for index in range(len(s1)):
        if s1[index] != s2[index]:
            difference_indices.append(index)

    if len(difference_indices) != 2:
        return False

    first_index, second_index = difference_indices
    return s1[first_index] == s2[second_index] and s1[second_index] == s2[first_index]
'''
You are given two strings s1 and s2, each of length 4, consisting of lowercase English letters.

You may perform the following operation on either of the strings any number of times:
    - Choose two indices i and j such that j - i = 2, and swap the characters at these positions in the chosen string.

Determine whether it is possible to make the two strings equal by applying this operation.

Return True if you can make s1 and s2 equal, and False otherwise.

Examples:
Input: s1 = "abcd", s2 = "cdab"
Output: True

Input: s1 = "abcd", s2 = "dacb"
Output: False

Даны две строки s1 и s2 длины 4, состоящие из строчных букв английского алфавита.

Над любой из строк можно выполнять следующую операцию неограниченное количество раз:
    - Выбрать два индекса i и j так, что j - i = 2, и поменять местами символы на этих позициях.

Определите, можно ли сделать строки s1 и s2 одинаковыми, используя данную операцию.

Верните True, если строки можно сделать равными, и False - в противном случае.

Примеры:
Ввод: s1 = "abcd", s2 = "cdab"
Вывод: True

Ввод: s1 = "abcd", s2 = "dacb"
Вывод: False
'''

def can_be_equal(s1: str, s2: str) -> bool:
    even_s1 = []
    odd_s1 = []
    even_s2 = []
    odd_s2 = []

    for i in range(4):
        if i % 2 == 0:
            even_s1.append(s1[i])
            even_s2.append(s2[i])
        else:
            odd_s1.append(s1[i])
            odd_s2.append(s2[i])

    even_s1.sort()
    even_s2.sort()
    odd_s1.sort()
    odd_s2.sort()

    if even_s1 != even_s2:
        return False

    if odd_s1 != odd_s2:
        return False

    return True
'''
You are given a string s consisting only of uppercase English letters.

You may perform a sequence of operations on this string. In one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from the string s.

After removing a substring, the remaining parts of the string are concatenated, which may create new occurrences of the substrings "AB" or "CD".

Return the minimum possible length of the string that can be obtained after performing the operations optimally.

Examples:
Input: s = "ABFCACDB"
Output: 2

Input: s = "ACBBD"
Output: 5

Дана строка s, состоящая только из заглавных латинских букв.

Над этой строкой можно выполнять операции. За одну операцию разрешается удалить любое вхождение подстроки "AB" или "CD" из строки s.

После удаления подстроки оставшиеся части строки склеиваются, в результате чего могут появиться новые подстроки "AB" или "CD".

Необходимо вернуть минимально возможную длину строки, которую можно получить, выполняя операции оптимальным образом.

Примеры:
Ввод: s = "ABFCACDB"
Вывод: 2

Ввод: s = "ACBBD"
Вывод: 5
'''

def min_length(s: str) -> int:
    stack = []

    for character in s:
        stack.append(character)

        if len(stack) >= 2:
            last_two = stack[-2] + stack[-1]
            if last_two == "AB" or last_two == "CD":
                stack.pop()
                stack.pop()

    return len(stack)
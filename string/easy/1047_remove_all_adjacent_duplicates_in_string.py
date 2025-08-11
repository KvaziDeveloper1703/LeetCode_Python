'''
Given a string S consisting of lowercase English letters.
A duplicate removal means choosing two adjacent and equal letters and removing them from the string.
We repeatedly perform duplicate removals on S until no more such removals are possible.

Return the final string after all possible duplicate removals. It can be proven that the result is unique.

Examples:
Input: S = "abbaca"
Output: "ca"

Input: S = "azxxzy"
Output: "ay"

Дана строка S, состоящая из строчных букв английского алфавита.
Удаление дубликата — это выбор двух одинаковых и стоящих рядом букв с их последующим удалением из строки.
Мы выполняем такие удаления снова и снова, пока это возможно.

Верните итоговую строку после всех возможных удалений дубликатов. Гарантируется, что результат будет единственным.

Примеры:
Ввод: S = "abbaca"
Вывод: "ca"

Ввод: S = "azxxzy"
Вывод: "ay"
'''

def remove_duplicates(S: str) -> str:
    stack = []

    for character in S:
        if stack and stack[-1] == character:
            stack.pop()
        else:
            stack.append(character)

    return "".join(stack)
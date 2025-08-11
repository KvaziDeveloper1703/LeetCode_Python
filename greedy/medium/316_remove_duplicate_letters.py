'''
Given a string S, remove duplicate letters so that every letter appears once and only once.
You must ensure that the resulting string is the smallest in lexicographical order among all possible results.

Examples:
Input: S = "bcabc"
Output: "abc"

Input: S = "cbacdcbc"
Output: "acdb"

Дана строка S. Удалите повторяющиеся буквы так, чтобы каждая буква встречалась ровно один раз.
При этом результат должен быть лексикографически минимальной строкой среди всех возможных вариантов.

Примеры:
Ввод: S = "bcabc"
Вывод: "abc"

Ввод: S = "cbacdcbc"
Вывод: "acdb"
'''

def remove_duplicate_letters(S: str) -> str:
    last_index_of_character = {character: idx for idx, character in enumerate(S)}
    result_stack = []
    characters_in_stack = set()

    for current_index, current_character in enumerate(S):
        if current_character not in characters_in_stack:
            while (result_stack 
                   and current_character < result_stack[-1] 
                   and current_index < last_index_of_character[result_stack[-1]]):

                removed_character = result_stack.pop()
                characters_in_stack.remove(removed_character)

            result_stack.append(current_character)
            characters_in_stack.add(current_character)

    return ''.join(result_stack)
'''
Given a string S, reverse it with the following rules:
    1) All non-English-letter characters must remain in their original positions;
    2) All English letters must be reversed in order, but still placed only at positions of other English letters.

Return the resulting string after applying these rules.

Examples:
Input: S = "ab-cd"
Output: "dc-ba"

Input: S = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Дана строка S. Необходимо перевернуть её по следующим правилам:
    1) Все неанглийские буквы должны остаться на своих местах;
    2) Все английские буквы должны быть переставлены в обратном порядке, но размещаться только на позициях других английских букв.

Верните полученную строку после применения этих правил.

Примеры:
Ввод: S = "ab-cd"
Вывод: "dc-ba"

Ввод: S = "a-bC-dEf-ghIj"
Вывод: "j-Ih-gfE-dCba"
'''

def reverse_only_letters(S: str) -> str:
    letter_characters = [character for character in S if character.isalpha()]
    result_characters = []

    for character in S:
        if character.isalpha():
            reversed_letter = letter_characters.pop()
            result_characters.append(reversed_letter)
        else:
            result_characters.append(character)

    final_result = ''.join(result_characters)
    return final_result
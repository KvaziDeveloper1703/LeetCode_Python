'''
Given a string S consisting only of lowercase English letters and the character '?'.

Replace all '?' characters with lowercase letters so that the final string does not contain two consecutive repeating characters.

You cannot modify the characters that are not '?'. It is guaranteed that the initial string has no consecutive repeating characters except possibly for '?'.

Return the resulting string after all replacements. If there are multiple valid answers, return any of them. It can be shown that at least one valid answer always exists.

Examples:
Input: S = "?zs"
Output: "azs"

Input: S = "ubv?w"
Output: "ubvaw"

Дана строка S, которая состоит только из строчных букв английского алфавита и символа '?'.

Необходимо заменить все символы '?' на строчные буквы так, чтобы в итоговой строке не было двух одинаковых подряд идущих символов.

Менять уже заданные (не '?') символы нельзя. Гарантируется, что в исходной строке нет подряд одинаковых символов, кроме '?'.

Нужно вернуть строку после всех замен. Если существует несколько правильных решений — можно вернуть любое. Доказывается, что хотя бы одно решение всегда существует.

Примеры:
Ввод: S = "?zs"
Вывод: "azs"

Ввод: S = "ubv?w"
Вывод: "ubvaw"
'''

def modify_string(S: str) -> str:
    letters = list(S)
    n = len(letters)

    for i in range(n):
        if letters[i] == '?':
            for character in "abc":
                if (i > 0 and letters[i - 1] == character) or (i < n - 1 and letters[i + 1] == character):
                    continue
                letters[i] = character
                break
    return "".join(letters)
'''
You are given a string s.
Your task is to remove all digits by repeatedly applying the following operation: Delete the first digit in the string and also delete the closest non-digit character to its left.
Return the resulting string after all possible operations are performed.

Examples:
Input: s = "abc"
Output: "abc"

Input: s = "cb34"
Output: ""

Дана строка s.
Нужно удалить все цифры, выполняя следующую операцию повторно: Удалить первую цифру в строке и также удалить ближайший слева символ, который не является цифрой.
Верните строку, которая получится после выполнения всех возможных операций.

Пример:
Ввод: s = "abc"
Вывод: "abc"

Ввод: s = "cb34"
Вывод: ""
'''

def clear_digits(s: str) -> str:
    result_characters = []

    for character in s:
        if character.isdigit():
            if result_characters:
                result_characters.pop()
        else:
            result_characters.append(character)

    return "".join(result_characters)
'''
You are given a string s consisting of English letters.

Return the greatest English letter that appears in s both in lowercase and uppercase form.

The returned letter must be in uppercase.

If no such letter exists, return an empty string.

One English letter b is considered greater than another letter a if b comes later in the English alphabet than a.

Examples:
Input: s = "lEeTcOdE"
Output: "E"

Input: s = "arRAzFif"
Output: "R"

Дана строка s, состоящая из букв английского алфавита.

Необходимо вернуть наибольшую букву английского алфавита, которая встречается в строке и в строчном, и в заглавном виде.

Возвращаемая буква должна быть заглавной.

Если такой буквы не существует, верните пустую строку.

Буква b считается больше буквы a, если она расположена позже в английском алфавите.

Примеры:
Ввод: s = "lEeTcOdE"
Вывод: "E"

Ввод: s = "arRAzFif"
Вывод: "R"
'''

def greatest_letter(s: str) -> str:
    characters = set(s)

    for letter_code in range(ord('Z'), ord('A') - 1, -1):
        uppercase_letter = chr(letter_code)
        lowercase_letter = uppercase_letter.lower()

        if uppercase_letter in characters and lowercase_letter in characters:
            return uppercase_letter

    return ""
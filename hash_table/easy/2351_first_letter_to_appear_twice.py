'''
You are given a string s consisting of lowercase English letters.

Return the first letter that appears twice in the string.

Definition:
A letter a is considered to appear twice before another letter b if the second occurrence of a appears earlier in the string than the second occurrence of b.

It is guaranteed that:
The string s contains at least one letter that appears twice.

Examples:
Input: s = "abccbaacz"
Output: "c"

Input:  s = "abcdd"
Output: "d"

Вам дана строка s, состоящая из строчных букв английского алфавита.

Необходимо вернуть первую букву, которая встречается дважды.

Определение:
Буква a считается появившейся дважды раньше, чем буква b, если второе появление буквы a находится раньше в строке, чем второе появление буквы b.

Гарантируется, что:
В строке s обязательно есть хотя бы одна буква, которая встречается дважды.

Примеры:
Ввод: s = "abccbaacz"
Вывод: "c"

Ввод: s = "abcdd"
Вывод: "d"
'''

def repeated_character(s: str) -> str:
    seen_characters = set()
    for character in s:
        if character in seen_characters:
            return character
        seen_characters.add(character)
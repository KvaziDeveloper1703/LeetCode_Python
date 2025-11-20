'''
A pangram is a sentence that contains every letter of the English alphabet at least once.

You are given a string sentence consisting only of lowercase English letters.
Return True if sentence is a pangram, and False otherwise.

Examples:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: True

Input: sentence = "leetcode"
Output: False

Панграмма - это строка, в которой каждая буква английского алфавита встречается хотя бы один раз.

Дана строка sentence, содержащая только строчные английские буквы.
Верните True, если sentence является панграммой, и False - в противном случае.

Примеры:
Ввод: sentence = "thequickbrownfoxjumpsoverthelazydog"
Вывод: True

Ввод: sentence = "leetcode"
Вывод: False
'''

def check_if_pangram(sentence: str) -> bool:
    letters_set = set()

    for character in sentence:
        letters_set.add(character)

    return len(letters_set) == 26
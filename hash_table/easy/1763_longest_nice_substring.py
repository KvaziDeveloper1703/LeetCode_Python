'''
A string s is called nice if, for every letter of the alphabet that appears in s, both its uppercase and lowercase forms are present.
For example, "abABB" is nice because both 'A'/'a' and 'B'/'b' appear.
However, "abA" is not nice because 'b' appears but 'B' does not.

Given a string s, return the longest substring of s that is nice.
If there are multiple such substrings, return the one that appears first in s.
If no nice substring exists, return an empty string.

Examples:
Input: s = "YazaAay"
Output: "aAa"

Input: s = "Bb"
Output: "Bb"

Строка s называется хорошей, если для каждой буквы алфавита, которая встречается в s, в строке присутствуют оба варианта - и прописная, и строчная.
Например, "abABB" - хорошая строка, потому что для 'a' и 'b' есть и строчные, и заглавные символы.
А строка "abA" - не хорошая, потому что 'b' есть, а 'B' - нет.

Дана строка s. Нужно вернуть самую длинную подстроку строки s, которая является хорошей.
Если таких подстрок несколько, вернуть первую по порядку.
Если хороших подстрок нет, вернуть пустую строку.

Примеры:
Ввод: s = "YazaAay"
Вывод: "aAa"

Ввод: s = "Bb"
Вывод: "Bb".
'''

def longest_nice_substring(input_string: str) -> str:
    def depth_first_search(current_substring: str) -> str:
        if len(current_substring) < 2:
            return ""

        characters_in_substring = set(current_substring)
            
        for index, character in enumerate(current_substring):
            if character.swapcase() not in characters_in_substring:
                left_substring_result = depth_first_search(current_substring[:index])
                right_substring_result = depth_first_search(current_substring[index + 1:])
                if len(left_substring_result) >= len(right_substring_result):
                    return left_substring_result
                else:
                    return right_substring_result

        return current_substring

    return depth_first_search(input_string)
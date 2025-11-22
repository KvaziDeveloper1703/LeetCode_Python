'''
Each lowercase letter from 'a' to 'j' has a value equal to its position in the alphabet starting from 0.

The numerical value of a string is formed by concatenating the values of its letters and converting the result into an integer.

You are given three strings: firstWord, secondWord, and targetWord, all using only letters 'a' to 'j'.

Return True if the numerical value of firstWord plus the numerical value of secondWord equals the numerical value of targetWord. Otherwise, return False.

Каждой строчной букве от 'a' до 'j' присвоено значение, равное её позиции в алфавите, начиная с 0.

Числовое значение строки - это конкатенация значений её букв, преобразованная в целое число.

Даны три строки: firstWord, secondWord и targetWord, содержащие только буквы от 'a' до 'j'.

Верните True, если числовое значение firstWord + числовое значение secondWord равно числовому значению targetWord. Иначе верните False.
'''

def is_sum_equal(firstWord: str, secondWord: str, targetWord: str) -> bool:
    def convert_word_to_value(word: str) -> int:
        numeric_string = ''.join(str(ord(current_character) - ord('a')) for current_character in word)
        return int(numeric_string)

    return (convert_word_to_value(firstWord) + convert_word_to_value(secondWord)) == convert_word_to_value(targetWord)
'''
Given an array of strings words. Each word can be transformed by converting every letter into its Morse code equivalent and then concatenating the results.

Return the number of unique transformations among all the words.

Examples:
Input: words = ["gin","zen","gig","msg"]
Output: 2

Input: words = ["a"]
Output: 1

Дан массив строк words. Каждое слово преобразуется путём замены каждой буквы на соответствующий код Морзе и последующей конкатенации этих кодов.

Нужно вернуть количество уникальных преобразований среди всех слов.

Примеры:
Ввод: words = ["gin","zen","gig","msg"]
Вывод: 2

Ввод: words = ["a"]
Вывод: 1
'''

from typing import List

def unique_morse_representations(words: List[str]) -> int:
    morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    character_to_morse = {}

    for i in range(26):
        letter = chr(ord('a') + i)
        code = morse_codes[i]
        character_to_morse[letter] = code

    transformations = set()

    for word in words:
        morse_word = ""
        for character in word:
            morse_code = character_to_morse[character]
            morse_word += morse_code
        transformations.add(morse_word)

    return len(transformations)
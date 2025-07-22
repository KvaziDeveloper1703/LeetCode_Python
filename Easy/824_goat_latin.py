'''
Given a string sentence consisting of words separated by spaces. Each word contains only uppercase and lowercase English letters.

Convert the sentence into Goat Latin, a made-up language, using the following rules:
    1) If a word begins with a vowel, simply append "ma" to the end of the word.
    2) If a word begins with a consonant, remove the first letter, append it to the end of the word, and then add "ma".
    3) After applying one of the above transformations, add a number of letters 'a' to the end of the word equal to its position in the sentence.

Return the final sentence in Goat Latin form.

Examples:
Input: sentence = "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Input: sentence = "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaahetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

Дана строка sentence, состоящая из слов, разделённых пробелами. Каждое слово содержит только строчные и заглавные буквы английского алфавита.

Ваша задача — преобразовать строку в Goat Latin — вымышленный язык — по следующим правилам:
    1) Если слово начинается с гласной буквы, к его концу добавляется "ma".
    2) Если слово начинается с согласной буквы, первая буква удаляется, добавляется в конец слова, после чего прибавляется "ma".
    3) После применения одного из этих правил к каждому слову, к его концу добавляется определённое количество букв 'a' в зависимости от его позиции в предложении.

Верните итоговое предложение в формате Goat Latin.

Примеры:
Ввод: sentence = "I speak Goat Latin"
Вывод: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Ввод: sentence = "The quick brown fox jumped over the lazy dog"
Вывод: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
'''

def to_goat_latin(sentence: str) -> str:
    vowels = set('aeiouyAEIOUY')
    words = sentence.split()
    result = []

    for index, word in enumerate(words, start=1):
        if word[0] in vowels:
            goat_word = word + 'ma'
        else:
            goat_word = word[1:] + word[0] + 'ma'
        goat_word += 'a' * index
        result.append(goat_word)

    return ' '.join(result)
'''
You have a keyboard where some letter keys are broken. All other keys work correctly.

You are given:
    - A string text, consisting of words separated by a single space;
    - A string brokenLetters, containing all the distinct letters that are broken on the keyboard.

Return the number of words in text that can be typed fully using this keyboard.

У вас есть клавиатура, на которой некоторые буквенные клавиши сломаны. Все остальные клавиши работают нормально.

Дано:
    - строка text, состоящая из слов, разделённых одним пробелом;
    - строка brokenLetters, содержащая все сломанные буквы.

Нужно вернуть количество слов в text, которые можно напечатать полностью, то есть слова, в которых нет ни одной буквы из brokenLetters.
'''

def can_be_typed_words(text: str, brokenLetters: str) -> int:
    broken_letters_set = set(brokenLetters)
    valid_words_count = 0

    for word in text.split():
        if all(character not in broken_letters_set for character in word):
            valid_words_count += 1

    return valid_words_count
'''
Given two strings S and T. Each string represents input into a text editor, where:
    + '#' represents a backspace character;
    + typing '#' when the text is empty leaves it empty.

Return True if both strings are equal after processing the backspaces. Otherwise, return False.

Examples:
Input: S = "ab#c", T = "ad#c"
Output: True

Input: S = "ab##", T = "c#d#"
Output: True

Даны две строки S и T. Каждая строка представляет ввод в текстовый редактор, где:
    + '#' обозначает символ удаления (backspace);
    + нажатие '#', когда текст уже пуст, оставляет его пустым.

Верните True, если после обработки всех удалений строки S и T становятся одинаковыми. В противном случае верните False.

Примеры:
Ввод: S = "ab#c", T = "ad#c"
Вывод: True

Ввод: S = "ab##", T = "c#d#"
Вывод: True
'''

def backspace_сompare(S: str, T: str) -> bool:
    def build(text):
        result = []
        for character in text:
            if character == '#':
                if result:
                    result.pop()
            else:
                result.append(character)
        return ''.join(result)

    return build(S) == build(T)
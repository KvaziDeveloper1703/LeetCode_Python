'''
Given a string S of lowercase English letters and an array widths, where each element represents the pixel width of the corresponding letter.
You want to write S across lines, where each line can hold up to 100 pixels. 
Write the letters one by one, and start a new line when the current line cannot fit the next letter.

Return an array of two integers:
    + the total number of lines used,
    + and the width used on the last line.

Дана строка S из строчных английских букв и массив widths, где каждый элемент — это ширина соответствующей буквы.
Нужно записать строку по строкам, где каждая строка вмещает не более 100 пикселей. 
Буквы записываются подряд, и если следующая не помещается — начинается новая строка.

Верните два числа:
    + сколько всего строк получилось,
    + и сколько пикселей заняла последняя строка.
'''

from typing import List

def number_of_lines(widths: List[int], S: str) -> List[int]:
    max_width = 100
    lines = 1
    current_width = 0

    for character in S:
        index = ord(character) - ord('a')
        character_width = widths[index]

        if current_width + character_width > max_width:
            lines += 1
            current_width = character_width
        else:
            current_width += character_width

    return [lines, current_width]
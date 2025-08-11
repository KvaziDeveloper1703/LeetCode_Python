'''
Given an array of words and an integer max_width, format the text so that each line has exactly max_width characters and is fully justified.
Use a greedy approach: fill each line with as many words as possible.

Rules:
    + Add spaces between words to make the line exactly max_width characters long;
    + Distribute spaces as evenly as possible between words;
    + If extra spaces remain, put more on the left;
    + The last line should be left-justified, with words separated by a single space and any extra spaces added at the end.

Example:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], max_width = 16
Output: [   "This    is    an",
            "example  of text",
            "justification.  "
    ]

Дан массив слов words и целое число max_width. Необходимо отформатировать текст так, чтобы каждая строка содержала ровно max_width символов и была полностью выровнена по ширине.
Используйте жадный подход: заполняйте каждую строку максимально возможным количеством слов.

Правила:
    + Между словами нужно вставить пробелы так, чтобы длина строки была ровно max_width символов;
    + Пробелы распределяются как можно равномернее между словами;
    + Если остаются лишние пробелы, они добавляются в начале между левыми словами;
    + Последняя строка должна быть выровнена по левому краю — между словами ставится по одному пробелу, а оставшиеся пробелы добавляются в конец строки.

Пример:
Ввод: words = ["This", "is", "an", "example", "of", "text", "justification."], max_width = 16
Вывод: ["This    is    an",  
        "example  of text",  
        "justification.  "
    ]
'''

from typing import List

def full_justify(words: List[str], max_width: int) -> List[str]:
    result = []
    line = []
    line_length = 0

    for word in words:
        if line_length + len(word) + len(line) > max_width:
            spaces = max_width - line_length
            if len(line) == 1:
                result.append(line[0] + ' ' * spaces)
            else:
                even_space = spaces // (len(line) - 1)
                extra = spaces % (len(line) - 1)
                for i in range(extra):
                    line[i] += ' '
                result.append((' ' * even_space).join(line))
            line = []
            line_len = 0

        line.append(word)
        line_len += len(word)

    result.append(' '.join(line).ljust(max_width))
    return result
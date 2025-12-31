'''
You are given an integer n that consists of exactly three digits.

We call the number n fascinating if, after performing the following operation, the resulting number:
    - contains all digits from 1 to 9 exactly once, and
    - does not contain the digit 0.

Operation:
- Concatenate the numbers n, 2 × n, and 3 × n.

Return True if n is fascinating, otherwise return False.

Concatenating numbers means joining them together.

Examples:
Input: n = 192
Output: True

Input: n = 100
Output: False

Дано целое число n, состоящее ровно из трёх цифр.

Число n называется fascinating (фантастическим), если после выполнения следующей операции полученное число:
    - содержит все цифры от 1 до 9 ровно по одному разу, и
    - не содержит цифру 0.

Операция:
    - Конкатенировать числа n, 2 × n и 3 × n.

Верните True, если число n является фантастическим, иначе верните False.

Конкатенация чисел означает их объединение в одну строку.

Примеры:
Ввод: n = 192
Вывод: True

Ввод: n = 100
Вывод: False
'''

def is_fascinating(n: int) -> bool:
    s = str(n) + str(2 * n) + str(3 * n)

    if len(s) != 9:
        return False

    if '0' in s:
        return False

    return set(s) == set('123456789')
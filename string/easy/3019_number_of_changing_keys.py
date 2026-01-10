'''
You are given a 0-indexed string s representing characters typed by a user.
A key change is defined as typing a character using a different keyboard key than the one used for the previous character.

Important:
Modifier keys such as Shift or Caps Lock are not considered when determining a key change.
This means that typing 'a' followed by 'A' does not count as a key change.

Your task is to count how many times the user changed the key while typing the string s.
Return the total number of key changes.

Examples:
Input: s = "aAbBcC"
Output: 2

Input: s = "AaAaAaaA"
Output: 0

Вам дана строка s с индексацией от 0, представляющая символы, набранные пользователем.
Смена клавиши определяется как ввод символа с использованием другой клавиши, отличной от той, которая использовалась для предыдущего символа.

Важно:
Модификаторы клавиатуры, такие как Shift или Caps Lock, не учитываются при определении смены клавиши.
То есть ввод 'a', а затем 'A' не считается сменой клавиши.

Необходимо подсчитать количество смен клавиши, которые пользователь совершил при наборе строки s.
Верните общее количество таких смен.

Примеры:
Ввод: s = "aAbBcC"
Вывод: 2

Ввод: s = "AaAaAaaA"
Вывод: 0
'''

def count_key_changes(s: str) -> int:
    changes = 0

    for i in range(1, len(s)):
        if s[i].lower() != s[i - 1].lower():
            changes += 1

    return changes
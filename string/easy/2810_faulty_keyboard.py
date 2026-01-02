'''
Your laptop keyboard is faulty. Whenever you type the character 'i', the entire string currently displayed on the screen is reversed. Typing any other character works normally.

You are given a 0-indexed string s. You type each character of s one by one using this faulty keyboard.

Return the final string that appears on the screen after typing all characters.

Examples:
Input: s = "string"
Output: "rtsng"

Input: s = "poiinter"
Output: "ponter"

Клавиатура вашего ноутбука неисправна. Каждый раз, когда вы вводите символ 'i', вся строка, которая в данный момент отображается на экране, переворачивается. Ввод других символов работает нормально.

Вам дана 0-индексированная строка s. Вы поочерёдно вводите каждый символ строки s с помощью этой неисправной клавиатуры.

Необходимо вернуть итоговую строку, которая окажется на экране после ввода всех символов.

Примеры:
Ввод: s = "string"
Вывод: "rtsng"

Ввод: s = "poiinter"
Вывод: "ponter"
'''

def final_string(inputString: str) -> str:
    textOnScreen = ""

    for currentCharacter in inputString:
        if currentCharacter == 'i':
            textOnScreen = textOnScreen[::-1]
        else:
            textOnScreen += currentCharacter

    return textOnScreen
'''
You are given a string command, which consists only of the characters "G", "()", and "(al)" arranged in some order.

You need to design a Goal Parser that interprets the command according to the following rules:
    - "G" is interpreted as "G",
    - "()" is interpreted as "o",
    - "(al)" is interpreted as "al".

After interpreting all parts of the command, concatenate the resulting strings in the same order and return the final result.

Examples:
Input: command = "G()(al)"
Output: "Goal"

Input: command = "G()()()()(al)"
Output: "Gooooal"

Дана строка command, состоящая только из символов "G", "()" и "(al)" в некотором порядке.

Нужно реализовать парсер Goal Parser, который интерпретирует строку по следующим правилам:
    - "G" интерпретируется как "G",
    - "()" интерпретируется как "o",
    - "(al)" интерпретируется как "al".

После замены всех частей нужно соединить результаты в исходном порядке и вернуть получившуюся строку.

Примеры:
Ввод: command = "G()(al)"
Вывод: "Goal"

Ввод: command = "G()()()()(al)"
Вывод: "Gooooal"
'''

class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")
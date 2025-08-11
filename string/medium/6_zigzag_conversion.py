'''
You are given a string S and an integer number_of_rows. Write code to rearrange the characters of S in a zigzag pattern on number_of_rows rows and then read the result line by line.

For example, if S = "PAYPALISHIRING" and number_of_rows = 3, the zigzag pattern looks like this:
P   A   H   N  
A P L S I I G  
Y   I   R
Reading line by line, the output is: "PAHNAPLSIIGYIR"

Дана строка S и целое число number_of_rows. Напишите код, который переставит символы строки S в зигзагообразный узор по заданному числу строк, а затем считает результат построчно.
Например, если S = "PAYPALISHIRING" и number_of_rows = 3, зигзагообразный узор будет выглядеть так:
P   A   H   N  
A P L S I I G  
Y   I   R
Читая построчно, получим результат: "PAHNAPLSIIGYIR"
'''

def convert(S: str, number_of_rows: int) -> str:
    if number_of_rows == 1 or number_of_rows >= len(S):
        return S

    rows = [''] * number_of_rows
    current_row = 0
    going_down = False

    for character in S:
        rows[current_row] += character
        if current_row == 0 or current_row == number_of_rows - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1

    return ''.join(rows)
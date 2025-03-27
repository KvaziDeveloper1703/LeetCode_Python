'''
You are given a string s and an integer numRows. Write code to rearrange the characters of s in a zigzag pattern on numRows rows and then read the result line by line.

For example, if s = "PAYPALISHIRING" and numRows = 3, the zigzag pattern looks like this:
P   A   H   N  
A P L S I I G  
Y   I   R
Reading line by line, the output is: "PAHNAPLSIIGYIR"
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        curr_row = 0
        going_down = False

        for char in s:
            rows[curr_row] += char
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            curr_row += 1 if going_down else -1

        return ''.join(rows)
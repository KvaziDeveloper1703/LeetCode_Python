'''
Given an m x n grid of characters board and a string word, return true if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same cell may not be used more than once.

Example:
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]
        ]
word = "ABCCED"
Output: true

Дана сетка символов board размером m x n и строка word. Необходимо определить, существует ли данное слово в сетке.
Слово может быть составлено из последовательно соседних ячеек, где соседними считаются ячейки, находящиеся по горизонтали или вертикали. Одна и та же ячейка не может быть использована более одного раза при составлении слова.

Пример:
Ввод: board = [ ["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]
        ]
word = "ABCCED"
Вывод: true
'''

from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    num_rows, num_columns = len(board), len(board[0])
    
    def depth_first_search(row: int, column: int, word_index: int) -> bool:
        
        if word_index == len(word):
            return True
        if row < 0 or row >= num_rows or column < 0 or column >= num_columns:
            return False
        if board[row][column] != word[word_index]:
            return False
        
        current_character = board[row][column]
        board[row][column] = "#"
        path_found = (
            depth_first_search(row + 1, column, word_index + 1) or
            depth_first_search(row - 1, column, word_index + 1) or
            depth_first_search(row, column + 1, word_index + 1) or
            depth_first_search(row, column - 1, word_index + 1)
        )
        
        board[row][column] = current_character
        return path_found
    
    for row in range(num_rows):
        for column in range(num_columns):
            if depth_first_search(row, column, 0):
                return True
    
    return False
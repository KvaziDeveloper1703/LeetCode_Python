'''
A cell in an Excel sheet is represented as a string "<column><row>", where:
    - <column> is the column number expressed using uppercase letters: 1 → A, 2 → B, 3 → C, …;
    - <row> is the row number expressed as an integer.

You are given a string s in the format "<column1><row1>:<column2><row2>".
Here <column1> and <row1> represent the starting column and row, and <column2> and <row2> represent the ending column and row.
It is guaranteed that r1 ≤ r2 and c1 ≤ c2.

Return a list of all cells (x, y) such that r1 ≤ x ≤ r2 and c1 ≤ y ≤ c2.

Each cell must be returned as a string in the same format ("<column><row>").
The output must be sorted first by columns and then by rows in non-decreasing order.

Examples:
Input: "K1:L2"
Output: ["K1", "K2", "L1", "L2"]

Input: "A1:F1"
Output: ["A1", "B1", "C1", "D1", "E1", "F1"]

Ячейка Excel обозначается строкой вида "<column><row>", где:
    - <column> - это номер столбца, записанный заглавными буквами: 1 → A, 2 → B, 3 → C и так далее;
    - <row> - это номер строки, записанный целым числом.

Вам дана строка s в формате "<column1><row1>:<column2><row2>".
Здесь <column1>, <row1> - начальный столбец и строка,
<column2>, <row2> - конечный столбец и строка.
Гарантируется, что r1 ≤ r2 и c1 ≤ c2.

Верните список всех ячеек (x, y), которые удовлетворяют условиям r1 ≤ x ≤ r2 и c1 ≤ y ≤ c2.

Каждая ячейка должна быть записана в том же формате ("<column><row>").
Список должен быть отсортирован сначала по столбцам, затем по строкам.

Пример:
Ввод: "K1:L2"
Вывод: ["K1", "K2", "L1", "L2"]

Ввод: "A1:F1"
Вывод: ["A1", "B1", "C1", "D1", "E1", "F1"]
'''

from typing import List

def cells_in_range(s: str) -> List[str]:
    start_column = s[0]
    start_row = int(s[1])
    end_column = s[3]
    end_row = int(s[4])

    cells = []

    for column_code in range(ord(start_column), ord(end_column) + 1):
        for row_number in range(start_row, end_row + 1):
            cell_name = chr(column_code) + str(row_number)
            cells.append(cell_name)

    return cells
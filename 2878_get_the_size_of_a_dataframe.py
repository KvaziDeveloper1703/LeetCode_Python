'''
You are given a DataFrame players with multiple columns.

Write a solution to calculate the number of rows and the number of columns in the DataFrame.

Return the result as an array in the following format: [number of rows, number of columns].

Example:
Input: A DataFrame with 10 rows and 5 columns.
Output: [10, 5]

Дан DataFrame players, который содержит несколько столбцов.

Напишите решение, которое вычисляет количество строк и количество столбцов в этом DataFrame.

Верните результат в виде массива в формате: [количество строк, количество столбцов].

Пример:
Ввод: DataFrame из 10 строк и 5 столбцов.
Вывод: [10, 5]
'''

import pandas as pd
from typing import List

def get_dataframe_size(players: pd.DataFrame) -> List[int]:
    rows, columns = players.shape
    return [rows, columns]
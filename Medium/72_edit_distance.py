'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 into word2.

You may perform the following operations:
+ Insert a character;
+ Delete a character;
+ Replace a character.

Example:
Input: word1 = "horse", word2 = "ros"
Output: 3

Даны две строки word1 и word2. Верните минимальное количество операций, необходимых для преобразования word1 в word2.

Разрешённые операции:
+ Вставка символа;
+ Удаление символа;
+ Замена символа.

Пример:
Ввод: word1 = "horse", word2 = "ros"
Вывод: 3
'''

def min_distance(source_word: str, target_word: str) -> int:
    source_length = len(source_word)
    target_length = len(target_word)
    edit_distance_table = []

    for row_index in range(source_length + 1):
        current_row = []
        for column_index in range(target_length + 1):
            current_row.append(0)
        edit_distance_table.append(current_row)

    for row_index in range(source_length + 1):
        edit_distance_table[row_index][0] = row_index  # удаление всех символов

    for column_index in range(target_length + 1):
        edit_distance_table[0][column_index] = column_index  # вставка всех символов

    for row_index in range(1, source_length + 1):
        for column_index in range(1, target_length + 1):
            current_char_from_source = source_word[row_index - 1]
            current_char_from_target = target_word[column_index - 1]
    
            if current_char_from_source == current_char_from_target:
                edit_distance_table[row_index][column_index] = edit_distance_table[row_index - 1][column_index - 1]
            else:
                cost_insert = edit_distance_table[row_index][column_index - 1]     # вставка
                cost_delete = edit_distance_table[row_index - 1][column_index]     # удаление
                cost_replace = edit_distance_table[row_index - 1][column_index - 1]  # замена
                edit_distance_table[row_index][column_index] = 1 + min(cost_insert, cost_delete, cost_replace)

    return edit_distance_table[source_length][target_length]
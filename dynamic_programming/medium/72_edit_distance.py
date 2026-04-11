'''
Given two strings source_word and target_word.

Return the minimum number of operations required to convert source_word into target_word.

You may perform the following operations:
    + Insert a character;
    + Delete a character;
    + Replace a character.

Example:
Input: source_word = "horse", target_word = "ros"
Output: 3

Даны две строки source_word и target_word. Верните минимальное количество операций, необходимых для преобразования source_word в target_word.

Разрешённые операции:
    + Вставка символа;
    + Удаление символа;
    + Замена символа.

Пример:
Ввод: source_word = "horse", target_word = "ros"
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
        edit_distance_table[row_index][0] = row_index

    for column_index in range(target_length + 1):
        edit_distance_table[0][column_index] = column_index

    for row_index in range(1, source_length + 1):
        for column_index in range(1, target_length + 1):
            current_char_from_source = source_word[row_index - 1]
            current_char_from_target = target_word[column_index - 1]

            if current_char_from_source == current_char_from_target:
                edit_distance_table[row_index][column_index] = edit_distance_table[row_index - 1][column_index - 1]
            else:
                cost_insert = edit_distance_table[row_index][column_index - 1]
                cost_delete = edit_distance_table[row_index - 1][column_index]
                cost_replace = edit_distance_table[row_index - 1][column_index - 1]
                edit_distance_table[row_index][column_index] = 1 + min(cost_insert, cost_delete, cost_replace)

    return edit_distance_table[source_length][target_length]
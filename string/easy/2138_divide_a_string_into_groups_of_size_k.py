'''
A string s can be divided into groups of size k using this procedure:
    - The first group is made from the first k characters of the string, the second group from the next k characters, and so on. Each character belongs to exactly one group;
    - For the last group, if fewer than k characters remain, you must add the fill character until the group reaches size k;
    - The grouping must be done so that if you remove the fill characters from the last group and join all groups together, you get the original string s.

Given the string s, the group size k, and the fill character fill, return an array of strings representing all the groups created using this procedure.

Examples:
Input: s = "abcdefghi", k = 3, fill = "x"
Output: ["abc","def","ghi"]

Input: s = "abcdefghij", k = 3, fill = "x"
Output: ["abc","def","ghi","jxx"]

Строку s можно разделить на группы длины k по следующему правилу:
    - Первая группа состоит из первых k символов строки, вторая группа - из следующих k символов и так далее. Каждый символ может входить только в одну группу;
    - Если в последней группе остаётся меньше чем k символов, недостающие символы необходимо заполнить символом fill, чтобы группа имела длину k;
    - Разбиение выполняется так, чтобы если удалить символы заполнения из последней группы и соединить все группы обратно, получилось исходное s.

По данной строке s, длине группы k и символу заполнения fill верните массив строк, представляющий группы, на которые была разделена строка.

Примеры:
Ввод: s = "abcdefghi", k = 3, fill = "x"
Вывод: ["abc","def","ghi"]

Ввод: s = "abcdefghij", k = 3, fill = "x"
Вывод: ["abc","def","ghi","jxx"]
'''

from typing import List

def divide_string(s: str, k: int, fill: str) -> List[str]:
    result_groups = []
    current_index = 0

    while current_index < len(s):
        group = s[current_index : current_index + k]

        if len(group) < k:
            group += fill * (k - len(group))

        result_groups.append(group)
        current_index += k

    return result_groups
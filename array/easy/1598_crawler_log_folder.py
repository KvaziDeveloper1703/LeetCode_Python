'''
Given a log of folder change operations in a LeetCode-style file system.

The possible operations are:
    + "../" : Move to the parent folder. If you are already in the main folder, stay there;
    + "./" : Stay in the current folder;
    + "x/" : Move into a child folder named x. It is guaranteed that this folder exists.

The system starts in the main folder. After performing all operations in logs, return the minimum number of operations needed to return to the main folder.

Examples:
Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2

Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
Output: 3

Вам дан журнал операций изменения папок в файловой системе (по стилю LeetCode).

Возможные операции:
    + "../" : Перейти в родительскую папку. Если вы уже в главной папке, остаетесь в ней;
    + "./" : Остаётесь в текущей папке;
    + "x/" : Перейти в дочернюю папку с именем x. Гарантируется, что эта папка существует.

Система изначально находится в главной папке. После выполнения всех операций из logs нужно вернуть минимальное количество операций, чтобы вернуться в главную папку.

Примеры:
Ввод: logs = ["d1/","d2/","../","d21/","./"]
Вывод: 2

Ввод: logs = ["d1/","d2/","./","d3/","../","d31/"]
Вывод: 3
'''

from typing import List

def min_operations(logs: List[str]) -> int:
    depth = 0

    for log in logs:
        if log == "../":
            if depth > 0:
                depth -= 1
        elif log == "./":
            continue
        else:
            depth += 1

    return depth
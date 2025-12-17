'''
You are given a 0-indexed string blocks of length n, where each character is either 'W' or 'B':
    - 'W' represents a white block;
    - 'B' represents a black block.

You are also given an integer k, which represents the required number of consecutive black blocks.

In one operation, you may recolor one white block ('W') and change it to a black block ('B').

Your task is to determine the minimum number of operations required so that the string contains at least one substring of k consecutive black blocks.

Return this minimum number.

Вам дана строка с нулевой индексацией blocks длины n, состоящая из символов 'W' и 'B', где:
    - 'W' - белый блок;
    - 'B' - чёрный блок.

Также дано целое число k, обозначающее требуемое количество последовательных чёрных блоков.

За одну операцию вы можете перекрасить один белый блок ('W') в чёрный ('B').

Необходимо определить минимальное количество операций, после которых в строке появится хотя бы один участок из k подряд идущих чёрных блоков.

Верните это минимальное количество операций.
'''

def minimum_recolors(blocks: str, k: int) -> int:
    minimum_operations = float("inf")
    white_blocks_count = 0

    for index in range(k):
        if blocks[index] == 'W':
            white_blocks_count += 1

    minimum_operations = white_blocks_count

    for index in range(k, len(blocks)):
        if blocks[index] == 'W':
            white_blocks_count += 1
        if blocks[index - k] == 'W':
            white_blocks_count -= 1

        minimum_operations = min(minimum_operations, white_blocks_count)

    return minimum_operations
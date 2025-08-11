'''
Given two version strings version_1 and version_2, compare them. A version string consists of revisions separated by dots '.'. Each revision is treated as an integer, ignoring any leading zeros.

To compare version strings:
    + Compare each revision from left to right;
    + If one version has fewer revisions, treat the missing ones as 0.

Return:
    + -1 if version_1 < version_2;
    + 1 if version_1 > version_2;
    + 0 if they are equal.

Examples:
Input: version_1 = "1.2", version_2 = "1.10"
Output: -1

Input: version_1 = "1.01", version_2 = "1.001"
Output: 0

Даны две строки version_1 и version_2, представляющие версии. Версия состоит из числовых ревизий, разделённых точками '.'. Каждую ревизию нужно интерпретировать как целое число, игнорируя ведущие нули.

Сравнение выполняется:
    + Слева направо, по каждой ревизии;
    + Если в одной версии ревизий меньше, недостающие считаются равными 0.

Верните:
    + -1, если version_1 < version_2;
    + 1, если version_1 > version_2;
    + 0, если версии равны.

Примеры:
Ввод: version_1 = "1.2", version_2 = "1.10"
Вывод: -1

Ввод: version_1 = "1.01", version_2 = "1.001"
Вывод: 0
'''

def compare_version(version_1: str, version_2: str) -> int:
    version_1_parts = list(map(int, version_1.split('.')))
    version_2_parts = list(map(int, version2.split('.')))

    max_length = max(len(version_1_parts), len(version_2_parts))

    version_1_parts.extend([0] * (max_length - len(version_1_parts)))
    version_2_parts.extend([0] * (max_length - len(version_2_parts)))

    for i in range(max_length):
        if version_1_parts[i] > version_2_parts[i]:
            return 1
        elif version_1_parts[i] < version_2_parts[i]:
            return -1

    return 0
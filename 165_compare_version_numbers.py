'''
Given two version strings version1 and version2, compare them.
A version string consists of revisions separated by dots '.'. Each revision is treated as an integer, ignoring any leading zeros.

To compare version strings:
+ Compare each revision from left to right.
+ If one version has fewer revisions, treat the missing ones as 0.

Return:
+ -1 if version1 < version2
+ 1 if version1 > version2
+ 0 if they are equal

Examples:
Input: version1 = "1.2", version2 = "1.10"
Output: -1

Input: version1 = "1.01", version2 = "1.001"
Output: 0

Даны две строки version1 и version2, представляющие версии.
Версия состоит из числовых ревизий, разделённых точками '.'. Каждую ревизию нужно интерпретировать как целое число, игнорируя ведущие нули.

Сравнение выполняется:
+ Слева направо, по каждой ревизии.
+ Если в одной версии ревизий меньше, недостающие считаются равными 0.

Верните:
+ -1, если version1 < version2
+ 1, если version1 > version2
+ 0, если версии равны

Примеры:
Ввод: version1 = "1.2", version2 = "1.10"
Вывод: -1

Ввод: version1 = "1.01", version2 = "1.001"
Вывод: 0
'''

def compare_version(version1: str, version2: str) -> int:
    v1_parts = list(map(int, version1.split('.')))
    v2_parts = list(map(int, version2.split('.')))

    max_length = max(len(v1_parts), len(v2_parts))

    v1_parts.extend([0] * (max_length - len(v1_parts)))
    v2_parts.extend([0] * (max_length - len(v2_parts)))

    for i in range(max_length):
        if v1_parts[i] > v2_parts[i]:
            return 1
        elif v1_parts[i] < v2_parts[i]:
            return -1

    return 0
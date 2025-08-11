'''
You are given a license key represented as a string S that consists only of alphanumeric characters and dashes (-). The string is separated into n + 1 groups by n dashes.
You are also given an integer k.
Your task is to reformat the string s so that:
    + Each group (except possibly the first one) contains exactly k characters;
    + The first group must contain at least one character and could be shorter than k;
    + Groups are separated by a single dash (-);
    + All lowercase letters should be converted to uppercase.

Return the reformatted license key.

Examples:
Input: S = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"

Input: S = "2-5g-3-J", k = 2
Output: "2-5G-3J"

Дан строковый ключ лицензии S, который состоит только из буквенно-цифровых символов и дефисов (-). Строка разделена на n + 1 групп с помощью n дефисов.
Также дано целое число k.
Необходимо отформатировать строку S так, чтобы:
    + Каждая группа (кроме, возможно, первой) содержала ровно k символов;
    + Первая группа содержала хотя бы один символ и могла быть короче k;
    + Группы разделялись одним дефисом (-);
    + Все строчные буквы были преобразованы в заглавные.

Верните отформатированный лицензионный ключ.

Примеры:
Ввод: S = "5F3Z-2e-9-w", k = 4
Вывод: "5F3Z-2E9W"

Ввод: S = "2-5g-3-J", k = 2
Вывод: "2-5G-3J"
'''

def license_key_formatting(S: str, k: int) -> str:
    S = S.replace('-', '').upper()
    size = len(S)
    first_group = size % k or k
    groups = [S[:first_group]]

    for i in range(first_group, size, k):
        groups.append(S[i:i+k])

    return '-'.join(groups)
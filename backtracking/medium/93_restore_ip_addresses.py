'''
You are given a string S consisting only of digits. Your task is to return all possible valid IP addresses that can be created by inserting exactly three dots into the string. You must not reorder or remove any digits.

A valid IP address:
    + Has exactly four integer parts, separated by dots;
    + Each part must be a number from 0 to 255;
    + Leading zeros are not allowed, except for the number 0 itself.

Return all valid IP addresses that can be formed from the string S, in any order.

Example:
Input: "25525511135"
Output: [   "255.255.11.135", 
            "255.255.111.35"
    ]

Дана строка S, содержащая только цифры. Нужно вернуть все возможные корректные IP-адреса, которые можно получить, вставляя ровно три точки в строку. Нельзя менять порядок символов или удалять их.

Корректный IP-адрес:
    + Состоит из четырёх чисел, разделённых точками;
    + Каждое число находится в диапазоне от 0 до 255;
    + Число не может начинаться с нуля, если оно не равно самому нулю.

Нужно вернуть все допустимые IP-адреса, которые можно составить из строки S, в любом порядке.

Пример:
Ввод: "25525511135"
Вывод: ["255.255.11.135", 
        "255.255.111.35"
    ]
'''

from typing import List

def restore_ip_addresses(S: str) -> List[str]:
    result = []

    def backtrack(start: int, path: List[str]):
        if len(path) == 4:
            if start == len(S):
                result.append(".".join(path))
            return

        for length in range(1, 4):
            if start + length > len(S):
                break
            segment = S[start:start + length]

            if (segment.startswith("0") and len(segment) > 1) or int(segment) > 255:
                continue

            backtrack(start + length, path + [segment])

    backtrack(0, [])
    return result
"""
You are given a string queryIP. Return:
    + "IPv4" if queryIP is a valid IPv4 address
    + "IPv6" if queryIP is a valid IPv6 address
    + "Neither" if queryIP is not a valid IP address of either type

IPv4 address:
    + Format: "x1.x2.x3.x4"
    + Each xi must be a decimal number from 0 to 255
    + No leading zeros allowed (e.g. "192.168.01.1" is invalid)
    + Must contain exactly 4 segments, separated by dots (.)

IPv6 address:
    + Format: "x1:x2:x3:x4:x5:x6:x7:x8"
    + Each xi must be a hexadecimal string of length 1 to 4
    + Valid characters: digits (0-9), letters (a-f, A-F)
    + Leading zeros are allowed
    + Must contain exactly 8 segments, separated by colons (:)

Examples:
Input: queryIP = "172.16.254.1"
Output: "IPv4"

Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"

Дана строка queryIP. Необходимо вернуть:
    + "IPv4", если queryIP — корректный IPv4-адрес
    + "IPv6", если queryIP — корректный IPv6-адрес
    + "Neither", если строка не является корректным IP-адресом ни одного типа

IPv4-адрес:
    + Формат: "x1.x2.x3.x4"
    + Каждое xi — десятичное число от 0 до 255
    + Запрещены ведущие нули (например, "192.168.01.1" — неверно)
    + Должно быть ровно 4 сегмента, разделённых точками (.)

IPv6-адрес:
    + Формат: "x1:x2:x3:x4:x5:x6:x7:x8"
    + Каждое xi — шестнадцатеричная строка длиной от 1 до 4 символов
    + Допустимые символы: цифры (0–9), буквы (a–f, A–F)
    + Ведущие нули разрешены
    + Должно быть ровно 8 сегментов, разделённых двоеточиями (:)

Примеры:
Ввод: queryIP = "172.16.254.1"
Вывод: "IPv4"

Ввод: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Вывод: "IPv6"
"""

class Solution:
    def validIPAddress(self, query_ip: str) -> str:
        if self.is_valid_ipv4(query_ip):
            return "IPv4"
        elif self.is_valid_ipv6(query_ip):
            return "IPv6"
        else:
            return "Neither"

    def is_valid_ipv4(self, ip_string: str) -> bool:
        ipv4_parts = ip_string.split(".")
        if len(ipv4_parts) != 4:
            return False
        for part in ipv4_parts:
            if not part.isdigit():
                return False
            if not 0 <= int(part) <= 255:
                return False
            if part[0] == '0' and len(part) > 1:
                return False
        return True

    def is_valid_ipv6(self, ip_string: str) -> bool:
        ipv6_parts = ip_string.split(":")
        if len(ipv6_parts) != 8:
            return False
        valid_hex_characters = "0123456789abcdefABCDEF"
        for part in ipv6_parts:
            if len(part) == 0 or len(part) > 4:
                return False
            for character in part:
                if character not in valid_hex_characters:
                    return False
        return True
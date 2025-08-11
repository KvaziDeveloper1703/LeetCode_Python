'''
Given a valid IPv4 address, return its defanged version.
A defanged IP address replaces every period "." with "[.]".

Examples:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

Дан корректный IPv4-адрес. Нужно вернуть его "обезвреженную" версию.
"Обезвреженный" IP-адрес получается путём замены каждой точки "." на строку "[.]".

Примеры:
Ввод: address = "1.1.1.1"
Вывод: "1[.]1[.]1[.]1"

Ввод: address = "255.100.50.0"
Вывод: "255[.]100[.]50[.]0"
'''

def defang_ip_address(address: str) -> str:
    return address.replace(".", "[.]")
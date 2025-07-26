'''
Every valid email address consists of two parts: a local name and a domain name, separated by the '@' symbol.

There are two special rules for the local name:
    + Dots (.) in the local name are ignored. For example, "alice.z@leetcode.com" is the same as "alicez@leetcode.com";
    + Plus (+) in the local name means everything after the first '+' is ignored. For example, "m.y+name@email.com" becomes "my@email.com".

These rules do not apply to the domain name.

Given an array of email addresses. You need to apply the above rules and return the number of unique email addresses that will actually receive the emails.

Examples:
Input: emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
Output: 2

Input: emails = ["a@leetcode.com","b@leetcode.com", "c@leetcode.com"]
Output: 3

Каждый корректный адрес электронной почты состоит из локального имени и домена, разделённых символом '@'.

Для локального имени действуют два правила:
    + Точки (.) в локальном имени игнорируются. Например, "alice.z@leetcode.com" и "alicez@leetcode.com" считаются одинаковыми;
    + Плюс (+) в локальном имени означает, что всё после первого '+' игнорируется. Например, "m.y+name@email.com" превращается в "my@email.com".

Эти правила не применяются к домену.

Дан массив строк emails, в который отправляются письма. Нужно вернуть количество уникальных электронных адресов, которые реально получат письма, с учётом указанных правил.

Примеры:
Ввод: emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
Вывод: 2

Ввод: emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
Вывод: 3
'''

from typing import List

def number_of_unique_emails(emails: List[str]) -> int:
    unique_emails = set()

    for email in emails:
        local, domain = email.split('@')
        local = local.split('+')[0]
        local = local.replace('.', '')
        normalized_email = f"{local}@{domain}"
        unique_emails.add(normalized_email)

    return len(unique_emails)
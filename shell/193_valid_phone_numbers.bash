: '
You are given a text file named file.txt that contains a list of phone numbers, one per line.
Write a one-line Bash script that prints only the valid phone numbers.

A valid phone number must match one of the following formats:
    - xxx-xxx-xxxx;
    - (xxx) xxx-xxxx.

You may assume:
    - Each line contains exactly one phone number;
    - There are no leading or trailing spaces in any line.

Example:
Input:
987-123-4567
123 456 7890
(123) 456-7890

Output:
987-123-4567
(123) 456-7890

Дан текстовый файл file.txt, содержащий список телефонных номеров.
Напишите однострочный Bash-скрипт, который выводит только корректные телефонные номера.

Корректный номер должен соответствовать одному из следующих форматов:
    - xxx-xxx-xxxx;
    - (xxx) xxx-xxxx.

Можно считать, что:
    - В каждой строке записан ровно один номер;
    - В строках нет пробелов в начале и в конце.

Пример:
Ввод:
987-123-4567
123 456 7890
(123) 456-7890

Вывод:
987-123-4567
(123) 456-7890
'

file_name="file.txt"
grep -E '^([0-9]{3}-[0-9]{3}-[0-9]{4}|\([0-9]{3}\) [0-9]{3}-[0-9]{4})$' "$file_name"
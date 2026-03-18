: '
You are given a text file named file.txt.
Write a one-line Bash script that prints only the 10th line of the file.

Example:
Input (file.txt):
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10

Output:
Line 10

Дан текстовый файл file.txt.
Напишите однострочный Bash-скрипт, который выводит только 10-ю строку файла.

Пример:
Ввод (file.txt):
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10

Вывод:
Line 10
'

file_name="file.txt"
sed -n '10p' "$file_name"
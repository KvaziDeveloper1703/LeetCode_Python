'''
You are given a phone number as a string number.

The string number consists of digits, spaces (' '), and/or dashes ('-').

You need to reformat the phone number according to these rules:
    - Remove all spaces and dashes;
    - Group the remaining digits from left to right into blocks of length 3 until there are 4 or fewer digits left;
    - The final digits are grouped as follows:
        - If there are 2 digits left → make one block of length 2;
        - If there are 3 digits left → make one block of length 3;
        - If there are 4 digits left → make two blocks of length 2 each.

Finally, join all blocks with dashes ('-').

The reformatting should never produce a block of length 1 and should have at most two blocks of length 2.

Return the formatted phone number.

Examples:
Input: number = "1-23-45 6"
Output: "123-456"

Input: number = "123 4-567"
Output: "123-45-67"

Дан номер телефона в виде строки number.

Строка number может содержать цифры, пробелы (' ') и/или дефисы ('-').

Нужно отформатировать номер телефона по следующим правилам:
    - Удалить все пробелы и дефисы;
    - Разделить оставшиеся цифры слева направо на блоки длиной по 3, пока не останется 4 или меньше цифр;
    - Последние цифры оформить так:
        - Если осталось 2 цифры → один блок из 2 цифр;
        - Если осталось 3 цифры → один блок из 3 цифр;
        - Если осталось 4 цифры → два блока по 2 цифры.

Затем соединить блоки дефисами ('-').

Форматирование не должно создавать блоков длиной 1 и должно содержать не более двух блоков длиной 2.

Верни отформатированный номер телефона.

Примеры:
Ввод: number = "1-23-45 6"
Вывод: "123-456"

Ввод: number = "123 4-567"
Вывод: "123-45-67"
'''

def reformat_number(number: str) -> str:
    cleaned_number = ""
    for character in number:
        if character.isdigit():
            cleaned_number += character

    blocks = []
    index = 0
    total_length = len(cleaned_number)

    while total_length - index > 4:
        current_block = cleaned_number[index:index + 3]
        blocks.append(current_block)
        index += 3

    remaining_digits = cleaned_number[index:]

    if len(remaining_digits) == 2 or len(remaining_digits) == 3:
        blocks.append(remaining_digits)
    elif len(remaining_digits) == 4:
        blocks.append(remaining_digits[0:2])
        blocks.append(remaining_digits[2:4])

    return "-".join(blocks)
'''
You are given two strings, key and message, where:
    - key represents a cipher key;
    - message represents an encrypted message.

To decode the message, follow these steps:
    - From the string key, take the first occurrence of each of the 26 lowercase English letters, ignoring spaces;
    - Use these letters to form a substitution table, preserving their order of appearance;
    - Align this substitution table with the regular English alphabet ('a' to 'z'), so that:
        - the first unique letter in key maps to 'a';
        - the second unique letter maps to 'b';
        - and so on.
    - Decode the message by replacing each letter using the substitution table;
    - Spaces ' ' in the message remain unchanged.

Return the decoded message.

Examples:
Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
Output: "this is a secret"

Input: key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
Output: "the five boxing wizards jump quickly"

Даны две строки key и message, где:
    - key - это ключ шифра;
    - message - это зашифрованное сообщение.

Чтобы расшифровать сообщение, выполните следующие шаги:
    - Из строки key возьмите первое вхождение каждой из 26 строчных букв английского алфавита, игнорируя пробелы;
    - Используйте эти буквы (в порядке их появления) для построения таблицы подстановки;
    - Совместите таблицу подстановки с обычным английским алфавитом ('a'–'z'), так что:
        - первая уникальная буква из key соответствует 'a';
        - вторая - 'b';
        - и так далее.
    - Расшифруйте строку message, заменяя каждую букву согласно таблице подстановки;
    - Пробелы ' ' в сообщении остаются без изменений.

Верните расшифрованное сообщение.

Примеры:
Ввод: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
Вывод: "this is a secret"

Ввод: key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
Вывод: "the five boxing wizards jump quickly"
'''
def decode_message(key: str, message: str) -> str:
    substitution_mapping = {}
    next_plaintext_code = ord('a')

    for character in key:
        if character != ' ' and character not in substitution_mapping:
            substitution_mapping[character] = chr(next_plaintext_code)
            next_plaintext_code += 1

    decoded_characters = []
    for character in message:
        if character == ' ':
            decoded_characters.append(' ')
        else:
            decoded_characters.append(substitution_mapping[character])

    return ''.join(decoded_characters)
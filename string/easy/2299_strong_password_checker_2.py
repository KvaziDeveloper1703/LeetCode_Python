'''
A password is considered strong if it satisfies all of the following conditions:
    - It contains at least 8 characters;
    - It contains at least one lowercase letter;
    - It contains at least one uppercase letter;
    - It contains at least one digit;
    - It contains at least one special character. The allowed special characters are: "!@#$%^&*()-+";
    - It does not contain two identical characters in adjacent positions.

Given a string password, return True if the password is strong. Otherwise, return False.

Examples:
Input: password = "IloveLe3tcode!"
Output: True

Input: password = "Me+You--IsMyDream"
Output: False

Пароль считается надёжным, если он удовлетворяет всем следующим условиям:
    - Он содержит не менее 8 символов;
    - Он содержит хотя бы одну строчную букву;
    - Он содержит хотя бы одну заглавную букву;
    - Он содержит хотя бы одну цифру;
    - Он содержит хотя бы один специальный символ. Допустимые специальные символы: "!@#$%^&*()-+";
    - В пароле нет двух одинаковых символов, стоящих подряд.
    - По заданной строке password необходимо определить, является ли пароль надёжным.

Верните True, если пароль надёжный, и False - в противном случае.

Примеры:
Ввод: password = "IloveLe3tcode!"
Вывод: True

Ввод: password = "Me+You--IsMyDream"
Вывод: False
'''

def strong_password_checker(password: str) -> bool:
    if len(password) < 8:
        return False

    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-+"

    for index in range(len(password)):
        character = password[index]

        if character.islower():
            has_lowercase = True
        elif character.isupper():
            has_uppercase = True
        elif character.isdigit():
            has_digit = True
        elif character in special_characters:
            has_special = True

        if index > 0 and character == password[index - 1]:
            return False

    return (has_lowercase and has_uppercase and has_digit and has_special)
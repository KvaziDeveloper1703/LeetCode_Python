'''
A sentence consists only of lowercase letters, digits, hyphens, punctuation marks, and spaces.
The sentence can be split into one or more tokens, separated by one or more spaces.

A token is considered a valid word if all of the following conditions are satisfied:
    - It contains only lowercase letters, hyphens, and/or punctuation marks - no digits;
    - It contains at most one hyphen. If a hyphen appears, it must be surrounded by lowercase letters;
    - It contains at most one punctuation mark, and if present, it must appear only at the end of the token.

Examples of valid words include: "a-b.", "afad", "ba-c", "a!", and "!".

Given a string sentence, return the number of valid words in it.

Предложение состоит только из строчных букв, цифр, дефисов, знаков пунктуации и пробелов.
Предложение можно разбить на один или несколько токенов, разделённых одним или несколькими пробелами.

Токен считается корректным словом, если выполняются все следующие условия:
    - Он содержит только строчные буквы, дефисы и/или знаки пунктуации — цифр быть не должно;
    - В нём не более одного дефиса. Если дефис присутствует, он должен быть окружён строчными буквами;
    - В нём не более одного знака пунктуации, и если он есть, он должен находиться только в конце токена.

Примеры корректных слов: "a-b.", "afad", "ba-c", "a!", "!".

Дана строка sentence. Верните количество корректных слов в этом предложении.
'''

def count_valid_words(sentence: str) -> int:
    def is_valid_word(token: str) -> bool:
        if not token:
            return False

        hyphen_character_count = 0
        punctuation_character_count = 0

        for token_character_index, token_character in enumerate(token):
            if token_character.isdigit():
                return False

            if token_character == '-':
                hyphen_character_count += 1
                if hyphen_character_count > 1:
                    return False
                if token_character_index == 0 or token_character_index == len(token) - 1:
                    return False
                if not (token[token_character_index - 1].isalpha() and token[token_character_index + 1].isalpha()):
                    return False

            if token_character in "!.,":  
                punctuation_character_count += 1
                if punctuation_character_count > 1:
                    return False
                if token_character_index != len(token) - 1:
                    return False

            if token_character.isalpha() or token_character in "-!.,":  
                continue

            return False

        return True

    list_of_tokens = sentence.split()
    number_of_valid_words = 0

    for token in list_of_tokens:
        if is_valid_word(token):
            number_of_valid_words += 1

    return number_of_valid_words
"""
You are given a string title that contains one or more words separated by a single space. Each word consists only of English letters.

Capitalize the title according to these rules:
    - If a word has 1 or 2 letters, convert all its letters to lowercase;
    - Otherwise, capitalize the first letter and make all remaining letters lowercase.

Return the transformed title.

Examples:
Input: title = "capiTalIze tHe titLe"
Output: "Capitalize The Title"

Input: title = "First leTTeR of EACH Word"
Output: "First Letter of Each Word"

Дана строка title, содержащая одно или несколько слов, разделённых одиночным пробелом. Каждое слово состоит только из английских букв.

Необходимо преобразовать строку так:
    - Если слово содержит 1 или 2 буквы, сделать все буквы строчными;
    - Иначе - сделать первую букву заглавной, а остальные - строчными.

Верните преобразованный заголовок.

Примеры:
Ввод: title = "capiTalIze tHe titLe"
Вывод: "Capitalize The Title"

Ввод: title = "First leTTeR of EACH Word"
Вывод: "First Letter of Each Word"
"""

def capitalize_title(title: str) -> str:
    title_words = title.split()
    transformed_words = []

    for word in title_words:
        if len(word) <= 2:
            transformed_words.append(word.lower())
        else:
            transformed_words.append(word[0].upper() + word[1:].lower())

    final_title = " ".join(transformed_words)
    return final_title
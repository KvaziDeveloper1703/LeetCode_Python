'''
You are given two strings S and T. Determine if they are isomorphic.
Two strings are isomorphic if the characters in S can be replaced to get T, with the following rules:
+ Every occurrence of a character in S must be replaced with the same character in T;
+ The character mapping must preserve the order of characters;
+ No two characters in S can map to the same character in T, but a character can map to itself.

Examples:
Input: S = "egg", T = "add"
Output: true

Input: S = "foo", T = "bar"
Output: false

Даны две строки S и T. Необходимо определить, являются ли они изоморфными.
Две строки считаются изоморфными, если символы в строке S можно заменить, чтобы получить строку T, при соблюдении следующих условий:
+ Каждое вхождение символа из S должно заменяться одним и тем же символом из T;
+ Порядок символов должен сохраняться;
+ Два разных символа из S не могут отображаться в один и тот же символ из T, но один символ может отображаться сам на себя.

Примеры:
Ввод: S = "egg", T = "add"
Вывод: true

Ввод: S = "foo", T = "bar"
Вывод: false
'''

def is_isomorphic(S: str, T: str) -> bool:
    if len(S) != len(T):
        return False

    mapping_st = {}
    mapping_ts = {}

    for source_character, target_character in zip(S, T):
        if source_character in mapping_st:
            if mapping_st[source_character] != target_character:
                return False
        else:
            mapping_st[source_character] = target_character

        if target_character in mapping_ts:
            if mapping_ts[target_character] != source_character:
                return False
        else:
            mapping_ts[target_character] = source_character

    return True
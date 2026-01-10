'''
You are given a string word consisting of distinct lowercase English letters.

A telephone keypad contains keys numbered from 2 to 9, each of which can be mapped to a distinct set of lowercase letters. To type a letter assigned to a key, the key must be pressed a certain number of times:
    - the first letter on a key requires one push,
    - the second letter requires two pushes,
    - the third letter requires three pushes, and so on.

You are allowed to remap the letters to the keys numbered 2 through 9 under the following rules:
    - Each letter must be mapped to exactly one key;
    - Each key may be mapped to any number of letters;
    - Keys 1, 0, *, and # do not map to any letters.

Your task is to determine the minimum total number of key presses required to type the string word after optimally remapping the letters to the keys.

Return the minimum number of pushes needed.

Examples:
Input: word = "abcde"
Output: 5

Input: word = "xycdefghij"
Output: 12

Вам дана строка word, состоящая из различных строчных букв английского алфавита.

На телефонной клавиатуре клавиши с номерами от 2 до 9 могут быть сопоставлены с уникальными наборами букв.

Чтобы напечатать букву, назначенную на клавишу:
    - первая буква требует одно нажатие,
    - вторая - два нажатия,
    - третья - три нажатия, и так далее.

Разрешается переназначить буквы на клавиши с номерами от 2 до 9, соблюдая следующие условия:
    - Каждая буква должна быть назначена ровно на одну клавишу;
    - Каждой клавише можно назначить любое количество букв;
    - Клавиши 1, 0, * и # не соответствуют никаким буквам.

Необходимо определить минимальное общее количество нажатий клавиш, требуемое для ввода строки word при оптимальном распределении букв по клавишам.

Верните минимальное количество нажатий.

Примеры:
Ввод: word = "abcde"
Вывод: 5

Ввод: word = "xycdefghij"
Вывод: 12
'''

def minimum_pushes(word: str) -> int:
    pushes = 0

    for i in range(len(word)):
        pushes += i // 8 + 1

    return pushes
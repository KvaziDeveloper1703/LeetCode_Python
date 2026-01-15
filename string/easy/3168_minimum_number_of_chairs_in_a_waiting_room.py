'''
You are given a string s. Each character represents an event happening every second i:
    - If s[i] == 'E', a person enters the waiting room and takes a chair;
    - If s[i] == 'L', a person leaves the waiting room, freeing a chair.

The waiting room is initially empty.

Return the minimum number of chairs needed so that a chair is always available for every person who enters the room.

Дана строка s. Каждый символ описывает событие, происходящее каждую секунду i:
    - Если s[i] == 'E', человек заходит в зал ожидания и занимает стул;
    - Если s[i] == 'L', человек выходит из зала ожидания, освобождая стул.

Изначально зал ожидания пустой.

Нужно вернуть минимальное количество стульев, чтобы стул всегда был доступен каждому входящему человеку.
'''

def minimum_chairs(s: str) -> int:
    current_people = 0
    maximum_people = 0

    for event in s:
        if event == 'E':
            current_people += 1
            maximum_people = max(maximum_people, current_people)
        else:
            current_people -= 1

    return maximum_people
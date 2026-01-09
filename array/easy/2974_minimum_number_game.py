'''
You are given a 0-indexed integer array numbers of even length.

Alice and Bob play a game that consists of several rounds. During the game, an initially empty array called result_array is formed.

The rules of the game are as follows:
    - At the beginning, the array numbers is sorted in ascending order;
    - The game proceeds in rounds, where each round processes two elements:
        - alice_removed_number is the current minimum element;
        - bob_removed_number is the next minimum element.
    - Bob appends bob_removed_number to result_array first;
    - Alice then appends alice_removed_number to result_array.

This process continues until all elements from numbers are used.

Return the resulting array result_array.

Examples:
Input: numbers = [5,4,2,3]
Output: [3,2,5,4]

Input: numbers = [2,5]
Output: [5,2]

Дан целочисленный массив numbers с индексацией от 0 и чётной длиной.

Алиса и Боб играют в игру, в ходе которой формируется изначально пустой массив result_array.

Правила игры:
    - В начале массив numbers сортируется по возрастанию;
    - Игра проходит по раундам, где за один раунд обрабатываются два элемента:
        - alice_removed_number - текущий минимальный элемент;
        - bob_removed_number - следующий минимальный элемент.
    - Сначала Боб добавляет bob_removed_number в result_array;
    - Затем Алиса добавляет alice_removed_number в result_array.

Игра продолжается до тех пор, пока все элементы массива numbers не будут использованы.

Необходимо вернуть итоговый массив result_array.

Примеры:
Ввод: numbers = [5,4,2,3]
Вывод: [3,2,5,4]

Ввод: numbers = [2,5]
Вывод: [5,2]
'''

def number_game(numbers):
    numbers.sort()
    result_array = []

    for index in range(0, len(numbers), 2):
        alice_removed_number = numbers[index]
        bob_removed_number = numbers[index + 1]

        result_array.append(bob_removed_number)
        result_array.append(alice_removed_number)

    return result_array
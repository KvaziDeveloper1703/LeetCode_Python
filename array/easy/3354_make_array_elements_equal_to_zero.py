'''
You are given an integer array numbers of length arrayLength.
First, choose a starting position currentPosition such that numbers[currentPosition] == 0.
Then choose an initial movement direction movementDirection, which can be either left or right.

After that, repeatedly perform the following process:
    - If currentPosition goes out of the range [0, arrayLength - 1], the process ends.
    - If numbers[currentPosition] == 0, move one step in the current direction:
        - increase currentPosition by 1 if moving right;
        - decrease currentPosition by 1 if moving left.
    - If numbers[currentPosition] > 0:
        - decrement numbers[currentPosition] by 1;
        - reverse the movement direction;
        - take one step in the new direction.

A choice of the starting position currentPosition and the initial movement direction is considered valid if all elements in numbers become 0 by the end of the process.
Return the number of possible valid selections.

Examples:
Input: numbers = [1,0,2,0,3]
Output: 2

Input: numbers = [2,3,4,0,4,1,0]
Output: 0

Дан целочисленный массив numbers длины arrayLength.
Сначала необходимо выбрать начальную позицию currentPosition такую, что numbers[currentPosition] == 0.
Затем выбирается начальное направление движения movementDirection, которое может быть влево или вправо.

После этого многократно выполняется следующий процесс:
    - Если currentPosition выходит за пределы диапазона [0, arrayLength - 1], процесс завершается.
    - Если numbers[currentPosition] == 0, выполняется шаг в текущем направлении:
        - currentPosition увеличивается на 1 при движении вправо;
        - currentPosition уменьшается на 1 при движении влево.
    - Если numbers[currentPosition] > 0:
        - значение numbers[currentPosition] уменьшается на 1;
        - направление движения меняется на противоположное;
        - выполняется один шаг в новом направлении.

Выбор начальной позиции currentPosition и направления движения считается корректным, если к моменту завершения процесса все элементы массива numbers равны 0.
Необходимо вернуть количество возможных корректных вариантов выбора.

Примеры:
Ввод: numbers = [1,0,2,0,3]
Вывод: 2

Ввод: numbers = [2,3,4,0,4,1,0]
Вывод: 0
'''

from typing import List

def count_valid_selections(nums: List[int]) -> int:
    total_sum = sum(nums)
    left_part_sum = 0
    valid_selections_count = 0

    for index in range(len(nums)):
        if nums[index] == 0:
            right_part_sum = total_sum - left_part_sum
            difference = abs(left_part_sum - right_part_sum)

            if difference == 0:
                valid_selections_count += 2
            elif difference == 1:
                valid_selections_count += 1

        left_part_sum += nums[index]

    return valid_selections_count
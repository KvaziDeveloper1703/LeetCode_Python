'''
You are given two integers red and blue, representing the number of red and blue balls.

You need to arrange these balls into a triangle such that:
    - The 1st row contains 1 ball,
    - The 2nd row contains 2 balls,
    - The 3rd row contains 3 balls,
    - and so on...

Additional rules:
    - All balls in the same row must be the same color;
    - Two neighboring rows must have different colors.

Return the maximum possible height of the triangle that can be formed.

Examples:
Input: red = 2, blue = 4
Output: 3

Input: red = 2, blue = 1
Output: 2

Даны два целых числа red и blue - количество красных и синих шариков.

Нужно выложить из них треугольник по следующим правилам:
    - в 1-й строке должно быть 1 шарик,
    - во 2-й строке - 2 шарика,
    - в 3-й строке - 3 шарика,
    - и так далее...

Дополнительные условия:
    - все шарики в одной строке должны быть одного цвета;
    - соседние строки должны быть разных цветов.

Нужно вернуть максимальную возможную высоту треугольника.

Примеры:
Ввод: red = 2, blue = 4
Вывод: 3

Ввод: red = 2, blue = 1
Вывод: 2
'''

def max_height_of_triangle(red: int, blue: int) -> int:
    def buildTriangle(startWithRed: bool) -> int:
        redBalls = red
        blueBalls = blue
        height = 1

        while True:
            if startWithRed:
                if redBalls < height:
                    break
                redBalls -= height
            else:
                if blueBalls < height:
                    break
                blueBalls -= height

            startWithRed = not startWithRed
            height += 1

        return height - 1

    return max(buildTriangle(True), buildTriangle(False))
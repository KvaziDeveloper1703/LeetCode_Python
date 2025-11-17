'''
You work in a ball factory that produces balls numbered from lowLimit to highLimit, inclusive.
There are infinitely many boxes, each labeled with a positive integer starting from 1.

Your task is to place each ball into a box whose number equals the sum of the digits of the ball’s number.

Example:
    - Ball 321 goes into box 3 + 2 + 1 = 6
    - Ball 10 goes into box 1 + 0 = 1

After placing all balls into their corresponding boxes, return the maximum number of balls found in any single box.

Вы работаете на фабрике, где производят мячи с номерами от lowLimit до highLimit включительно.
Так же есть бесконечное количество коробок, пронумерованных от 1 и далее.

Ваша задача - положить каждый мяч в коробку с номером, который равен сумме цифр номера мяча.

Пример:
    - Мяч 321 кладётся в коробку 3 + 2 + 1 = 6
    - Мяч 10 кладётся в коробку 1 + 0 = 1

После того как все мячи разложены по коробкам, нужно вернуть наибольшее количество мячей в одной коробке.
'''
from collections import defaultdict

def count_balls(lowLimit: int, highLimit: int) -> int:
    box_to_balls_count = defaultdict(int)

    for ball_number in range(lowLimit, highLimit + 1):
        digit_sum = 0
        current_number = ball_number

        while current_number > 0:
            digit_sum += current_number % 10
            current_number //= 10

        box_to_balls_count[digit_sum] += 1

    max_balls_in_box = 0
        
    for balls_count in box_to_balls_count.values():
        if balls_count > max_balls_in_box:
            max_balls_in_box = balls_count

    return max_balls_in_box
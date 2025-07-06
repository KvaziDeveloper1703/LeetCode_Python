"""
Given an integer N, return a string array answer where:
+ answer[i] == "FizzBuzz" if i is divisible by both 3 and 5;
+ answer[i] == "Fizz" if i is divisible by 3;
+ answer[i] == "Buzz" if i is divisible by 5;
+ answer[i] == i if none of the above conditions are met.

Return the array for all integers from 1 to N.

Examples:
Input: n = 3
Output: ["1", "2", "Fizz"]

Input: n = 5
Output: ["1", "2", "Fizz", "4", "Buzz"]

Дано целое число N. Необходимо вернуть массив строк answer, где:
+ answer[i] == "FizzBuzz", если число делится и на 3, и на 5;
+ answer[i] == "Fizz", если число делится только на 3;
+ answer[i] == "Buzz", если число делится только на 5;
+ answer[i] == i (в виде строки), если ни одно из условий не выполняется.

Верните массив для всех целых чисел от 1 до N включительно.

Примеры:
Вход: n = 3
Выход: ["1", "2", "Fizz"]

Вход: n = 5
Выход: ["1", "2", "Fizz", "4", "Buzz"]
"""

def fizz_buzz(limit: int) -> list[str]:
    fizz_buzz_result = []

    for current_number in range(1, limit + 1):
        if current_number % 3 == 0 and current_number % 5 == 0:
            fizz_buzz_result.append("FizzBuzz")
        elif current_number % 3 == 0:
            fizz_buzz_result.append("Fizz")
        elif current_number % 5 == 0:
            fizz_buzz_result.append("Buzz")
        else:
            fizz_buzz_result.append(str(current_number))

    return fizz_buzz_result
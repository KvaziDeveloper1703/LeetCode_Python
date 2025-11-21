'''
You are given a 2D integer array logs, where each element logs[i] = [birthᵢ, deathᵢ] represents the birth year and death year of the i-th person.

A person is considered alive during every year x in the interval [birthᵢ, deathᵢ − 1]. They are not counted as alive in the year they die.

The population of a year x is the number of people who are alive during that year.

Your task is to return the earliest year that has the maximum population.

Дан двумерный массив целых чисел logs, где каждый элемент logs[i] = [birthᵢ, deathᵢ] обозначает год рождения и год смерти i-го человека.

Человек считается живым в каждый год x, который принадлежит диапазону [birthᵢ, deathᵢ − 1]. В год смерти человек не считается живым.

Население года x - это количество людей, которые живы в этот год.

Требуется вернуть самый ранний год, в котором население достигает максимального значения.
'''

from typing import List

def maximum_population(logs: List[List[int]]) -> int:
    population_difference = [0] * 2051

    for birth_year, death_year in logs:
        population_difference[birth_year] += 1
        population_difference[death_year] -= 1

    max_population = 0
    earliest_year_with_max_population = 1950
    current_population = 0

    for year in range(1950, 2051):
        current_population += population_difference[year]
        if current_population > max_population:
            max_population = current_population
            earliest_year_with_max_population = year

    return earliest_year_with_max_population
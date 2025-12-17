'''
You are participating in a competition and start with two positive integers:
    - initialEnergy - your initial energy;
    - initialExperience - your initial experience.

You are also given two 0-indexed integer arrays energy and experience, each of length n, where:
    - energy[i] is the energy of the i-th opponent;
    - experience[i] is the experience of the i-th opponent.

You will face the n opponents in order. To defeat the i-th opponent and proceed to the next one (if any), both your current energy and experience must be strictly greater than those of the opponent.

When you defeat the i-th opponent:
    - your energy decreases by energy[i];
    - your experience increases by experience[i].

Before the competition begins, you may train for any number of hours. After each hour of training, you may choose one of the following:
    - increase your initial energy by 1, or
    - increase your initial experience by 1.

Your task is to determine the minimum number of training hours required so that you can defeat all opponents.

Return this minimum number.

Вы участвуете в соревновании и начинаете с двух положительных целых чисел:
    - initialEnergy - ваша начальная энергия;
    - initialExperience - ваш начальный опыт.

Также даны два массива с нулевой индексацией energy и experience длины n, где:
    - energy[i] - энергия i-го противника;
    - experience[i] - опыт i-го противника.

Вы сражаетесь с n противниками по порядку. Чтобы победить i-го противника и перейти к следующему (если он есть), и ваша энергия, и ваш опыт должны быть строго больше, чем у этого противника.

После победы над i-м противником:
    - ваша энергия уменьшается на energy[i]
    - ваш опыт увеличивается на experience[i]

Перед началом соревнования вы можете тренироваться любое количество часов. За каждый час тренировки вы можете выбрать одно из двух действий:
    - увеличить начальную энергию на 1, или
    - увеличить начальный опыт на 1.

Необходимо найти минимальное количество часов тренировки, достаточное для того, чтобы победить всех противников.

Верните это минимальное количество.
'''

from typing import List

def min_number_of_hours(initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
    training_hours = 0
    current_energy = initialEnergy
    current_experience = initialExperience

    for index in range(len(energy)):
        if current_energy <= energy[index]:
            needed_energy = energy[index] - current_energy + 1
            training_hours += needed_energy
            current_energy += needed_energy

        if current_experience <= experience[index]:
            needed_experience = experience[index] - current_experience + 1
            training_hours += needed_experience
            current_experience += needed_experience

        current_energy -= energy[index]
        current_experience += experience[index]

    return training_hours
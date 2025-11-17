'''
You are given an array items, where each element items[i] = [typeᵢ, colorᵢ, nameᵢ] represents the type, color, and name of the i-th item.

You are also given a rule defined by two strings: ruleKey and ruleValue.

An item matches the rule if one of the following is true:
    - ruleKey == "type" and ruleValue == typeᵢ
    - ruleKey == "color" and ruleValue == colorᵢ
    - ruleKey == "name" and ruleValue == nameᵢ

Return the number of items that satisfy the given rule.

Examples:
Input: items = [["phone","blue","pixel"], ["computer","silver","lenovo"], ["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Output: 1

Input: items = [["phone","blue","pixel"], ["computer","silver","phone"], ["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
Output: 2

Дан массив items, где каждый элемент items[i] = [typeᵢ, colorᵢ, nameᵢ] описывает тип, цвет и название i-го предмета.

Также даны две строки: ruleKey и ruleValue, задающие правило.

Предмет считается подходящим под правило, если выполняется одно из условий:
    - ruleKey == "type" и ruleValue == typeᵢ
    - ruleKey == "color" и ruleValue == colorᵢ
    - ruleKey == "name" и ruleValue == nameᵢ

Верните количество предметов, которые соответствуют правилу.

Примеры:
Ввод: items = [["phone","blue","pixel"], ["computer","silver","lenovo"], ["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Вывод: 1

Ввод: items = [["phone","blue","pixel"], ["computer","silver","phone"], ["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
Вывод: 2
'''

from typing import List

def count_matches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    key_index = {
        "type": 0,
        "color": 1,
        "name": 2
    }

    index = key_index[ruleKey]
    count = 0

    for item in items:
        if item[index] == ruleValue:
            count += 1

    return count
'''
You are given a string s that represents a student's attendance record. Each character in the string stands for the student's attendance status on a particular day:
    + 'A': Absent
    + 'L': Late
    + 'P': Present

The student is eligible for an attendance award if both of the following conditions are satisfied:
    + The student was absent ('A') on fewer than 2 days in total.
    + The student was never late ('L') for 3 or more consecutive days.

Return true if the student is eligible for the award, or false otherwise.

Examples:
Input: s = "PPALLP"
Output: true

Input: s = "PPALLL"
Output: false

Дана строка s, представляющая посещаемость студента. Каждый символ в строке обозначает статус посещения в конкретный день:
    + 'A': отсутствовал (Absent)
    + 'L': опоздал (Late)
    + 'P': присутствовал (Present)

Студент получает награду за посещаемость, если одновременно выполняются два условия:
    + Студент отсутствовал ('A') менее чем 2 дня всего.
    + Студент никогда не опаздывал ('L') 3 или более дней подряд.

Необходимо вернуть true, если студент получает награду, и false — в противном случае.

Примеры:
Ввод: s = "PPALLP"
Вывод: true

Ввод: s = "PPALLL"
Вывод: false
'''

def check_record(self, s: str) -> bool:
    if s.count('A') >= 2:
        return False
    if 'LLL' in s:
        return False
    return True
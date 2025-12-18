'''
Alice and Bob are traveling to Rome for separate business trips.

You are given four strings: arriveAlice, leaveAlice, arriveBob, and leaveBob.
    - Alice will be in Rome from the date arriveAlice to the date leaveAlice, inclusive.
    - Bob will be in Rome from the date arriveBob to the date leaveBob, inclusive.

Each date is given as a 5-character string in the format "MM-DD", where:
    - MM represents the month,
    - DD represents the day.

All dates occur within the same calendar year, which is not a leap year.

Your task is to return the total number of days during which both Alice and Bob are in Rome at the same time.

The number of days in each month is as follows: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

Алиса и Боб отправляются в Рим по отдельным деловым поездкам.

Вам даны четыре строки: arriveAlice, leaveAlice, arriveBob и leaveBob.
    - Алиса будет находиться в Риме с даты arriveAlice по дату leaveAlice включительно.
    - Боб будет находиться в Риме с даты arriveBob по дату leaveBob включительно.

Каждая дата представлена строкой из 5 символов в формате "MM-DD", где:
    - MM - номер месяца,
    - DD - номер дня.

Все даты относятся к одному календарному году, который не является високосным.

Необходимо определить и вернуть общее количество дней, в течение которых Алиса и Боб одновременно находятся в Риме.

Количество дней в каждом месяце задано следующим массивом: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].
'''

def count_days_together(arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def day_of_year(date: str) -> int:
        month = int(date[:2])
        day = int(date[3:])
        return sum(days_in_month[:month - 1]) + day

    alice_start = day_of_year(arriveAlice)
    alice_end = day_of_year(leaveAlice)
    bob_start = day_of_year(arriveBob)
    bob_end = day_of_year(leaveBob)

    start_together = max(alice_start, bob_start)
    end_together = min(alice_end, bob_end)

    return max(0, end_together - start_together + 1)
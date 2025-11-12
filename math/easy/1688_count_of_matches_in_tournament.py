'''
You are given an integer n, representing the number of teams in a tournament that follows unusual rules:
    - If the current number of teams is even, each team is paired with another team. → A total of n / 2 matches are played, and n / 2 teams advance to the next round.
    - If the current number of teams is odd, one team automatically advances to the next round, and the rest are paired. → A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance.

Return the total number of matches played in the tournament until one winner remains.

Examples:
Input: n = 7
Output: 6

Input: n = 14
Output: 13

Дано целое число n, обозначающее количество команд в турнире с необычными правилами:
    - Если число команд чётное, каждая команда образует пару с другой. → Всего проводится n / 2 матчей, и n / 2 команд проходят в следующий раунд.
    - Если число команд нечётное, одна команда автоматически проходит дальше, а остальные образуют пары. → Всего проводится (n - 1) / 2 матчей, и (n - 1) / 2 + 1 команд проходят дальше.

Нужно вернуть общее количество матчей, сыгранных в турнире до определения победителя.

Примеры:
Ввод: n = 7
Вывод: 6

Ввод: n = 14
Вывод: 13
'''

def number_of_matches(n: int) -> int:
    total_matches = 0
    current_teams = n

    while current_teams > 1:
        if current_teams % 2 == 0:
            matches_this_round = current_teams // 2
            teams_next_round = current_teams // 2
        else:
            matches_this_round = (current_teams - 1) // 2
            teams_next_round = matches_this_round + 1

        total_matches += matches_this_round
        current_teams = teams_next_round

    return total_matches
import threading
import time

import requests


def get_total_goals(team: str, year: int) -> int:
    def get_goals_by_page(team: str, year: int, page: int, home: bool):
        nonlocal total_goals, lock
        if home:
            team_goals = 'team1goals'
            query = f'year={year}&team1={team}&page={page}'
        else:
            team_goals = 'team2goals'
            query = f'year={year}&team2={team}&page={page}'
        response = requests.get(f'{base_url}?{query}').json()
        for data in response['data']:
            lock.acquire()
            total_goals += int(data[team_goals])
            lock.release()

    base_url = 'https://jsonmock.hackerrank.com/api/football_matches'
    total_goals = 0
    lock = threading.Lock()

    team1_response = requests.get(f'{base_url}?year={year}&team1={team}').json()
    team2_response = requests.get(f'{base_url}?year={year}&team2={team}').json()
    team1_total_pages, team2_total_pages = team1_response['total_pages'], team2_response['total_pages'],

    thread_pool = []
    for i in range(1, team1_total_pages + 1):
        thread = threading.Thread(target=get_goals_by_page, args=(team, year, i, True,))
        thread_pool.append(thread)
        thread.start()

    for i in range(1, team2_total_pages + 1):
        thread = threading.Thread(target=get_goals_by_page, args=(team, year, i, False,))
        thread_pool.append(thread)
        thread.start()

    for th in thread_pool:
        th.join()

    return total_goals


start = time.time()
# goals = get_total_goals('Barcelona', 2011)
goals = get_total_goals('Chelsea', 2011)
print("Total Goals: ", goals)
end = time.time()
print(end - start, "sec")

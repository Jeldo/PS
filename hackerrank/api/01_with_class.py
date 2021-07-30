import http
import logging
import threading
import time
from typing import List

import requests


class MatchRecord:
    def __init__(self, competition: str, year: int, round: str, team1: str, team2: str, team1goals: str,
                 team2goals: str):
        self.competition = competition
        self.year = year
        self.round = round
        self.team1 = team1
        self.team2 = team2
        self.team1_goals = int(team1goals)
        self.team2_goals = int(team2goals)


class PageResponse:
    def __init__(self, page: int, per_page: int, total: int, total_pages: int, data: List[dict]):
        self.page = page
        self.per_page = per_page
        self.total = total
        self.total_pages = total_pages
        self.data = []
        for d in data:
            self.data.append(MatchRecord(**d))


BASE_URL = 'https://jsonmock.hackerrank.com/api/football_matches'
LOGGER = logging.getLogger()


def get_total_goals(team: str, year: int) -> int:
    def get_team_page(side: str, team: str, year: int, page: int = 1) -> PageResponse:
        try:
            if not page:
                res = requests.get(BASE_URL + f'?year={year}&{side}={team}')
            else:
                res = requests.get(BASE_URL + f'?year={year}&{side}={team}&page={page}')
        except requests.HTTPError as http_err:
            LOGGER.exception("error while sending a request")
            # LOGGER.error('error while sending a request')
            return None
        # TODO: handle http errors
        if res.status_code != http.HTTPStatus.OK:
            return None

        return PageResponse(**res.json())

    def get_goals_by_page(year: int, side: str, team: str, page: int):
        nonlocal total_goals, lock
        response = get_team_page(side, team, year, page)
        if not response:
            return
        for d in response.data:
            lock.acquire()
            if side == 'team1':
                total_goals += d.team1_goals
            elif side == 'team2':
                total_goals += d.team2_goals
            lock.release()

    total_goals = 0
    lock = threading.Lock()

    team1_response = get_team_page('team1', team, year)
    team2_response = get_team_page('team2', team, year)

    team1_total_pages, team2_total_pages = team1_response.total_pages, team2_response.total_pages,

    thread_pool = []
    for page in range(1, team1_total_pages + 1):
        thread = threading.Thread(target=get_goals_by_page, args=(year, 'team1', team, page,))
        thread_pool.append(thread)
        thread.start()

    for page in range(1, team2_total_pages + 1):
        thread = threading.Thread(target=get_goals_by_page, args=(year, 'team2', team, page,))
        thread_pool.append(thread)
        thread.start()

    for thread in thread_pool:
        thread.join()

    return total_goals


start = time.time()
# goals = get_total_goals('Barcelona', 2011)
goals = get_total_goals('Chelsea', 2011)
print("Total Goals: ", goals)
end = time.time()
print(end - start, "sec")

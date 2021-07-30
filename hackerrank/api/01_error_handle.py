# https://jsonmock.hackerrank.com/api/football_matches?year=<year>&team1=<team>&page=<page>
# https://jsonmock.hackerrank.com/api/football_matches?year=<year>&team2=<team>&page=<page>

# In this challenge, the REST API contains information about football matches. The provided API allows querying matches
# by teams and year. Your task is to get the total number of goals scored by a given team in a given year.

# To access a collection of matches, perform GET requests to above URLS,
# where <year> is the year of the competition, <team> is the name of the team,
# and <page> is the page of the results to request.
# The results might be divided into several pages. Pages are numbered from 1.

# Notice that the above two URLs are different.
# The first URL specifies the team1 parameter (denoting the visiting team).
# Thus, in order to get all matches that a particular team played in,
# need to retrieve matches where the team was the home team and the visiting team.

# For example, a GET request to https://jsonmock.hackerrank.com/api/football_matches?year=2011&team1=Barcelona&page=2
# returns data associated with matches in the year 2011, where team 1 was Barcelona, on the second page of the results.

# The response to such a request is a JSON with the following 5 fields:
# page : The current page of the results.
# per_page: The maximum number of matches returned per page.
# total: The total number of matches on all pages of the results.
# total_pages: The total number of pages with results.
# data: An array of objects containing matches information on the requested page.

# Each match record has several fields, but in this task only the following 4 are relevant:
# team1: a string denoting the name of the first team in the match
# team2: a string denoting the name of the second team in the match
# team1goals: a string denoting the number of goals scored by team 1 in the match
# team2goals: a string denoting the number of goals scored by team 2 in the match

# Function Description
# Complete the function getTotalGoals in the editor below.

# getTotalGoals has the following parameters:
# string team: the name of the team
# int year: the year of the competition

# The function must return an integer denoting the total number of goals
# scored by the given team in all matches in the given year that the team played in.

# Sample ['Barcelona', 2011'] -> 35
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

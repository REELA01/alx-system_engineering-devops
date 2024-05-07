#!/usr/bin/python3
"""
Script to query a list of all hot posts on a given Reddit subreddit.
"""


import requests


def number_of_subscribers(subreddit):
    """gitting ingo"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0


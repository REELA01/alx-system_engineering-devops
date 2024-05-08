#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Base case: if subreddit is invalid, return None"""
    if subreddit is None:
        return None
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'MyBot/0.1'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        articles = data['data']['children']
        for article in articles:
            hot_list.append(article['data']['title']
        after = data['data']['after']
        if after is not None:
            recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None

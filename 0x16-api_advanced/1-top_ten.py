#!/usr/bin/python3
"""contain top_ten function"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of first 10 hot post"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    res = response.json().get("data")
    [print(c.get("data").get("title")) for c in res.get("children")]

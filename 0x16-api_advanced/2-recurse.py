#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Base case: if subreddit is invalid, return None"""
    if subreddit is None:
        return None
    
    # Reddit API URL for getting hot articles in the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Set the User-Agent header to avoid Too Many Requests error
    headers = {'User-Agent': 'MyBot/0.1'}
    
    # Set parameters for pagination
    params = {'limit': 100, 'after': after}
    
    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params)
    
    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        # Extract titles of hot articles from response
        articles = data['data']['children']
        for article in articles:
            hot_list.append(article['data']['title'])
        
        # Check if there are more pages of results
        after = data['data']['after']
        if after is not None:
            # Recursively call the function to get next page of results
            recurse(subreddit, hot_list, after)
        else:
            # If no more pages, return the list of titles
            return hot_list
    else:
        # If subreddit is invalid or not found, return None
        return None

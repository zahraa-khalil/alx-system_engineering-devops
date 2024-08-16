#!/usr/bin/python3
"""Query the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditAPI/0.1'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            for post in posts:
                hot_list.append(post['data']['title'])

            next_after = data['data']['after']
            if next_after:
                return recurse(subreddit, hot_list, next_after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None

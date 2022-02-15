#!/usr/bin/python3
"""Function that queries the Reddit API and  prints the titles
of the first 10 hot posts listed for a given subreddit."""
import requests

url = 'https://www.reddit.com/r/{}/hot.json?limit=10'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}


def top_ten(subreddit):
    """Returns first 10 hot posts"""
    req = requests.get(url.format(subreddit), headers=headers)
    if req.status_code != 404:
        for item in req.json().get('data').get('children'):
            print(item['data']['title'])
    else:
        print(None)

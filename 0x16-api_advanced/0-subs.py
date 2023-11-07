#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    try:
        i = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                headers={'User-agent': 'hAxr'}, allow_redirects=False).json()
        return i.get('data').get('subscribers') if not None else 0
    except:
        return 0

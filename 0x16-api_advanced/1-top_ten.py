#!/usr/bin/python3
""" queries the Reddit API
    and prints the titles of top 10 posts
    listed for given subreddit """
import requests
import sys


def top_ten(subreddit):
    """ returns top ten post titles
        or none if queried subreddit invalid """
    headers = {'User-Agent': '0x16-api_advanced'}
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    response = requests.get(URL, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        postTitles = response.json().get('data').get('children')
        for titles in postTitles:
            print(title_.get('data').get('title'))
    else:
        print(None)

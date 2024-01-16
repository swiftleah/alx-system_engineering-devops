#!/usr/bin/python3
""" queries the Reddit API and returns list containing
    titles of all hot articles for given subreddit """
import requests
import sys
after = None


def recurse(subreddit, hot_list=[]):
    """ returns a list containing titles of all hot articles for subreddit
        or none if queried subreddit invalid """
    global after
    headers = {'User-Agent': '0x16-api_advanced'}
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(URL, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        listTitles = response.json().get('data').get('children')
        for title_ in listTitles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return (None)

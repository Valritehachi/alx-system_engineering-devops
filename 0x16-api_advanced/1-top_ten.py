#!/usr/bin/python3
""" a function that queries the Reddit API and prints the titles of the first 10 hot posts"""


import requests


def top_ten(subreddit):
    """ a function that queries the Reddit API and prints the titles."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the request, limiting the number of posts to 10
    params = {
        "limit": 10
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return

    results = response.json().get("data")

    [print(c.get("data").get("title")) for c in results.get("children")]

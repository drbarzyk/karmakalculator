# Karma Machine
# 4 / 20 / 22

from doctest import IGNORE_EXCEPTION_DETAIL
from dotenv import load_dotenv, set_key
from datetime import datetime
from dateutil import parser
from json import loads
import os
import requests
import pandas as pd

def validate_api_token():
    now = datetime.now()
    requestTimeout = 2 * 60 * 60    #2 hours
    requestDuration = now - parser.parse(os.environ.get('timestamp'))
    if requestDuration.total_seconds() > requestTimeout:
        exec(open("request.py").read())

def send_request(limit=25):
    headers = os.environ.get('headers')
    headers = loads(headers.replace("'", '"'))
    return requests.get("https://oauth.reddit.com/r/AskReddit/top", 
                        headers=headers,
                        params={'limit': f'{limit}'})

def build_df(res):
    labels = [
        'subreddit',
        'title',
        'selftext',
        'upvote_ratio',
        'ups',
        'downs',
        'score',
    ]

    df = pd.DataFrame(columns=labels)
    print(len(res.json()['data']['children']))
    for post in res.json()['data']['children']:
        data = {}
        for col in df.columns:
            data[col] = post['data'][col]
        post_df = pd.DataFrame([data])
        df = pd.concat([df, post_df], ignore_index=True)
    
    return df

def main():
    load_dotenv()
    validate_api_token()
    res = send_request()
    df = build_df(res)
    df.to_csv('reddit.csv')

if __name__ == '__main__':
    main()
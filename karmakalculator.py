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

# Grab an OAuth token for Reddit API if needed
# Token expires after 2 hours
def validate_oauth_token():
    # Get the current time
    now = datetime.now()

    # Check if 'timestamp' environment variable exists
    # If it doesn't, just set it to now
    if os.environ.get('timestamp') == '':
        os.environ['timestamp'] = f'{now}'
        set_key('.env', 'timestamp', os.environ['timestamp'])

    # Check if OAuth token has expired
    requestTimeout = 2 * 60 * 60    #2 hours
    requestDuration = now - parser.parse(os.environ.get('timestamp'))
    # If it has expired (or was previously empty), make a new request for a token
    if requestDuration.total_seconds() > requestTimeout or requestDuration.total_seconds() == 0:
        exec(open("oauth.py").read())

# Send a request to Reddit API
def send_request(limit=25):
    headers = os.environ.get('headers')
    # Get header in proper format
    headers = loads(headers.replace("'", '"'))
    return requests.get("https://oauth.reddit.com/r/AskReddit/top", 
                        headers=headers,
                        params={'limit': f'{limit}'})

# Build pandas DataFrame
def build_df(res):
    # (columns)
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
    # For each post in the request's data, add data corresponding to each label to the dataframe
    for post in res.json()['data']['children']:
        data = {}
        # Build table entry
        for col in df.columns:
            data[col] = post['data'][col]
        post_df = pd.DataFrame([data])
        df = pd.concat([df, post_df], ignore_index=True)
    
    return df

def main():
    # Load .env file
    load_dotenv()
    # Grab an OAuth token if needed
    validate_oauth_token()
    # Send request to Reddit API
    res = send_request()
    # Build pandas DataFrame from result of the request
    df = build_df(res)
    # Write DataFrame to file
    df.to_csv('posts.csv')

if __name__ == '__main__':
    main()
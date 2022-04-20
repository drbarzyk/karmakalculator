from dotenv import load_dotenv, set_key
from datetime import datetime
import os
import requests

load_dotenv()

CLIENT_ID = os.environ.get('personal_use_script')
SECRET_TOKEN = os.environ.get('secret')
USERNAME = os.environ.get('username')
PASSWORD = os.environ.get('password')

'''
*   Credit: James Briggs
*   https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c
'''
# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_TOKEN)

# here we pass our login method (password), username, and password
data = {
    'grant_type': 'password',
    'username': USERNAME,
    'password': PASSWORD
}
# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'KarmaKalculator/0.0.1'}

# send our request for an OAuth token, get current time
now = datetime.now()
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# change environment variables
os.environ['headers'] = f'{headers}'
set_key('.env', 'headers', os.environ['headers'])
os.environ['timestamp'] = f'{now}'
set_key('.env', 'timestamp', os.environ['timestamp'])
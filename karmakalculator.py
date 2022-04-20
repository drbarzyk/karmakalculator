# Karma Machine
# 4 / 20 / 22

from dotenv import load_dotenv, set_key
from datetime import datetime
from dateutil import parser
import os

def main():
    load_dotenv()

    now = datetime.now()
    requestTimeout = 2 * 60 * 60    #2 hours
    requestDuration = now - parser.parse(os.environ.get('timestamp'))
    if requestDuration.total_seconds() > requestTimeout:
        exec(open("request.py").read())

if __name__ == '__main__':
    main()
# karmakalculator

## Setup

### Requirements
- Python 3
- Reddit API

### Clone repository
- `git clone https://github.com/drbarzyk/karmakalculator.git`

### Reddit API

- Visit https://www.reddit.com/prefs/apps
- Create a new app
- Make a note of the **personal use script** and **secret** (*We'll use these later*)

### Environments

Create environment
- `python3 -m venv venv`
Activate environment (!!!)
- `source venv/bin/activate`
Add packages
- `pip install -r requirements.txt`
(!!!) (*You must activate the virtual environment each time to develop in*)

__You must do this part for Reddit API to work!__
###### .env

Edit existing .env file to include your **personal_use_script**, **secret**, Reddit **username** and **password**
*Leave the 'headers' and 'timestamp' variables blank*
  `personal_use_script='<PERSONAL_USE_SCRIPT>'
  secret='<SECRET>'
  username='<USERNAME>'
  password='<PASSWORD>'
  headers=''
  timestamp=''`
  
 ###### Useful Links
- https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c

# karmakalculator

## Setup

### Requirements
- Python 3
- Reddit API

### Clone repository
1. `git clone https://github.com/drbarzyk/karmakalculator.git`

### Reddit API

1. Visit https://www.reddit.com/prefs/apps
2. Create a new app
3. Make a note of the **personal use script** and **secret** (*We'll use these later*)
    ![image](https://user-images.githubusercontent.com/33323497/164302660-c75507a1-144a-4dd2-a7a3-9ebe312d8741.png)

### Environments

1. Create environment  
- `python3 -m venv venv`  

2. Activate environment (!!!)  
- `source venv/bin/activate`  

3. Add packages  
- `pip install -r requirements.txt`  

(!!!) *You must activate the virtual environment each time to develop in*  


# __You must do this part for Reddit API to work!__
### .env

1. Edit existing .env file to include your  
    - **personal_use_script**
    - **secret**
    - Reddit **username**
    - Reddit **password**  

*Leave the 'headers' and 'timestamp' variables blank*  
###### .env
    personal_use_script='<PERSONAL_USE_SCRIPT>'  
    secret='<SECRET>'  
    username='<USERNAME>'  
    password='<PASSWORD>'  
    headers=''  
    timestamp=''   
  
 ## Useful Links
- https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c

# Content-based-recommendation
Code for my research paper in Reykjavík University

### ORIGINAL NAMES GENERATOR CODE FROM
https://github.com/maknetaRo/python-100/tree/master/name-generator

### ORIGINAL VIDEO SCRAPER CODE FROM
https://github.com/nikhilkumarsingh/YouTubeAPI-Examples/blob/master/4.Channel-Vids.ipynb

### READ DOCUMENTATION BEFORE RUNNING

#### need to install ipynb to be able to call functions from other functions
- pip install ipynb


#### need to have installed
https://developers.google.com/youtube/v3/quickstart/python
- Python 2.7 or Python 3.5+
- The Google APIs Client Library for Python:
    - pip install --upgrade google-api-python-client
- The google-auth-oauthlib and google-auth-httplib2 libraries for user authorization.
    - pip install --upgrade google-auth-oauthlib google-auth-httplib2
    
#### YOU NEED TO STORE YOUR CONDA YOUTUBE API KEY IN A SECRET FILE
- https://towardsdatascience.com/how-to-hide-your-api-keys-in-python-fb2e1a61b0a0
    - keep in mind that you will probably have to remove spaces before and after = symbol 
    - correct line looks like this
        - export YOUTUBE_API_KEY='YOUTUBE-KEY_GOES_HERE'

# accounts settings
credentials = {}  # dictionary {"username": "password"} to store all "commenting" account logins to iterate through

# comment settings
accounts = []  # list of strings for user handles to comment on
num_posts = 1  # number of recent posts to comment on
comment = True  # boolean to comment on posts
comment_percent = 100  # percentage of posts to comment on
like = True  # boolean to like posts
like_percent = 100  # percentage of posts to like
comments = []  # list of strings for comments that will randomly be chosen

# action delay settings
action_delay = 3  # default amount of seconds delay after each comment/like
action_delay_from = 75  # randomized PERCENTAGE multiplier lower bound for action delay
action_delay_to = 300  # randomized PERCENTAGE multiplier upper bound for action delay

# account delay settings
account_delay_from = 10  # lower bound delay in seconds when a session is finished before starting the next
account_delay_to = 30  # upper bound delay in seconds when a session is finished before starting the next

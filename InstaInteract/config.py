# accounts settings
user_accounts = {}  # dictionary {"username": "password"} to store all "commenting" account logins to iterate through

# account delay settings
delay_from = 5  # lower bound delay in seconds when a session is finished before starting the next
delay_to = 15  # upper bound delay in seconds when a session is finished before starting the next

# comment settings
accounts = []  # list of strings for user handles to comment on
num_posts = 2  # number of recent posts to comment on
comment = True  # boolean to comment on posts
comment_percent = 100  # percentage of posts to comment on
like = True  # boolean to like posts
like_percent = 100  # percentage of posts to like
comments = []  # list of strings for comments that will randomly be chosen (can use generator.py to create, see README)

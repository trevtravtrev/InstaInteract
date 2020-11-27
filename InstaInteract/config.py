# accounts settings
user_accounts = {}  # dictionary {"username": "password"} to store all "commenting" account logins to iterate through

# account delay settings
account_delay_from = 5  # lower bound delay in seconds when a session is finished before starting the next
account_delay_to = 10  # upper bound delay in seconds when a session is finished before starting the next

# action delay settings
action_delay = 1  # default amount of seconds delay after each comment/like
action_delay_from = 75  # randomized PERCENTAGE multiplier lower bound for action delay
action_delay_to = 300  # randomized PERCENTAGE multiplier upper bound for action delay

# general settings
# available modes: "comment_and_like_recent"
mode = "comment_and_like_recent"
accounts = []  # list of strings for user handles to comment on
num_comments_from = 3  # lower bound number of comments per post (only used with the spam_comment_and_likes mode)
num_comments_to = 5  # upper bound number of comments per post (only used with the spam_comment_and_likes mode)
num_posts = 1  # number of recent posts to comment on
comment = True  # boolean to comment on posts
comment_percent = 100  # percentage of posts to comment on
like = True  # boolean to like posts
like_percent = 100  # percentage of posts to like
comments = []  # list of strings for comments that will randomly be chosen (can use generator.py to create, see README)

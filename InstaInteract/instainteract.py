from instapy import InstaPy
from time import sleep
from random import uniform

from InstaInteract import config


class InstaInteract:
    def __init__(self):
        self.mode = config.mode
        self.modes = {"comment_and_like_recent": self._comment_and_like_recent}

        self.user_accounts = config.user_accounts
        self.accounts = config.accounts
        self.num_posts = config.num_posts
        self.comment = config.comment
        self.comment_percent = config.comment_percent
        self.like = config.like
        self.like_percent = config.like_percent
        self.comments = config.comments
        self.account_delay_from = config.account_delay_from
        self.account_delay_to = config.account_delay_to
        self.action_delay = config.action_delay
        self.action_delay_from = config.action_delay_from
        self.action_delay_to = config.action_delay_to
        self.session = None

        self._check_config()
        self._check_mode()

    def run(self):
        for account in self.user_accounts:
            self._login(account)
            # set random delays after like/comment actions ("action delay settings" in config.py)
            self.session.set_action_delays(enabled=True, like=self.action_delay, comment=self.action_delay,
                                           randomize=True,
                                           random_range_from=self.action_delay_from,
                                           random_range_to=self.action_delay_to)
            # select mode to run (set "mode" parameter in config.py)
            self.modes[self.mode]()
            self._end_session()
            sleep(uniform(self.account_delay_from, self.account_delay_to))

    def _comment_and_like_recent(self):
        # settings
        self.session.set_comments(self.comments)
        self.session.set_do_comment(enabled=self.comment, percentage=self.comment_percent)
        self.session.set_do_like(enabled=self.like, percentage=self.like_percent)
        # start feature
        self.session.interact_by_users(self.accounts, amount=self.num_posts, randomize=False)   # removed "media='Photo"

    # def _spam_comment_and_like_recent(self):
    #     # settings
    #     self.session.set_comments(self.comments)
    #     self.session.set_do_comment(enabled=self.comment, percentage=self.comment_percent)
    #     self.session.set_do_like(enabled=self.like, percentage=self.like_percent)
    #     # start feature
    #     self.session.interact_by_users(self.accounts, amount=self.num_posts, randomize=False)   # removed "media='Photo"

    def _login(self, username):
        user = username
        pw = self.user_accounts.get(username)
        self.session = InstaPy(username=user,
                               password=pw,
                               headless_browser=False,
                               bypass_security_challenge_using='email')
        self.session.login()

    def _end_session(self):
        self.session.end()

    def _check_config(self):
        if not (self.user_accounts and self.accounts and self.comments):
            raise Exception("Invalid parameters in config.py file")

    def _check_mode(self):
        if self.mode not in self.modes:
            raise Exception("Invalid mode in config.py file")

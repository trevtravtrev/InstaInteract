from instapy import InstaPy
from time import sleep
from random import uniform

from InstaInteract import config


class InstaInteract:
    def __init__(self, mode):
        self.mode = mode
        self.modes = {"comment_and_like": self._comment_and_like}

        self.user_accounts = config.user_accounts
        self.accounts = config.accounts
        self.num_posts = config.num_posts
        self.comment = config.comment
        self.comment_percent = config.comment_percent
        self.like = config.like
        self.like_percent = config.like_percent
        self.comments = config.comments
        self.delay_from = config.delay_from
        self.delay_to = config.delay_to
        self.session = None

        self._check_config()
        self._check_mode()
        self._run()

    def _run(self):
        for account in self.user_accounts:
            self._login(account)
            self.modes[self.mode]()
            self._end_session()
            sleep(uniform(self.delay_from, self.delay_to))

    def _comment_and_like(self):
        # settings
        self.session.set_comments(self.comments)
        self.session.set_do_comment(enabled=self.comment, percentage=self.comment_percent)
        self.session.set_do_like(enabled=self.like, percentage=self.like_percent)
        # start feature
        self.session.interact_by_users(self.accounts, amount=self.num_posts, randomize=False, media='Photo')

    def _login(self, username):
        user = username
        pw = self.user_accounts.get(username)
        self.session = InstaPy(username=user,
                               password=pw,
                               headless_browser=False)
        self.session.login()

    def _end_session(self):
        self.session.end()

    def _check_config(self):
        if not (self.user_accounts and self.accounts and self.comments):
            raise Exception("Missing parameters in config.py file")

    def _check_mode(self):
        if self.mode not in self.modes:
            raise Exception("Invalid mode")

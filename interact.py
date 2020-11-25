from instapy import InstaPy
from time import sleep
from random import uniform
import config


def login(username):
    user = username
    pw = config.credentials.get(username)
    session = InstaPy(username=user,
                      password=pw,
                      headless_browser=False)
    session.login()
    return session


def interact(session):
    # settings
    session.set_action_delays(enabled=True, like=config.action_delay, comment=config.action_delay, randomize=True,
                              random_range_from=config.action_delay_from, random_range_to=config.action_delay_to)
    session.set_comments(config.comments)
    session.set_do_comment(enabled=config.comment, percentage=config.comment_percent)
    session.set_do_like(enabled=config.like, percentage=config.like_percent)
    # start feature
    session.interact_by_users(config.accounts, amount=config.num_posts, randomize=True, media='Photo')
    # end feature
    session.end()


def main():
    if config.credentials and config.accounts and config.comments:
        for username in config.credentials:
            session = login(username)
            interact(session)
            sleep(uniform(config.account_delay_from, config.account_delay_to))
    else:
        print("Error: missing parameters in config.py file")


if __name__ == '__main__':
    main()

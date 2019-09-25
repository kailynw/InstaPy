#!/usr/bin/env python3
# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import random



# set workspace folder at desired location (default is at your home folder)
set_workspace(path='/root/InstaPy')

# get an InstaPy session!
session = InstaPy(username='btvkwc', password="1325brushycreekrd",headless_browser=True)

select_user=random.choice(['abeldamina','lighthousefll','bbcofnj'])

with smart_run(session):

   
    # Interacts with a certain amount of the users post
    session.set_user_interact(amount=3, randomize=False, percentage=100, media='Photo')

    #Likes User post based on perc.
    session.set_do_like(enabled=True, percentage=100)

    # session.set_relationship_bounds(enabled=True,
    #                                 max_followers=400,
    #                                 max_following=10000,
    #                                 min_posts=2,
    #                                 max_posts=300)

    #Likes only a certain amount an hour
    session.set_quota_supervisor(enabled=True,sleepyhead=True, stochastic_flow=True, sleep_after=["likes_h"],peak_likes_hourly=22)

    session.set_skip_users(skip_private=True,
                            private_percentage=100)

    #Follow nobody
    session.set_do_follow(enabled=False, percentage=0)

    session.interact_user_followers([select_user], amount=200, randomize=True)


# activity
# session.end(threaded_session=True)

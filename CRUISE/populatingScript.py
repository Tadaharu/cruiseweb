import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CRUISE.settings')

import django
django.setup()

import random
from cruiseWeb.models import Tweet
from faker import Faker
from django.utils import timezone

fakegen = Faker()


def populate():
    with open('tweet.txt') as f:
        for eachline in f:
            tweet = eachline.lstrip()
            cDate = timezone.now()

            iData = Tweet.objects.get_or_create(tweetText = tweet, createdDate = cDate)[0]


if __name__ == '__main__':
    print('Populating Script!')
    populate()
    print('Populating Complete')

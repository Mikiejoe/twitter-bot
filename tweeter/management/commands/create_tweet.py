from django.core.management.base import BaseCommand
from tweeter.models import Tweet
from tweeter.gemini import generate_tweet
from tweeter.models import Token
import json
from tweeter.tweet import (
    post_tweet,
)
from .refresh_token import refresh_token


class Command(BaseCommand):
    help = "Create a tweet"

    def handle(self, *args, **options):
        refreshed_token = refresh_token()
        if refreshed_token is None:
            self.stdout.write(self.style.ERROR("Error refreshing token"))
        else:
            st_token = json.dumps(refreshed_token)
            t = Token.objects.get(name="token")
            t.token = st_token
            t.save()
            print("refreshed token is ", st_token)
            tweet = generate_tweet()
            payload = {"text": tweet}
            res = post_tweet(payload, refreshed_token)
            print("response is ", res)
            if res.status_code != 201:
                self.stdout.write(self.style.ERROR("Error creating tweet"))
            Tweet.objects.create(text=tweet)
            self.stdout.write(self.style.SUCCESS("Tweet created!"))

import tweepy
import json
from tweepy.streaming import StreamListener
from tweepy import Stream

with open('twitter_credentials.json') as access_data:
    cred = json.load(access_data)
    api_key = cred['API_KEY']
    api_secret_key = cred['API_SECRET_KEY']
    access_token = cred['ACCESS_TOKEN']
    access_token_secret = cred['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('valentines_tweets.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True


def on_error(self, status):
    print(status)
    return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#valentines'])








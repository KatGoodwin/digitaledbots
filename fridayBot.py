from time import sleep
import tweepy
from credentials import *
import datetime

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def howManyDaysMessage() :
    #find out how many days till friday
    today = datetime.date.today()
    day =  today.weekday()
    if (day == 4):
        message = 'Today is friday, yay!'
    else :
        daysLeft = 4-day % 7 
        message = 'There are %d days until Friday' % daysLeft
    return message

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        message = "@" + status.user.screen_name + ", " + howManyDaysMessage();
        print message
        try :

            api.update_status(message, [status.id], [True])
        except Exception as e:
            print e



myStreamListener = MyStreamListener()

myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track = ["#ideldaysTillFriday"])



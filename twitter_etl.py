
import tweepy
import pandas as pd
from datetime import datetime
import json
import s3fs

access_key= "MtyvoaruAmm03eXSKxs1KjFIP"
access_secret=  "5FH7IwkF9no6hJVKl7QZXN4pnOARUrEevHMpJkLouYCPqegfPd"
consumer_key=  "1826590903810883585-ADWo8GmTg1njcIrLoUQH0GbqfyAJeE"
consumer_secret=   "UqKhzvK8Oyo5xPpbDNgO9pBEugauzRFBf7YI5ChII0SGh"

#Twitter authentication
auth=tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

#Creating an API object
api= tweepy.API(auth)

tweets = api.user_timeline(screen_name='@PrayagSingh21',#the user name that you want to extract data from
                           #max number tweets you want to extract
                           count=3,
                           #If you don't want to extrat retweets
                           include_rts = False
                           #extended represents you want the entire tweet text else  only first 140 words  will get extracted
                           #tweet_mode='extended'

                           )

print(tweets)
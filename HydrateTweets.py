import tweepy
import os
import csv
import time

consumer_key = 'pHdWSt9mtJk4qfu60HflTkDcj'
consumer_secret = '1zN8OMuW3u99JdWoRpH4tzHI9faI2cyP4Dwb5TiacB0XljEwLe'
access_token = '990747555117060096-RFcF0YARXHnZPKJ2NhYFC6ekri2znB1'
access_token_secret = 'NaPMoG2MBIjHchpuiM3wrEzzs4ZBiwqhpiRORmIvHUC88'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search_words = ["black lives matter", "freddie gray", "mike brown", "michael brown",
                "#blacklivesmatter", "#freddiegray", "#michaelbrown", "#mikebrown"]

location = os.getcwd()
count = 1
start_time = time.time()

with open('tweets368.csv', 'w', newline='') as f:
    tweets = csv.writer(f)
    tweets.writerow(['Tweet ID', 'Username', 'Date and Time', 'User location',
                     'Text'])
    print("Good")
    for file in sorted(os.listdir(location))[2:368]: #368 total
        if file.endswith('.txt'):
            print(os.path.basename(file))
            tweet_id_lists = [int(line.strip()) for line in open(file, 'r')]
            N = len(tweet_id_lists)
            print(N)
            counter = 0
            count += 1
            start = 0
            stop = 100
            while stop <= N:
                if start > N:
                    break
                tweet_request = api.statuses_lookup(tweet_id_lists[start:stop])
                for tweet in tweet_request:
                    if any(phrase in tweet.text for phrase in search_words):
                        tweets.writerow([tweet.id_str, tweet.user.screen_name, tweet.created_at,
                                         tweet.user.location, tweet.text])
                counter += 1
                print("Good "+str(count) + " " + str(counter))
                start += 100
                stop += 100
                if stop > N:
                    stop = N
        print(time.time()-start_time)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import sys
import csv
import pyttsx3
import openpyxl
import traceback
from textblob import TextBlob
class TweetAnalyzer():
    """
    Functionality for analyzing and categorizing content from tweets.
    """

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", str(tweet)).split())

    

    def tweets_to_data_frame(self, tweets):
        df={}
        df = pd.DataFrame(data=[tweet.full_text for tweet in tweets], columns=['tweets'])

        df['id'] = [tweet.id for tweet in tweets]
        df['len'] = [len(tweet.full_text) for tweet in tweets]
        df['date'] = [tweet.created_at for tweet in tweets]
        df['source'] = [tweet.source for tweet in tweets]
        df['likes'] = [tweet.favorite_count for tweet in tweets]
        df['retweets'] = [tweet.retweet_count for tweet in tweets]
        print(df)
        return df

    ####function for sentimental analysis
    def get_tweet_sentiment(self, tweet): 
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(tweet)
        print(self.clean_tweet(tweet),analysis.sentiment.polarity)
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'

    def get_tweets(self, tweets):
        print(len(tweets))
        tmp=[]
        ''' 
        Main function to parse tweets. 
        '''
        #fethched tweets
        tweets_fethched = [] 
  
        try: 
            tweets_fethched=tweets 
  
            # parsing tweets one by one 
            for tweet in tweets:
                print('***************')
                # empty dictionary to store required params of a tweet 
                parsed_tweet = {} 
  
                # saving text of tweet 
                parsed_tweet['text'] = tweet 
                # saving sentiment of tweet 
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.full_text)
                
  
                # appending parsed tweet to tweets list 
                if tweet.retweet_count > 0: 
                    # if tweet has retweets, ensure that it is appended only once 
                    if parsed_tweet not in tweets: 
                        tmp.append(parsed_tweet) 
                else: 
                    tmp.append(parsed_tweet) 
  
            # return parsed tweets 
            return tmp 
  
        except: 
            # print error (if any) 
            print("Error : ",traceback.print_exc() ) 

 

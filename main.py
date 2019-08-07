from tweetanalyzer import *
from twitterConnector import *

twitter_client = TwitterClient()
tweet_analyzer = TweetAnalyzer()
tweets_for_csv = []
api = twitter_client.get_twitter_client_api()

tweets = api.user_timeline(screen_name="narendramodi", count=100,tweet_mode="extended")
lines=['ID','LEN','DATE','SOURCE','LIKES','RETWEETS']
df = tweet_analyzer.tweets_to_data_frame(tweets)

#write to a new csv file from the array of tweets
#print(df)
#outfile = 'pune' + "_tweets.csv"
print(tweets)
#with open(outfile, 'w') as writeFile:
#   writer = csv.writer(writeFile)
#    writer.writerow(lines)
# Call a Workbook() function of openpyxl  
# to create a new blank Workbook object 
wb = openpyxl.Workbook() 



# Get workbook active sheet   
# from the active attribute.  
sheet = wb.active
sheet.cell(row = 1, column = 1).value = ' ID '
sheet.cell(row = 1, column = 2).value = ' LEN '
sheet.cell(row = 1, column = 3).value = ' DATE '
sheet.cell(row = 1, column = 4).value = ' SOURCE '
sheet.cell(row = 1, column = 5).value = ' LIKES '
sheet.cell(row = 1, column = 6).value = ' RETWEETS '





tmp = []
tweets_for_csv = [tweet.full_text for tweet in tweets] # CSV file created  
for j in tweets_for_csv: 
#Appending tweets to the empty array tmp 
    tmp.append(j)  

# Printing the tweets
print('***************SP *****************')



#    print("writing to " + outfile)
for i in range(len(df['id'])):
    sheet.cell(row = i+2, column = 1).value =df['id'][i]
    sheet.cell(row = i+2, column = 2).value =df['len'][i]
    sheet.cell(row = i+2, column = 3).value =df['date'][i]
    sheet.cell(row = i+2, column = 4).value =df['source'][i]
    sheet.cell(row = i+2, column = 5).value =df['likes'][i]
    sheet.cell(row = i+2, column = 6).value =df['retweets'][i]
    
# save the file 
wb.save('modi_tweets.xlsx')

print('--------------new edit here -----------------')
print(tmp)
tmp=tweet_analyzer.get_tweets(tweets)
ptweets = [tweet for tweet in tmp if tweet['sentiment'] == 'positive'] 
# percentage of positive tweets 
print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tmp))) 
# picking negative tweets from tweets 
ntweets = [tweet for tweet in tmp if tweet['sentiment'] == 'negative'] 
# percentage of negative tweets 
print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tmp))) 
# percentage of neutral tweets 
#print("Neutral tweets percentage: {} %".format(100*len(tweets\p - ntweets - ptweets)/len(tweets))) 

# printing first 5 positive tweets 
print("\n\nPositive tweets:") 
for tweet in ptweets[:10]: 
    print(tweet['text']) 

# printing first 5 negative tweets 
print("\n\nNegative tweets:") 
for tweet in ntweets[:10]: 
    print(tweet['text']) 








#with open(outfile, 'w') as file:
    
    #for i in range(len(df['id'])):
        #QW=[]
        #writer = csv.writer(file, delimiter=',')
        #QW=list([df['id'][i],df['len'][i],df['date'][i],df['source'][i],df['likes'][i],df['retweets'][i]])
        #print(QW)
        #writer.writerow(map(lambda x: [x], QW))

#Twitter Trends function
trends1 = api.trends_place(1) # from the end of your code
# trends1 is a list with only one element in it, which is a 
# dict which we'll put in data.
'''data = trends1[0] 
# grab the trends
trends = data['trends']
# grab the name from each trend
names = [trend['name'] for trend in trends]
# put all the names together with a ' ' separating them
trendsName = ' '.join(names)
print(trendsName)
for a in names:
    print(a)'''
        

        

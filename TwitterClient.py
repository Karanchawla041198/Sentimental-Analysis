import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
	'''
	Generic Twitter Class for sentiment analysis.
	'''
	def __init__(self):
		'''
		Class constructor or initialization method.
		'''
		# keys and tokens from the Twitter Dev Console
		consumer_key = 'xU4wrrmSyj2Kf3isOFqr13nvO'
		consumer_secret = 'JMHtomNpxjP3675GsV9hH1YCa6tHuR5LFLHcTbLv4fWH8DHGJM'
		access_token = '1193117792796413952-2TO4tQ5rQdQHrnYVQbTj6KkSncZE5P'
		access_token_secret = '7o91Uk9kMszRu4KjG9yibE5mc1WXJSc8eI8vR7rvQJKpm'

		# attempt authentication
		try:
			# create OAuthHandler object
			self.auth = OAuthHandler(consumer_key, consumer_secret)
			# set access token and secret
			self.auth.set_access_token(access_token, access_token_secret)
			# create tweepy API object to fetch tweets
			self.api = tweepy.API(self.auth)
		except:
			print("Error: Authentication Failed")

	def clean_tweet(self, tweet):
		'''
		Utility function to clean tweet text by removing links, special characters
		using simple regex statements.
		'''
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())

	def get_tweet_sentiment(self, tweet):
		'''
		Utility function to classify sentiment of passed tweet
		using textblob's sentiment method
		'''
		# create TextBlob object of passed tweet text
		analysis = TextBlob(self.clean_tweet(tweet))
		# set sentiment
		if analysis.sentiment.polarity > 0:
			output = open("twitter-out.txt", "a")
			output.write("pos")
			output.write("\n")
			output.close()
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			output = open("twitter-out.txt", "a")
			output.write("ooo")
			output.write("\n")
			output.close()
			#return 'negative'
			return 'neutral'
		else:
			output = open("twitter-out.txt", "a")
			output.write("neg")
			output.write("\n")
			output.close()
			return 'negative'

	def get_tweets(self, query, count = 10):
		'''
		Main function to fetch tweets and parse them.
		'''
		# empty list to store parsed tweets
		tweets = []

		try:
			# call twitter api to fetch tweets
			fetched_tweets = self.api.search(q = query, count = count)

			# parsing tweets one by one
			for tweet in fetched_tweets:
				# empty dictionary to store required params of a tweet
				parsed_tweet = {}

				# saving text of tweet
				parsed_tweet['text'] = tweet.text
				# saving sentiment of tweet
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

				# appending parsed tweet to tweets list
				if tweet.retweet_count > 0:
					# if tweet has retweets, ensure that it is appended only once
					if parsed_tweet not in tweets:
						tweets.append(parsed_tweet)
				else:
					tweets.append(parsed_tweet)

			# return parsed tweets
			return tweets

		except tweepy.TweepError as e:
			# print error (if any)
			print("Error : " + str(e))


class twitterObj:
	def __init__(self, name, number):
		self.name=name
		self.number=number

		api = TwitterClient()
		self.tweets = api.get_tweets(query=name, count=number)

		# picking positive tweets from tweets
		self.ptweets = [tweet for tweet in self.tweets if tweet['sentiment'] == 'positive']
		# picking negative tweets from tweets
		self.ntweets = [tweet for tweet in self.tweets if tweet['sentiment'] == 'negative']
		# percentage of neutral tweets
		self.otweets = [tweet for tweet in self.tweets if tweet['sentiment'] == 'neutral']

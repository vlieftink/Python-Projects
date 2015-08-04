#!/usr/bin/python

import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os

from pymongo import MongoClient
import json


ckey = 
consumer_secret = 
access_token_key = 
access_token_secret = 

start_time = time.time() #grabs the system time
keyword_list = ['#kowet','kowet','Go Ahead Eagles']


#Listener Class Override
class listener(StreamListener):

	def __init__(self, start_time, time_limit=60):

		self.time = start_time
		self.limit = time_limit

	def on_data(self, data):

		while (time.time() - self.time) < self.limit:

			try:
				client = MongoClient('localhost', 27017)
				db = client['DB-NAME']
				collection = db['COLLECTION-NAME']
				tweet = json.loads(data)
				collection.insert(tweet)
				return True


			except BaseException, e:
				print 'failed ondata,', str(e)
				time.sleep(5)
				pass

		exit()

	def on_error(self, status):

		print statuses

auth = OAuthHandler(ckey, consumer_secret) #OAuth object
auth.set_access_token(access_token_key, access_token_secret)

twitterStream = Stream(auth, listener(start_time, time_limit=20000000000000000)) #initialize Stream object with a time out limit
twitterStream.filter(track=keyword_list)  #call the filter method to run the Stream Object

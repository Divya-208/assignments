#1./what is access token?
# print("The Access Token is a credential that can be used by an application to access an API.
#
# It can be any type of token (such as an opaque string or a JWT) and is meant for an API. Its purpose is to inform the API that the bearer of this token has been authorized to access the API and perform specific actions (as specified by the scope that has been granted).
#
# The Access Token should be used as a Bearer credential and transmitted in an HTTP Authorization header to the API.
#
#
# my access token=******
# my access token secret=##########")





#2.get ip addressss of some website.
# ("student@LAB5-140 MINGW32 ~/Desktop
# $ nslookup google.com
# Non-authoritative answer:
# Server:  google-public-dns-a.google.com
# Address:  8.8.8.8
#
# Name:    google.com
# Addresses:  2404:6800:4002:803::200e
#           172.217.24.238
#
#
# student@LAB5-140 MINGW32 ~/Desktop
# $ nslookup youtube.com
# Non-authoritative answer:
# Server:  google-public-dns-a.google.com
# Address:  8.8.8.8
#
# Name:    youtube.com
# Addresses:  2404:6800:4002:803::200e
#           172.217.24.238")

#3.extract tweets bThe Access Token is a credential that can be used by an application to access an API.
import tweepy
consumer_key208='///////////////'
consumer_secret208='///////////'
access_token208='---------'
access_token_secret208='------------'
auth=tweepy.OAuthHandler(consumer_key208,consumer_secret208)
auth.set_access_token(access_token208,access_token_secret208)
api=tweepy.API(auth)
tweets=api.search('#swacchbharatmission',lang="en",count=20,tweet_mode="extended")
#print tweets
for tweet in tweets :
    print("%%%%%%%%%%%%%")
    print(tweet.full_text)
    print("***************")



#4.difference between library and api

#API is a part of library which defines how an application communicates with external code

# API can be written in any language.
# Library is written in same language which is a collection of all the functionalities required for the use case.
# For example :class datetime.date
# An idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect. Attributes: year, month, and day.
#
# class datetime.time
# An idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds (there is no notion of “leap seconds” here). Attributes: hour, minute, second, microsecond, and tzinfo.
#
# class datetime.datetime
# A combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.
#
# class datetime.timedelta
# A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.
#
# class datetime.tzinfo
# An abstract base class for time zone information objects. These are used by the datetime and time classes to provide a customizable notion of time adjustment (for example, to account for time zone and/or daylight saving time).
#
# class datetime.timezone
# A class that implements the tzinfo abstract base class as a fixed offset from the UTC.
# For further reading : https://stackoverflow.com/questions/3678665/is-there-still-a-difference-between-a-library-
# We can create our own APIs using Python Framework like Django and Flask which can be used in websites.
# from django.db import models
# 
# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
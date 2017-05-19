
# coding: utf-8

# # ASSIGNMENT 3

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

from twython import Twython


# In[ ]:

#In the above cell, I imported twython library which is essential to capture tweets & perform analysis on twitter tweets.


# In[3]:

APP_KEY ='ahCowaVjdVvO5lmJGMpigchRR' 
APP_SECRET = 'o7dy5avGMI5AJutFPWjYHAeTAw5kVR8YBMt00OKXKvnUzBUvak'
OAUTH_TOKEN = '630413671-toB4t1du9TkC3NVwfdxFzZpZKJ6kDqiIGcBIG2Bx'
OAUTH_TOKEN_SECRET = 'fnTfmLeB1uiEheUPUHCEcFchcylJbBxLmvQHdrFF5wZl7'
twitter=Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)


# In[ ]:

#The above cell denotes my twitter app tokens & keys.


# In[4]:

twitter


# In[ ]:

#In the above cell, I tested for the connection is successful with twitter.


# In[5]:

search = twitter.search(q='women')


# In[ ]:

#Since, today is women's day. I searched for this term to get tweets easily.


# In[ ]:

#In the above cell, I tried to display value of 'text' key for index 0 of statuses dictionary.


# In[10]:

from twython import TwythonStreamer


# In[ ]:

#I imported TwythonStreamer to live capture the twitter.


# In[18]:

from twython import TwythonStreamer
tweets=[] 
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if data['user']['lang'] == 'en':
            tweets.append(data)
            print("received tweet #",len(tweets))
        if len(tweets) >= 50:
            self.disconnect()
    def on_error(self, status_code, data):
        print(status_code,data)
        self.disconnect()



# In[ ]:

#In the above cell, custom filter parameters were defined.


# In[19]:

stream = MyStreamer(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


# In[ ]:

#stream using the tokens and keys provided above.


# In[20]:

stream.statuses.filter(track='women')


# In[ ]:

#I captured the 50 tweets.


# In[ ]:

#I want to analyze the followers count for users in 50 tweets.


# In[23]:

t = []
for i in range(len(tweets[:])):
    t.append(tweets[i]['user']['followers_count'])


# In[24]:

df = pd.Series(t)


# In[ ]:

#I created a dataframe with followers count.


# In[26]:

import seaborn as sns
import matplotlib.pyplot as plt


# In[27]:

get_ipython().magic(u'matplotlib inline')


# In[28]:

sns.distplot(df)


# In[ ]:

#I created a distribution plot using seaborn to visually represent the count of followers for the respective tweets.


# In[29]:

df.describe()


# In[ ]:

#Statistical data 


# In[ ]:

#Thus, I analyzed twitter with the search term "machine" for first 10 tweets using twythonstreamer.


# Description: [Twitter Analysis for the term "machine" with focus on "followers_count" for first 10 live tweets stream.]
# 
# 
# 

# # Map of a Tweet

# {'contributors': None,
#  'coordinates': None,
#  'created_at': 'Thu Mar 09 00:30:35 +0000 2017',
#  'display_text_range': [0, 76],
#  'entities': {'hashtags': [],
#   'symbols': [],
#   'urls': [{'display_url': 'twitter.com/gabriella_akat\u2026',
#     'expanded_url': 'https://twitter.com/gabriella_akat/status/839511910282244096',
#     'indices': [77, 100],
#     'url': 'https://t.co/BRetdzB6Ua'}],
#   'user_mentions': []},
#  'favorite_count': 0,
#    'favorited': False,
#  u'filter_level': u'low',
#  u'geo': None,
#  u'id': 839634483263438848L,
#  u'id_str': u'839634483263438848',
#  u'in_reply_to_screen_name': None,
#  u'in_reply_to_status_id': None,
#  u'in_reply_to_status_id_str': None,
#  u'in_reply_to_user_id': None,
#  u'in_reply_to_user_id_str': None,
#  u'is_quote_status': True,
#  u'lang': u'en',
#  u'place': None,
#  u'possibly_sensitive': False,
#  u'quoted_status': {u'contributors': None,
#   u'coordinates': None,
#   u'created_at': u'Wed Mar 08 16:23:31 +0000 2017',
#   u'display_text_range': [0, 104],
#   u'entities': {u'hashtags': [{u'indices': [26, 43],
#      u'text': u'adaywithoutwomen'},
#     {u'indices': [94, 104], u'text': u'RealWomen'}],
#    u'media': [{u'display_url': u'pic.twitter.com/BnTAjHQAfU',
#      u'expanded_url': u'https://twitter.com/gabriella_akat/status/839511910282244096/photo/1',
#      u'id': 839511900723372032L,
#      u'id_str': u'839511900723372032',
#      u'indices': [105, 128],
#      u'media_url': u'http://pbs.twimg.com/media/C6aLoDNUYAAeHir.jpg',
#      u'media_url_https': u'https://pbs.twimg.com/media/C6aLoDNUYAAeHir.jpg',
#      u'sizes': {u'large': {u'h': 1914, u'resize': u'fit', u'w': 1413},
#       u'medium': {u'h': 1200, u'resize': u'fit', u'w': 886},
#       u'small': {u'h': 680, u'resize': u'fit', u'w': 502},
#       u'thumb': {u'h': 150, u'resize': u'crop', u'w': 150}},
#      u'type': u'photo',
#      u'url': u'https://t.co/BnTAjHQAfU'}],
#    u'symbols': [],
#    u'urls': [],
#    u'user_mentions': []},
#   u'extended_entities': {u'media': [{u'display_url': u'pic.twitter.com/BnTAjHQAfU',
#      u'expanded_url': u'https://twitter.com/gabriella_akat/status/839511910282244096/photo/1',
#      u'id': 839511900723372032L,
#      u'id_str': u'839511900723372032',
#      u'indices': [105, 128],
#      u'media_url': u'http://pbs.twimg.com/media/C6aLoDNUYAAeHir.jpg',
#      u'media_url_https': u'https://pbs.twimg.com/media/C6aLoDNUYAAeHir.jpg',
#      u'sizes': {u'large': {u'h': 1914, u'resize': u'fit', u'w': 1413},
#       u'medium': {u'h': 1200, u'resize': u'fit', u'w': 886},
#       u'small': {u'h': 680, u'resize': u'fit', u'w': 502},
#       u'thumb': {u'h': 150, u'resize': u'crop', u'w': 150}},
#      u'type': u'photo',
#      u'url': u'https://t.co/BnTAjHQAfU'}]},
#   u'favorite_count': 314,
#   u'favorited': False,
#   u'filter_level': u'low',
#   u'geo': None,
#   u'id': 839511910282244096L,
#   u'id_str': u'839511910282244096',
#   u'in_reply_to_screen_name': None,
#   u'in_reply_to_status_id': None,
#   u'in_reply_to_status_id_str': None,
#   u'in_reply_to_user_id': None,
#   u'in_reply_to_user_id_str': None,
#   u'is_quote_status': False,
#   u'lang': u'en',
#   u'place': None,
#   u'possibly_sensitive': False,
#   u'retweet_count': 169,
#   u'retweeted': False,
#   u'source': u'<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>',
#   u'text': u'To the people celebrating #adaywithoutwomen - GET REAL &amp; GET YOUR WHINY BUTT TO WORK! The #RealWomen https://t.co/BnTAjHQAfU',
#   u'truncated': False,
#   u'user': {u'contributors_enabled': False,
#    u'created_at': u'Wed Apr 22 22:43:34 +0000 2009',
#    u'default_profile': False,
#    u'default_profile_image': False,
#    u'description': u'Taking America Back! \u2764\nFollowed by @realjameswoods\n#TRUMP \u2b50 #MAGA \U0001f1fa\U0001f1f8\n#2A \U0001f4a5\n#Christian \U0001f607 \n#ProIsrael \U0001f1ee\U0001f1f1',
#    u'favourites_count': 32466,
#    u'follow_request_sent': None,
#    u'followers_count': 11246,
#    u'following': None,
#    u'friends_count': 10342,
#    u'geo_enabled': True,
#    u'id': 34428229,
#    u'id_str': u'34428229',
#    u'is_translator': False,
#    u'lang': u'en',
#    u'listed_count': 16,
#    u'location': u'United States',
#    u'name': u'Gabriella \u2764 \U0001f1fa\U0001f1f8\U0001f339',
#    u'notifications': None,
#    u'profile_background_color': u'000000',
#    u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png',
#    u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png',
#    u'profile_background_tile': False,
#    u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/34428229/1486531746',
#    u'profile_image_url': u'http://pbs.twimg.com/profile_images/837348640066682880/6qb7ew1r_normal.jpg',
#    u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/837348640066682880/6qb7ew1r_normal.jpg',
#    u'profile_link_color': u'3B94D9',
#    u'profile_sidebar_border_color': u'000000',
#    u'profile_sidebar_fill_color': u'000000',
#    u'profile_text_color': u'000000',
#    u'profile_use_background_image': False,
#    u'protected': False,
#    u'screen_name': u'gabriella_akat',
#    u'statuses_count': 16513,
#    u'time_zone': u'America/Los_Angeles',
#    u'url': None,
#    u'utc_offset': -28800,
#    u'verified': False}},
#  u'quoted_status_id': 839511910282244096L,
#  u'quoted_status_id_str': u'839511910282244096',
#  u'retweet_count': 0,
#  u'retweeted': False,
#  u'source': u'<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>',
#  u'text': u'No the REAL WOMEN were working and not whinning their liberal fat asses off. https://t.co/BRetdzB6Ua',
#  u'timestamp_ms': u'1489019435121',
#  u'truncated': False,
#  u'user': {u'contributors_enabled': False,
#   u'created_at': u'Sun Sep 18 14:51:51 +0000 2011',
#   u'default_profile': False,
#   u'default_profile_image': False,
#   u'description': u'Class is back in the White House.  I love our new 1st family. #DrainTheSwamp',
#   u'favourites_count': 89209,
#   u'follow_request_sent': None,
#   u'followers_count': 13354,
#   u'following': None,
#   u'friends_count': 13062,
#   u'geo_enabled': False,
#   u'id': 375669510,
#   u'id_str': u'375669510',
#   u'is_translator': False,
#   u'lang': u'en',
#   u'listed_count': 183,
#   u'location': None,
#   u'name': u'Trump IS my Pres',
#   u'notifications': None,
#   u'profile_background_color': u'DBE9ED',
#   u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme17/bg.gif',
#   u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme17/bg.gif',
#   u'profile_background_tile': False,
#   u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/375669510/1353888859',
#   u'profile_image_url': u'http://pbs.twimg.com/profile_images/797577683286851585/1LYFVtth_normal.jpg',
#   u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/797577683286851585/1LYFVtth_normal.jpg',
#   u'profile_link_color': u'CC3366',
#   u'profile_sidebar_border_color': u'DBE9ED',
#   u'profile_sidebar_fill_color': u'E6F6F9',
#   u'profile_text_color': u'333333',
#   u'profile_use_background_image': True,
#   u'protected': False,
#   u'screen_name': u'railgirl1952',
#   u'statuses_count': 294254,
#   u'time_zone': u'Central Time (US & Canada)',
#   u'url': None,
#   u'utc_offset': -21600,
#   u'verified': False}}

# Test the existence of feedparser feeds.

# Goal: handle errors without failing to run the program.

import feedparser
import logging
import time

# Trying with no feed as input.
feed_source = 'https://ia.net/feed'
d = feedparser.parse(feed_source)

if 'title' in d.feed:
	print(f"title: {'title' in d.feed}")
else:
	logging.error('Title does not exist in feed')

try:
	print(f"first entry: {d.entries[0]}")
except IndexError:
	logging.error('IndexError: there are no entries in this feed')

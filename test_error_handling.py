# Test the existence of feedparser feeds.

# Goal: handle errors without failing to run the program.

import feedparser
import logging
import time

# Trying with no feed as input.
feed_source = ''
d = feedparser.parse(feed_source)

try:
	if 'title' in d.feed:
		print(f"title: {'title' in d.feed}")
	print(f"first entry: {d.entries[0]}")
except IndexError:
	print("There was an IndexError.")

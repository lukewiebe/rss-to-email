# Find new entries in a given feed.
# Collect title, publish time, source for each entry.

import feedparser
import time

# Replace samplefeed.xml with url to use in real life
d = feedparser.parse(r'samplefeed.xml')

published_time = d.entries[0].published_parsed
current_time = time.localtime() # should this be .gmtime()?

# convert times to days since epoch
published_time = time.mktime(published_time)
current_time = time.mktime(current_time)

elapsed_time = current_time - published_time

if elapsed_time > 86400: # 86400 is number of seconds in a day
	print("Success! The difference between times is more than 1 day.")
else:
	print("Something went wrong here.")

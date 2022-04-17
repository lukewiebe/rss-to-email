# Find new entries in a given feed.
# Collect title, publish time, source for each entry.

import feedparser
import time

# Replace samplefeed.xml with url to use in real life
d = feedparser.parse(r'samplefeed.xml')

published_time = d.entries[0].published_parsed
published_time = time.mktime(published_time)

current_time = time.localtime() # should this be .gmtime()?
current_time = time.mktime(current_time)

elapsed_time = current_time - published_time

if elapsed_time > 86400: # 86400 is number of seconds in a day
	print("The difference between times is more than a day.")
else:
	print("The difference between times is less than a day.")

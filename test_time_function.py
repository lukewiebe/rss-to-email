# test_time_function.py
# Simple test case for my time checking function

import feedparser
import logging
import time_check

d = feedparser.parse(r'samplefeed.xml')
d = d.entries[0].published_parsed

print(time_check.is_this_less_than_a_day_old(d))

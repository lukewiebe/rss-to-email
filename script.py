# script

# Extract feed urls and titles.
# Result is a list of urls.

from xml.etree import ElementTree as ET
import requests
import time
import feedparser
import logging
import time_check

# Set logging to print debug messages
logging.basicConfig(level=logging.DEBUG)

def extract_rss_urls_from_opml(filename):
    urls = [] # empty array for output
    with open(filename, 'rt') as f:
        tree = ET.parse(f)
    for node in tree.findall('.//outline'):
        url = node.attrib.get('xmlUrl')
        title = node.attrib.get('title')
        if url:
            urls.append(url)
    return urls

urls = extract_rss_urls_from_opml('Feeds.opml')
# Test that feeds have been extracted from Feeds.opml
logging.debug("Number of URLs to check: " + str(len(urls)))

# Initialize feed counter for debugging and/or logging
feedcounter = 0

current_time = time.mktime(time.localtime())

for url in urls:
	d = feedparser.parse(url)
	if d.feed:
		logging.debug(f"Parsing {d.feed.link}...")
	else:
		logging.error(f"{url} does not exist")

	fresh_post = time_check.is_this_less_than_a_day_old(d.entries[0].published_parsed)
	if fresh_post == True:
		print(f"{d.feed.link} has a new post.")
		feedcounter += 1
	else:
		print(f"{d.feed.link} does not have any new posts.")

		# replicate all functionality of the old try block

		# 		published_time = d.entries[0].published_parsed
		# 		# Convert to Unix time
		# 		published_time = time.mktime(published_time)
		# 
		# 		elapsed_time = current_time - published_time
		# 		if elapsed_time < 86400:
		# 			print(f"{d.feed.link} has a new post.")
		# 			feedcounter += 1
		# 	except IndexError:
		# 		logging.error("Feed has no entries.")

logging.debug("Number of Feeds with new entries: " + str(feedcounter))



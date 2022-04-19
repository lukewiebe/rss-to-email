# script

# Extract feed urls and titles.
# Result is a list of urls.

from xml.etree import ElementTree as ET
import requests
import time
import feedparser
import logging

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
logging.debug("Number of URLs to check: " + str(len(urls))) # test feed extraction

# Hit each url with a GET request.

# Commented this out because feedparser handles fetching the contents of feeds.

# first_lines = [] # list to count responses
# 
# for url in urls:
# 	response = requests.get(url)
# 	# add the first line of each response to first_lines list
# 	first_lines.append(response.text.partition('\n')[0])
# 
# logging.debug("Number of responses: " + str(len(first_lines))) # compare to number of urls

# get current time and convert to Unix time
feedcounter = 0
current_time = time.mktime(time.localtime())

for url in urls:
	logging.debug("Current value of feeds with new entries: " + str(feedcounter))
	d = feedparser.parse(url)
	logging.debug(f"Parsing {d.feed.link}...")
	published_time = d.entries[0].published_parsed
	# Convert to Unix time
	published_time = time.mktime(published_time)
	elapsed_time = current_time - published_time
	if elapsed_time < 86400:
		feedcounter += 1
# 	elif elapsed_time > 86400:
		# Do not include in digest

logging.debug("Number of Feeds with new entries: " + str(feedcounter))

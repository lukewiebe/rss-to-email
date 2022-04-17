# script

# Extract feed urls and titles.
# Result is a list of urls.

from xml.etree import ElementTree as ET
import requests
import time
import feedparser

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
print("Number of URLs to check: " + str(len(urls))) # test feed extraction

# Hit each url with a GET request.

first_lines = [] # list to count responses

for url in urls:
	response = requests.get(url)
	# add the first line of each response to first_lines list
	first_lines.append(response.text.partition('\n')[0])

print("Number of responses: " + str(len(first_lines))) # compare to number of urls

# get current time and convert to Unix time
current_time = time.mktime(time.localtime())

for url in urls:
	d = feedparser.parse(url)
	published_time = d.entries[0].published_parsed
	# Convert to Unix time
	published_time = time.mktime(published_time)
	elapsed_time = current_time - published_time
	if elapsed_time < 86400:
		# Include in digest
	else if elapsed_time > 86400:
		# Do not include in digest

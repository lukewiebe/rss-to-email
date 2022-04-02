# script

# Extract feed urls and titles.
# Result is a list of dicts with keys: 'title', 'url'

from xml.etree import ElementTree as ET

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
print(urls) # test feed extraction



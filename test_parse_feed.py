# Parse a given feed for new entries.
# Collect title, publish time, source for each entry.

from xml.etree import ElementTree as ET

with open('samplefeed.xml', 'r') as f:
	tree = ET.parse(f)

print(tree.findall('/'))

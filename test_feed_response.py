# Script to get a sample feed response.
# Completed, will overwrite samplefeed.xml each time it runs.

import requests
from pprint import pprint
url = 'https://ia.net/feed'
response = requests.get(url)

print(response)

print(response.headers['content-type'])

text = response.text

with open('samplefeed.xml', 'w') as f:
    f.write(text)

with open('samplefeed.xml', 'r') as f:
    content = f.readlines()[1:5]
    pprint(content)

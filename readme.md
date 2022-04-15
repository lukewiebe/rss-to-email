# RSS to Email

Hello! This is my first ever Python project. It's mostly an excuse to learn Python, but it's also something I want to use.

This will become an automated daily digest that will email me new articles from my RSS feeds.

## Current State

`test_feed_response.py` is now working. It dumps the response from ia.net's RSS feed into `samplefeed.xml` so I have sample data to work with.

Parsing `Feeds.opml` is working in `script.py`.

Next steps: use the logic in `test_feed_response.py` to build a loop that hits each feed with a GET request. Use the data in `samplefeed.xml` and the technique in `script.py` to build a parser for the resulting HTML. 

# RSS to Email

This will become an automated daily digest that will email me new articles from my rss feeds.

## Current State

`test_feed_response.py` is now working. It dumps the response from ia.net's rss feed into `samplefeed.xml` so I have sample data to work with.

Parsing `Feeds.opml` is working in `script.py`.

Next steps: use the logic in `test_feed_response.py` to build a loop that hits each feed with a GET request. Use the data in `samplefeed.xml` and the technique in `script.py` to build a parser for the resulting HTML. 

A note on `feedparser`: There is a package that can handle parsing RSS feeds for me, but it is overkill for what I want to do. All I need is to pull the publish date, link, title, and site from a feed entry and use it to create an email. `feedparser` can do this and much more. However, this project is about learning and I believe that learning to parse XML files will be far more useful to me than learning to use a package that does it for me.

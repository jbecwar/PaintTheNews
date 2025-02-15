import feedparser

def getTitles():
    url = 'https://www.reddit.com/r/News/.rss'
    feed = feedparser.parse(url)
    return [entry.title for entry in feed.entries]

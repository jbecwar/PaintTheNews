import feedparser

def getTitles():
    #url = 'https://www.reddit.com/r/News/.rss'
    url = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'

    feed = feedparser.parse(url)
    return [entry.title for entry in feed.entries]

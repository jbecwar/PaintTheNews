import feedparser
import db

def getTitles(runtime):
    #url = 'https://www.reddit.com/r/News/.rss'
    url = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'

    feed = feedparser.parse(url)
    for entry in feed.entries:
        db.insertHeadline(url, entry.title, entry.link, entry.published, runtime)
    return [entry.title for entry in feed.entries]

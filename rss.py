import feedparser
import db

def getTitles():
    #url = 'https://www.reddit.com/r/News/.rss'
    url = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'

    feed = feedparser.parse(url)
    db.createHeadlineTable()
    for entry in feed.entries:
        db.insertHeadline(url, entry.title, entry.link, entry.published)
    return [entry.title for entry in feed.entries]

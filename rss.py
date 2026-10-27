import feedparser
import db
import random

def getTitles(runtime):
    feeds = [
    ('The New York Times', 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'),
    ('Yahoo News', 'https://news.yahoo.com/rss'),
    ('The Guardian', 'https://www.theguardian.com/world/rss'),
    ('US News', 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US:en'),
    ('BBC News', 'https://www.bbc.co.uk/feeds/rss/world.xml'),
    ('CNN', 'https://www.cnn.com/services/rss/'),
    ('Al Jazeera', 'https://www.aljazeera.com/xml/rss/all.xml'),
    ('NPR', 'https://www.npr.org/rss/rss.php?id=1001'),
    ('Fox News', 'https://www.foxnews.com/about/rss'),
    ('USA Today', 'https://www.usatoday.com/rss/'),
    ('Good News Network', 'https://www.goodnewsnetwork.org/category/news/feed/')
    ]
    
    entityCount = 0

    while entityCount <1:
        feedName, url = random.choice(feeds)
        print(f"Fetching RSS feed from: {feedName} ({url})")
        feed = feedparser.parse(url)
        entityCount = len(feed.entries)
        print(f"Found {entityCount} entries.")
    
    for entry in feed.entries:
        db.insertHeadline(url, entry.title, entry.link, entry.published, runtime)
    return feedName, [entry.title for entry in feed.entries]

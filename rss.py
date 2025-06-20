import feedparser
import db
import random

def getTitles(runtime):
    urls = [
    'http://www.reddit.com/.rss',
    'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
    'https://news.yahoo.com/rss',
    'https://www.theguardian.com/world/rss',
    'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US:en',
    'https://www.bbc.co.uk/feeds/rss/world.xml',
    'https://www.cnn.com/services/rss/',
    'https://www.aljazeera.com/xml/rss/all.xml',
    'https://www.npr.org/rss/rss.php?id=1001',
    'https://www.foxnews.com/about/rss',
    'https://www.usatoday.com/rss/',
    'https://www.goodnewsnetwork.org/category/news/feed/'
    ]
    
    entityCount = 0

    while entityCount <1:
        url = random.choice(urls)
        print(f"Fetching RSS feed from: {url}")
        feed = feedparser.parse(url)
        entityCount = len(feed.entries)
        print(f"Found {entityCount} entries.")
    
    for entry in feed.entries:
        db.insertHeadline(url, entry.title, entry.link, entry.published, runtime)
    return [entry.title for entry in feed.entries]

import feedparser
import urllib.parse

def get_news(topic="india"):
    
    topic = urllib.parse.quote(topic)
    rss_url = f"https://news.google.com/rss/search?q={topic}"

    feed = feedparser.parse(rss_url)

    if not feed.entries:
        return ["Sorry Boss, I couldn't fetch the latest news."]

    headlines = []

    for article in feed.entries[:5]:
        headlines.append(article.title)

    return headlines


import feedparser
from newspaper import Config
from newspaper import Article

# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

# config = Config()
# config.browser_user_agent = user_agent
# config.request_timeout = 10

rss_links = {
    'nytimes': 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
    'cnn': 'http://rss.cnn.com/rss/cnn_latest.rss/',
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'reuters': 'https://www.reutersagency.com/feed/?taxonomy=best-topics&post_type=best',
    'washingtonpost': 'http://feeds.washingtonpost.com/rss/world',
    'wsj': 'https://feeds.content.dowjones.io/public/rss/RSSUSnews', #blocked from download
    'usatoday': 'https://www.usnews.com/rss/news', 
    'abcnews': 'http://abcnews.go.com/abcnews/topstories', #broken
    'nbcnews': 'http://feeds.nbcnews.com/nbcnews/public/news',
    'cbsnews': 'http://www.cbsnews.com/latest/rss/main',
    'bloomberg': 'http://www.bloomberg.com/feed/news/', #broken
    'huffpost': 'http://www.huffingtonpost.com/feeds/index.xml', #broken
    'buzzfeed': 'https://www.buzzfeed.com/world.xml',
    'vice': 'https://www.vice.com/en_us/rss', #broken
    'slate': 'http://www.slate.com/rss',
    'vox': 'http://www.vox.com/rss/index.xml',
    'salon': 'http://www.salon.com/feed/',
    'thinkprogress': 'https://thinkprogress.org/feed', #broken
    'theintercept': 'https://theintercept.com/feed/?rss',
    'theatlantic': 'http://feeds.feedburner.com/TheAtlantic',
    'thenewyorker': 'http://www.newyorker.com/feed/news',
    'time': 'http://feeds2.feedburner.com/time/topstories',
    'newsweek': 'http://www.newsweek.com/rss', #broken
    'usnews': 'http://www.usnews.com/rss/news',
    'forbes': 'http://www.forbes.com/real-time/feed2/',
    'businessinsider': 'http://www.businessinsider.com/rss',
    'fortune': 'http://fortune.com/feed/',
    'cnbc': 'http://www.cnbc.com/id/100003114/device/rss/rss.html',
    'marketwatch': 'http://www.marketwatch.com/rss/topstories',
    'latimes': 'http://www.latimes.com/local/rss2.0.xml',
    'chicagotribune': 'http://www.chicagotribune.com/news/local/rss2.0.xml',
    'bostonglobe': 'http://www.bostonglobe.com/rss/bigpicture',
    'dallasnews': 'http://www.dallasnews.com/rss/headlines',
    'miamiherald': 'http://www.miamiherald.com/news/?template=rss&mime=xml',
    'democracynow': 'https://www.democracynow.org/democracynow.rss',
    'jacobin' : 'https://jacobin.com/rss',
    'commondreams': 'https://www.commondreams.org/feeds/news.rss',
}

def scrape_news_from_feed(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)
    # print(feed)
    for entry in feed.entries:
        # create a newspaper article object
        article = Article(entry.link)
        # print(entry.link)
        # download and parse the article
        article.download()
        article.parse()
        # extract relevant information
        articles.append({
            'title': article.title,
            'author': article.authors,
            'publish_date': article.publish_date,
            'content': article.text,
            'images' : article.images,
            'url': article.url
        })
    return articles

def scrape_news_from_source(source):
    return scrape_news_from_feed(rss_links[source])

articles = scrape_news_from_source('nytimes')

# print the extracted articles
for article in articles:
    print('Title:', article['title'])
    # print('Author:', article['author'])
    # print('Publish Date:', article['publish_date'])
    print('Content:', article['content'])
    # print('Images:', article['images'])
    # print('URL:', article['url'])
    print()

import newspaper
import feedparser

def scrape_news_from_feed(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        # create a newspaper article object
        article = newspaper.Article(entry.link)
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


feed_url = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
articles = scrape_news_from_feed(feed_url)

# print the extracted articles
for article in articles:
    print('Title:', article['title'])
    print('Author:', article['author'])
    print('Publish Date:', article['publish_date'])
    print('Content:', article['content'])
    print('Images:', article['images'])
    print('URL:', article['url'])
    print()

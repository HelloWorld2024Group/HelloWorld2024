import Fetcher
import pandas as pd

def create_article_database():
    articles = []
    for source in Fetcher.rss_links.keys():
        print('Scraping articles from', source)
        articles.extend(Fetcher.scrape_news_from_source(source))

    df = pd.DataFrame(articles)
    df.to_csv('articles.csv', index=False)

create_article_database()
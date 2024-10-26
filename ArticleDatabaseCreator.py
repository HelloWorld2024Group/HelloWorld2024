import Fetcher
import pandas as pd

def create_article_database(sources):
    articles = []
    for source in sources:
        print('Scraping articles from', source)
        articles.extend(Fetcher.scrape_news_from_source(source))

    df = pd.DataFrame(articles)
    df.to_csv('articles.csv', index=False)

sources = ['bbc', 'cnn', 'nytimes']
create_article_database(sources)
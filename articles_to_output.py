import Fetcher
import transformers
from sentence_transformers import SentenceTransformer
from numpy import dot
from numpy.linalg import norm
import numpy as np
import random
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
import pandas as pd
from together import Together
import feedparser
from newspaper import Article


def return_article_dict(articles):
    article_dict = {}

    #stores a list of articles in a dictionary
    for i in range(0, len(articles)):
        article_dict["article{}".format(i)] = articles[i]["content"]
    return article_dict


def get_summaries(a):

    client = Together()
    sum_dict = {}

    for i in range(0,len(a)):
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct-Turbo",
            messages=[{"role": "user", "content": a[i] + "Generate a bulleted list of main ideas. Do not add anything other than content"}],
        )
        topic = response.choices[0].message.content
        topic = topic.strip("Here's a bulleted list of the main ideas from the article: \n")

        response2 = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct-Turbo",
            messages=[{"role": "user", "content": a[i] + "Generate a header based on the main ideas in 10 words or less."}],
        )
        header = response2.choices[0].message.content

        sum_dict[header] = topic
    return sum_dict

def summarizes_articles(user_choices):
    #scrapes articles
    articles = []
    for source, url in Fetcher.rss_links.items():
        if source in user_choices:
            print(source)
            feed = Fetcher.feedparser.parse(url)
            for entry in feed.entries:
                try:
                    # create a newspaper article object
                    article = Article(entry.link)
                    # download and parse the article
                    article.download()
                    article.parse()
                    # extract relevant information
                    articles.append({
                        'content': article.text,
                    })
                except Exception as e:
                    pass
    print(articles)

    article_dict = return_article_dict(articles)
    #variables:
    #arbirtrary threshold for similarity
    threshold = 1.3
    #list of articles to be clustered
    list_of_articles = list(article_dict.values())

    print(list_of_articles)

    #sentence transformer model
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    #list of vectors about sentence semantics for each sentence
    embeddings = model.encode(list_of_articles) 

    #links embeddings using ward method
    Z = linkage(embeddings, method='ward')

    # Create clusters by cutting the dendrogram at a certain threshold (t)
    clusters = fcluster(Z, t=threshold, criterion='distance')
    
    print(clusters)

    #creates a dictionary with numbered articles and their clustered
    cluster_dict = {}
    for i in range(0,len(clusters)):
        cluster_dict["article{}".format(i)] = clusters[i]

    #initializes a dictionary w keys being each of the clusters 
    grouped_dict = {}
    for cluster_num in np.unique(list(cluster_dict.values())):
        grouped_dict[cluster_num] = []

    #values of cluster_dict defined as all articles with same cluster in a list
    for k,v in cluster_dict.items():
        if k not in grouped_dict:
            grouped_dict[v].append(k)


    #removes all clusters with only one article
    filtered_grouped_list = [] 
    for k,v in grouped_dict.items():
        if len(v) > 1:
            filtered_grouped_list.append(v)

    print(filtered_grouped_list)

    #creates list of articles where all articles of same topic are concatonated into one string
    articles_to_summarize = []
    for v in filtered_grouped_list:
        one_topic_list = []
        for art in v:
            one_topic_list.append((article_dict[art]))
        articles_to_summarize.append("\t".join(one_topic_list))

    print(articles_to_summarize)

    final_dict = get_summaries(articles_to_summarize)

    print(final_dict)
    
    return final_dict
    
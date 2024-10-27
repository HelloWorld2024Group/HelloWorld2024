import Fetcher
import articles_to_output

final_dict = []
for source, url in Fetcher.rss_links.items():
    #print(url)
    final_dict.append(articles_to_output.summarizes_articles(url))

print(final_dict)

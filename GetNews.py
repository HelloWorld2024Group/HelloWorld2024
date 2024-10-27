import sys
# import articles_to_output
import json

sources = sys.argv[1:]

with open('all_sources_content.json') as f:
    data = json.load(f)

user_content_list = []
for source in sources:
    user_content_list.extend([article for article in data[source]])

# summaries = articles_to_output.summarizes_articles(user_content_list)
with open("articles.json", "w") as file:
    json.dump(user_content_list, file)


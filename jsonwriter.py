import json
import articles_to_output

feed_url = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'

#Data to be written into the JSON file (usually a dictionary or list)
data = articles_to_output.summarizes_articles(feed_url)

# Writing data into a JSON file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)  # indent=4 adds pretty formatting (optional)


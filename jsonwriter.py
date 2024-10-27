import json
import articles_to_output

#feed_url = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'

def json_writer(data):

    # Writing data into a JSON file
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4) 


#json_writer(articles_to_output.summarizes_articles())


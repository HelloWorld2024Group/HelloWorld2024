import pandas as pd
from together import Together

def format_article(row):
    return f"source={str(row['source'])}, title={row['title']}, date={row['publish_date']}, authors={row['author']}, content={row['content']}, url={row['url']}"

def get_summaries(output_file):
    articlesDF = pd.read_csv('articles.csv')

    client = Together()
    summaries = []

    for index, row in articlesDF.iterrows():
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct-Turbo",
            messages=[{"role": "user", "content": format_article(row) + "\nSummarize the article in one sentence."}],
        )

        newRow = row.to_dict()
        newRow['summary'] = response.choices[0].message.content
        summaries.append(newRow)

        count = index + 1
        if count % 10 == 0:
            print(f"Summarized {count}/{articlesDF.shape[0]} articles")

    summariesDF = pd.DataFrame(summaries)
    summariesDF.to_csv(output_file, index=False)

output_file = 'summaries.csv'
get_summaries(output_file)
import sys
import articles_to_output
import jsonwriter

sources = sys.argv[1:]
summaries = articles_to_output.summarizes_articles(sources)
jsonwriter.json_writer(summaries)
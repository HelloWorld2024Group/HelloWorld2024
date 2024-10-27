# Newsflash AI

We developed NEWSFLASH AI, a news summarization app that
leverages machine learning, Llama, and Pygame. The app allows
users to choose their preferred news outlets and browse news in their 
category of interest. It then gathers news articles from those
sources and provides summarized content with headers and bullet
points for multiple articles. Leonor focused on the front-end
development, creating the app interface, user screens, buttons,
images, and text displays. This app saves users the hassle of
reading articles across multiple platforms to obtain the same
information, making it easier and more timely to stay updated
with the news.

For this project, we created an AWS API that fetches the top news articles every day and stores them, along with their vector embeddings, which it uses to group articles together. After a user opens the app and specifies their preferred news sources, a call is made to the API that generates a headline with bullet points for each grouping (using only the specified news sources), which is then displayed in the app. The headers and bullet points are generated from two models: one that tokenizes and then combines semantically similar articles and one that feeds a Llama model the newly combined articles to generate headers/summaries.

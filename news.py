
from config import newsapi
from say import say
import requests

def newsReport(country):
    news_data = requests.get(
        f"https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={newsapi}")

    articles = news_data.json()['articles']

    news_articles = []
    for arti in articles:
        news_articles.append(arti['title'])

    for i in range(5):
        say(news_articles[i])

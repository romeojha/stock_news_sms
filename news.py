#from news api endpoint getting top 4 news and this will be
#later called on main


import requests
import datetime

today = datetime.date.today()
API_KEY_NEWS = '7eabe04bb3124b859eb201acbb77860e'


def company_news():
    params = {
        'q': 'Tesla Inc',
        'from': today,
        'sortBy': 'popularity',
        'apikey': API_KEY_NEWS,
        'language': 'en',
        'pageSize': '5'
    }

    NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'

    req = requests.get(NEWS_ENDPOINT, params=params)
    response = req.json()
    data = response['articles'][:4]
    return data

article_list=company_news()

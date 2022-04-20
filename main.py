import requests
import news
from twilio.rest import Client


TWILIO_SID = 'AC121cc84bac166b7b54c52d8b16379f62'
TWILIO_TOKEN = '761b27672087421c51bde0f4385043e7'
PHONE = '+18454022616'


STOCK_NAME = 'TSLA'
COMPANY_NAME = 'Tesla Inc'


STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
API_KEY = '779JYMIFS0Q990ZJ'


param = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': API_KEY
}


req = requests.get(STOCK_ENDPOINT, params=param)
response = req.json()


data = response['Time Series (Daily)']
new_data = [value for (key, value) in data.items()]
yesterday_closing_price = new_data[1]['4. close']
today_closing_price = float(new_data[0]['4. close'])

diff = float(today_closing_price) - float(yesterday_closing_price)
diff_percent = (diff / today_closing_price) * 100

article_list = news.article_list
list2 = [article['description'] for article in article_list]

if abs(diff_percent) > 4:
    print(diff_percent)
    for arti in list2:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        message = client.messages.create(
            body=arti,
            from_='18454022616',
            to='+919546610073',
        )
        print(message.sid)
else:
    print(diff_percent)
    print('error')

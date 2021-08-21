import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os


URL = 'https://www.amazon.com/YABING-Steins-Living-Bedroom-Decoration/dp/B09B72S1LG/ref=sr_1_62?crid=1YBV9O75' \
      'ADNM&dchild=1&keywords=steins+gate+merchandise&qid=1627516762&sprefix=steins+gate+mer%2Caps%2C150&sr=8-62'

headers = {
      'Accept-Language': 'en-us',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'
                    ' Version/14.0.3 Safari/605.1.15'
}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
price = float(soup.find(name='span', id='priceblock_ourprice').getText()[1:])
name = soup.find(name='span', id='productTitle').getText()

if price < 12:
    email = os.environ.get("email")
    password = os.environ.get("password")

    with smtplib.SMTP('smtp.mail.yahoo.com', port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(msg=f'Subject: Low price alert!\n\nThe product you wanted ({name}) is now cheaper than '
                                f'your target price. The price now is ${price}.',
                                from_addr=email,
                                to_addrs='periwalmukul14@gmail.com')

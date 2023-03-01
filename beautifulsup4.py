import requests
import lxml
from bs4 import BeautifulSoup

HOST ='https://login.kg'

URL = 'https://login.kg/produktsija-apple/monobloki-apple-imac'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}


def get_html(url, params=''):
    response = requests.get(url, headers=HEADERS, params=params)
    return response


def get_contetnt(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='product-thumb')
    monoblocks = []
    for item in items:
        monoblocks.append(
            {
                'title': item.find('div', class_='caption').get_text(strip=True),
                'link': item.find('div', class_='caption').find('a').get('href'),
                'price': item.find('p', class_='price').get_text(strip=True),
                'img_link': item.find('div', class_='image').find('img').get('src')


            }
        )

    return monoblocks

html = get_html(URL)
content = get_contetnt(html.text)

#with open('html.txt','w')as f:
#    f.write(str(html.text))

with open('pars.txt', 'w')as f:
   f.write(str(content))
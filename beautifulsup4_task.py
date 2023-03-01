#1. Отправьте запрос на API Rick and Morty, и вытащите 10 живых персонажей людской
#расы, затем сохраните это в свой json файл.

import requests

# import  requests
#
# BASE_URL = 'https://rickandmortyapi.com/'
#
# response = requests.delete(f'{BASE_URL}/products/21')
# print(response.json())







# def get_html(url, params=''):
#     response = requests.get(url, headers=HEADERS, params=params)
#     return response
#
#
#
# def get_contetnt(html):
#     soup = BeautifulSoup(html, 'lxml')
#     items = soup.find_all('div', class_='product-thumb')
#     monoblocks = []
#     for item in items:
#         monoblocks.append(
#             {
#                 'title': item.find('div', class_='caption').get_text(strip=True),
#                 'link': item.find('div', class_='caption').find('a').get('href'),
#                 'price': item.find('p', class_='price').get_text(strip=True),
#                 'img_link': item.find('div', class_='image').find('img').get('src')
#
#
#             }
#         )
#
#     return monoblocks

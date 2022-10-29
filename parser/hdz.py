import requests
from bs4 import BeautifulSoup as BS
from pprint import pprint

URL = 'https://rezka.ag/collections/317-luchshie-ekranizacii-literaturnyh-proizvedeniy/'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

def get_html(html, params=''):
    reg = requests.get(url=URL, headers=HEADERS, params=params)
    return reg

def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    series = []
    for item in items:
        info = item.find('div', class_='b-content__inline_item-link').find('div').getText().split(', ')
        serial = {
            'title': item.find('div', class_='b-content__inline_item-link').find('a').getText(),
            'link':  item.find('div', class_='b-content__inline_item-link').find('a').get('href'),
            'inform': item.find('div', class_='b-content__inline_item-link').find('div').getText().split(', '),
        }
        try:
            serial['year'] = info[0]
            serial['country'] = info[1]
            serial['genre'] = info[2]
        except:
            serial['year'] = info[0]
            serial['country'] = 'Unknown'
            serial['genre'] = info[2]
        series.append(serial)
    return series

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        series = []
        for page in range(1, 21):
            html = get_html(f'{URL}page/{page}/')
            current_page = get_data(html.text)
            series.extend(current_page)
        return series
    else:
        raise Exception('Error in parsingg')

pprint(parser())
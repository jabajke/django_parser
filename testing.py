from bs4 import BeautifulSoup
import requests

url = 'https://www.21vek.by/refrigerators/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/95.0.4638.69 Safari/537.36', 'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, params=params)
    return r


def parse():
    html = get_html(url)
    print(html)


parse()

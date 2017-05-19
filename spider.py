import requests
from bs4 import BeautifulSoup


def web_crawler(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://www.toptenz.net/page/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')

        for link in soup.findAll('a', {'class': 'entry-title'}):
            href = link.get('href')
            print(href)
        page += 1

web_crawler(1)



import requests
import bs4
import time

vacancy = "python"
BASE_URL = "https://hh.ru"
url = f"https://hh.ru/search/vacancy?text={vacancy}"
headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"
}

# pip install lxml
# pip install beautifulsoup4


def get_next_page(soup):
    next_page = soup.select_one('a[data-qa="pager-next"]')["href"]
    return (BASE_URL + next_page) if next_page else None


def get_page(url):
    while url:
        text = requests.get(url, headers=headers).text
        soup = bs4.BeautifulSoup(text, "lxml")
        yield soup
        url = get_next_page(soup)
        print("-" * 20)
        print(url)
        print("-" * 20)

url = "https://spb.hh.ru/search/vacancy?text=python&salary=&ored_clusters=true&page=31&search_session_id=b17342e3-e38f-421b-ac14-248434ce3725"
for page in get_page(url):
    header_v = [i.text for i in page.select('span[data-qa="serp-item__title-text"]')]
    for post in header_v:
        header_v['href']
    company = page.select(
        'div > a > span > span > span[data-qa="vacancy-serp__vacancy-employer-text"]'
    )
    print(header_v)
    print(company)
    time.sleep(2)

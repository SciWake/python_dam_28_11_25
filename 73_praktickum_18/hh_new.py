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


def get_card_data(card: bs4.BeautifulSoup) -> tuple:
    url = card.select_one('a[data-qa="serp-item__title"]')["href"]
    title = card.select_one('span[data-qa="serp-item__title-text"]').text
    company = card.select_one(
        'span[data-qa="vacancy-serp__vacancy-employer-text"]'
    ).text
    return (url, title, company)


def main():
    data = []
    for page in get_page(url):
        cards = page.select('div[data-qa^="vacancy-serp__vacancy"]')
        for card in cards:
            data.append(get_card_data(card))
        print(data)
        time.sleep(3)

main()

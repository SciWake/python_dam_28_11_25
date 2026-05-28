import time

import bs4
import pymysql
import requests
from config import BASE_URL, dbconfig, headers, url
from db import create_database, create_table, insert_data


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


def get_card_data(card):
    url = card.select_one('a[data-qa="serp-item__title"]')["href"]
    title = card.select_one('span[data-qa="serp-item__title-text"]').text
    company = card.select_one(
        'span[data-qa="vacancy-serp__vacancy-employer-text"]'
    ).text
    if not url or not title:
        return None
    return (title, company, url)


def main():
    with pymysql.connect(**dbconfig) as connection:
        print(connection.open)
        db_name = create_database(connection)
        connection.select_db(db_name)
        create_table(connection)

        for page in get_page(url):
            data = []
            cards = page.select('div[data-qa^="vacancy-serp__vacancy"]')
            for card in cards:
                card_data = get_card_data(card)
                if card_data:
                    data.append(card_data)
            insert_data(connection, data)
            time.sleep(3)


main()

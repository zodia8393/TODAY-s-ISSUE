# news_scanner.py

import requests
from bs4 import BeautifulSoup

# 네이버 뉴스 페이지에서 기사 크롤링
def scan_news():
    url = 'https://news.naver.com/main/ranking/popularDay.naver'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    article_titles = []
    for i in range(1, 11):
        article_titles.append(soup.select(f'.ranking_section > ol > li:nth-child({i}) > div > a')[0].get_text())
    return article_titles

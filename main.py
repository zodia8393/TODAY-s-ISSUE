# main.py

import schedule
import time
from news_scanner import scan_news
from summarizer import summarize_texts
from sms_sender import send_sms

# 매일 오후 10시에 뉴스 스캐닝 및 요약 문자 전송 작업 실행
def job():
    article_titles = scan_news()
    summarized_texts = summarize_texts(article_titles)
    send_sms(article_titles, summarized_texts)

schedule.every().day.at("22:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

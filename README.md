# TODAY-s-ISSUE

news_summarizer 모듈 사용 설명서
1. 모듈의 이름과 버전
모듈의 이름: news_summarizer
버전: 1.0.0

2. 모듈의 설치 방법
news_summarizer 모듈을 설치하려면, 다음과 같은 명령어를 실행합니다.

Copy code
pip install news_summarizer
3. 모듈의 기능과 사용 예시
news_summarizer 모듈은 네이버 뉴스 페이지에서 기사를 스캐닝하고, BERT 모델을 이용하여 텍스트 요약을 수행한 후 문자 메시지를 발송하는 기능을 제공합니다.

python
Copy code
from news_summarizer import summarize_news

# 뉴스 스캐닝 및 요약 문자 전송 작업 실행
summarize_news()
4. 모듈의 API 문서
summarize_news()
입력: 없음
출력: 없음
동작: 네이버 뉴스 페이지에서 기사를 스캐닝하고, BERT 모델을 이용하여 텍스트 요약을 수행한 후 문자 메시지를 발송합니다.
5. 모듈의 제한 사항과 주의 사항
summarize_news() 함수에서 사용된 Twilio API의 발신 전화번호와 인증 토큰, 수신 전화번호 등은 모듈 사용자가 직접 설정해주어야 합니다.
모듈의 사용을 위해서는 requests, bs4, konlpy, transformers, torch, twilio 라이브러리가 필요합니다.
BERT 모델 파일이 저장된 경로에 따라 summarizer.py 파일의 model.load_state_dict(torch.load('saved_model.pth', map_location=torch.device('cpu'))) 부분을 적절히 수정해야 합니다.
news_summarizer 모듈은 현재 한글 기사에 대해서만 작동합니다.

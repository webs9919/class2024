import requests
from bs4 import BeautifulSoup
import json
import datetime

# 현재 날짜를 문자열로 저장
current_date = datetime.datetime.now().strftime("%Y-%m-%d")

# 웹 페이지로부터 데이터 요청 및 수신
response = requests.get("https://music.bugs.co.kr/chart")
soup = BeautifulSoup(response.text, "lxml")

# 데이터 선택
rankings = [rank.text.strip() for rank in soup.select(".ranking > strong")]
titles = [title.text.strip() for title in soup.select(".title > a")]
artists = [artist.text.strip() for artist in soup.select(".artist > a:nth-child(1)")]
images = [img['src'].strip() for img in soup.select(".thumbnail > img")]

# 데이터를 리스트 of 딕셔너리 형태로 구성
chart_data = []
for ranking, title, artist, image_url in zip(rankings, titles, artists, images):
    chart_data.append({
        "Ranking": ranking,
        "Title": title,
        "Artist": artist,
        "ImageURL": image_url
    })

# 파일 이름 설정
file_name = f"bugs100_{current_date}.json"

# JSON 파일로 저장
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(chart_data, file, ensure_ascii=False, indent=4)
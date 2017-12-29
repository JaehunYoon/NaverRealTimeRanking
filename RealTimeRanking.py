# 네이버 실시간 검색어 크롤러

import requests  # requests 라이브러리를 사용하기 위해 import
from os import system  # clear screen 기능을 사용하기 위해 os 라이브러리에서 system 함수를 import
from bs4 import BeautifulSoup  # 크롤링에 유용한 BeautifulSoup4 라이브러리 사용
from time import sleep  # 시간 간격을 주어 실시간 검색어 순위를 주기적으로 업데이트하기 위해 time 라이브러리에서 sleep 함수를 import
from datetime import datetime  # 시간 정보를 받아오기 위해 datetime 라이브러리 사용


def time_check():  # 정보를 수집해온 시간을 출력하기 위해 현재 시간 정보를 반환하는 함수
    now = datetime.now()  # 현재 시간을 now 변수에 저장
    now_time = f"<{now.year}. {now.month}. {now.day} - {now.hour}:{now.minute} 기준 네이버 실시간 검색어 순위>"

    return now_time  # 현재 시간 정보를 반환


while True:  # 실시간으로 계속 업데이트를 하기 위한 반복문
    html = requests.get('https://www.naver.com/').text  # 네이버 html 소스코드를 html 변수에 저장
    soup = BeautifulSoup(html, 'lxml')  # lxml을 이용하여 웹 페이지를 파싱
    rank_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
    # PM_CL_realtimeKeyword_rolling 라는 class에서 class명이 ah_k인 span 태그 형식의 내용만 select로 저장

    print(time_check() + "\n")  # 함수에서 반환된 시간 정보 출력 + 개행
    for rank, title in enumerate(rank_list, 1):  # Python 내장함수인 enumerate를 이용하여 반복문 실행
        print(rank, title.text)  # 순위와 제목 출력
        sleep(0.75)  # 0.75초를 간격으로 1위부터 20위까지 순차적으로 출력
    sleep(10)  # 10초 경과 시 실시간 검색어 순위 정보를 업데이트 하기 위해 sleep 사용
    system('cls')  # 10초 후 화면 초기화
    print("\n")

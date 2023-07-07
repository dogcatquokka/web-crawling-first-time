import requests
from bs4 import BeautifulSoup

url = "https://entertain.naver.com/movie"
response = requests.get(url)
html = response.text
soap = BeautifulSoup(html,"html.parser")
important = BeautifulSoup(html,"html.parser")
#select_one 하나만 가져옴
#Select() 모두 다 가져옴
titles = soap.select("a.tit")
imp = important.select_one("h2.end_tit")


#미션1. 관심있는 키워드를 프로그램 실행시 직접 입력하자
keyward = str(input("관심있는 키워드 입력하시오 :") )
for title in titles :
    if keyward in title.text :
        print(title.text)
 






#미션2. 내가 입력한 키워드가 포합된 제목만 화면에 출력하자
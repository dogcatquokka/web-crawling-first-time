# https://finance.naver.com/item/sise.naver?code=086520

import requests
from bs4 import BeautifulSoup


url = "https://finance.naver.com/item/sise.naver?code=086520"
response = requests.get(url)

html =response.text

soap = BeautifulSoup(html,"html.parser")

a = soap.select_one("strong.tah.p11")
print(a.text)




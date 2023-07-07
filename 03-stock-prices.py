# https://finance.naver.com/item/sise.naver?code=086520 005380, 161890
import requests
from bs4 import BeautifulSoup

codes = ["086520","005380","161890"]
url = "https://finance.naver.com/item/sise.naver?code=%s"
prices =[]

for code in codes :




    response = requests.get(url % code)

    html =response.text

    soap = BeautifulSoup(html,"html.parser")
    a = soap.select_one("strong.tah.p11")
    prices.append(a.text)
print(prices)





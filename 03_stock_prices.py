#현대차 005380
#카카오 035720
#이수페타시스 007660

import requests 
from bs4 import BeautifulSoup

codes = ["005380", "035720", "007660"]
url = "https://finance.naver.com/item/sise.naver?code=%s"
prices = []

for code in codes :
    response = requests.get(url % code)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    price = soup.select_one("strong#_nowVal")
    prices.append(price.text)
    
print(prices)

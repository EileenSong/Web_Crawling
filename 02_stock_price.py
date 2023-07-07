
import requests 
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/sise.naver?code=247540"
response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, "html.parser")

# 스트롱태그인데 id가 nowVal인것
#strong.tah.p11
price = soup.select_one("strong#_nowVal")
print(price.text)

import requests 
from bs4 import BeautifulSoup


#네이버 증권 : https://finance.naver.com/


response = requests.get("https://finance.naver.com/")

#웹페이지는 html 언어로 구성되어 있다
html = response.text

result = BeautifulSoup(html, "html.parser")

info = result.select_one("h2.h_market")
print(info.text)
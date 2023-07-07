import requests 
from bs4 import BeautifulSoup

url = "https://entertain.naver.com/movie"

response = requests.get(url)
html = response.text


soup = BeautifulSoup(html, "html.parser")

#select_one은 해당하는 정보 하나를 가져오는 것
#select는 해당하는 정보라면 모두 골라서 다 가져온다

titles = soup.select("a.title")


search_word = input("관심있는 키워드를 입력해 주세요:")
for title in titles: 
    if search_word in title.text:
        print(title.text)
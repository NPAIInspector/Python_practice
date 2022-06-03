import requests
from bs4 import BeautifulSoup


result = requests.get('https://news.yahoo.co.jp/')
info01 = BeautifulSoup(result.text, 'html.parser')
info02 = info01.find_all("div", class_="yjnSub_list_text")

for news in info02:
    print(news.getText())
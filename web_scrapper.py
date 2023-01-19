from bs4 import BeautifulSoup
import requests

url = "https://trade.sa.nexon.com/"
request = requests.get(url, headers={"User-Agent":"Kimchi"})

if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")

    items_info = soup.find('div', class_="item-list show-cursor")
    print(items_info)
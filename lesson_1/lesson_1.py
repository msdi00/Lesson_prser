import requests
from bs4 import BeautifulSoup

# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
# headers = {
#     "accept": "*/*",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
# }

# req = requests.get(url)

with open('url_text.html', encoding='utf-8') as file_url:
    src = file_url.read()

soup = BeautifulSoup(src, "lxml")
all_products_href = soup.find_all(class_="mzr-tc-group-item-href")
for item in all_products_href:
    print(item)

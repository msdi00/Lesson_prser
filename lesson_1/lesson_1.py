import requests
from bs4 import BeautifulSoup

url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

# req = requests.get(url)
with open('url_text', 'r', encoding='utf-8') as file_url:
    req = file_url.read()


src = req
print(src)
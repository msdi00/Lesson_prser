import requests
from bs4 import BeautifulSoup
import json
import re
import csv

# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
# headers = {
#     "accept": "*/*",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"

# req = requests.get(url)

# with open('url_text.html', encoding='utf-8') as file_url:
#     src = file_url.read()
#
# soup = BeautifulSoup(src, "lxml")
# all_products_href = soup.find_all(class_="mzr-tc-group-item-href")
# all_category_dict = {}
# for item in all_products_href:
#     item_text = item.text
#     item_href = "https://health-diet.ru" + item.get("href")
#     print(f'{item_text}: {item_href}')
#     all_category_dict[item_text] = item_href

# with open("all_category_href.json", "w", encoding='utf-8') as file:
#     json.dump(all_category_dict, file, indent=4, ensure_ascii=False)

# with open("all_category_href.json", encoding='utf-8') as file:
#     all_categories = json.load(file)
#
#     redacted_json = {}
#     for item, value in all_categories.items():
#         redacted_json[re.sub(r'\W*\s+', '_', item)] = value
#         with open("all_category_href.json", "w", encoding='utf-8') as file_w:
#             json.dump(redacted_json, file_w, indent=4, ensure_ascii=False)

with open("all_category_href.json", encoding='utf-8') as file_r:
    all_categories = json.load(file_r)

count = 0
for category_name, category_href in all_categories.items():
    if count == 0:
        with open(f"E:\\Projects\\Lesson_prser\\data\\{count}_{category_name}.html", encoding='utf-8') as file_w:
            scr = file_w.read()
            soup = BeautifulSoup(scr, "lxml")
            # table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")

            # priduct = table_head[0].text
            # calories = table_head[1].text
            # proteins = table_head[2].text
            # fats = table_head[3].text
            # carbohydrates = table_head[4].text
            #
            # with open(f"E:\\Projects\\Lesson_prser\\data_csv\\{count}_{category_name}.csv", "w", encoding='utf-8') as file_w_csv:
            #     writer = csv.writer(file_w_csv)
            #     writer.writerow(
            #         (
            #             priduct,
            #             calories,
            #             proteins,
            #             fats,
            #             carbohydrates
            #
            #         )
            #     )

            product_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")

            for item in product_data:
                product_tds = item.find_all("td")
                title = product_tds[0].find("a").text
                calories = product_tds[1].text
                proteins = product_tds[2].text
                fats = product_tds[3].text
                carbohydrates = product_tds[4].text
                print(proteins)

            count += 1





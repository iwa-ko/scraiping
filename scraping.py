import requests
from bs4 import BeautifulSoup

# ターゲットのURL
url = 'https://twich.tv'

# ページの取得
response = requests.get(url)

# ページの解析
soup = BeautifulSoup(response.text, 'html.parser')

# 例: タイトルの取得
title = soup.title.text
print('タイトル:', title)

# # 例: 特定の要素の取得
# # この例では、クラスが "example-class" のすべての div 要素を取得しています
# example_divs = soup.find_all('div', class_='example-class')
# for div in example_divs:
#     print('例のdiv:', div.text)
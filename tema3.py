"""
● Să se scrie un web scraper care obține date pe care le afișează într-un fișier:
○ datele ce urmează a fi obținute sunt la alegere (pentru lipsă de idei puteți obține informații despre articolele
disponibile la adresa http://frsah.ro/)
○ formatul fișierului și modul de stocare al datelor este la alegere.
○ extra:
➠ adăugați funcționalitate de citire a informației din fișier și afișarea ei în consolă.
➠ adăugați funcționalitate de citire a informației anterioare și completarea acesteia cu informații noi
"""

import requests
from bs4 import BeautifulSoup

URL = 'http://frsah.ro/stiri/'
html_text = requests.get(URL).text
with open('html_file', 'w', encoding="utf-8") as file:
    file.write(html_text)

soup = BeautifulSoup(html_text, 'html.parser')

news_content = soup.find('div', class_='jeg_posts jeg_load_more_flag')
news = news_content.find_all('h3', class_='jeg_post_title')
pub_date = news_content.find_all('div', class_='jeg_meta_date')

for one_pub_date in pub_date:
    date_cell = one_pub_date.find('a')
    published_date = date_cell.text
    print(published_date)

if 'aprilie' in published_date:
    for one_news in news:
        news_cell = one_news.find('a')
        news_title = news_cell.text
        print(news_title)




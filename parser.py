import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3 import Retry
import re


url = "https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md"
#Обход ограничения запросов к старнице
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('https://', adapter)


# Загрузка страницы
response = session.get(url)
html = response.text

# Извлечение информации
soup = BeautifulSoup(html, "html.parser")
repos = soup.find_all("tr")

for repo in repos:
    rait = repo.find_all("td")[0:1]
    for i in rait:
        rait = int(i.text)

    name = repo.find_all("td")[1:2]
    for i in name:
        name = i.find("a")['href'].replace('https://github.com/',"").replace('"', "").replace("\\",'')

    stars = repo.find_all("td")[2:3]
    for i in stars:
        stars = int(i.text)

    forks = repo.find_all("td")[3:4]
    for i in forks:
        forks = int(i.text)
    issues = repo.find_all("td")[5:6]
    for i in issues:
        issues = int(i.text)
    language = repo.find_all("td")[4:5]
    for i in language:
        language = i.text

    """количество просмотров и подключение"""
    url_page = f"https://github.com/{name}"
    response_page = session.get(url_page)
    html_page = response_page.text

    """Извлечение информации о просмотрах"""

    soup_page = BeautifulSoup(html_page, "html.parser")
    views = soup_page.find_all("a", href=f"/{name}/watchers")
    for i in views:
        views = i.text.replace("\n", "").replace("watching", "").replace(" ", "")
        if "k" in views:
            views = int(float(views.replace("k",""))*1000)







    """Извлечение информации о владельцах"""
    owner_link = soup_page.find_all("li", class_='mb-2 mr-2')
    owners = []
    for i in range(len(owner_link)):
        owners.append(owner_link[i].find("a")["href"].replace("https://github.com/", ""))
        dict = {
            "repo":name,
            "owner":owners,
            "position_cur":rait,
            "position_prev":rait-1,
            "stars":stars,
            "watchers":views,
            "forks":forks,
            "open_issues":issues,
            "language":language
        }
    print(dict)



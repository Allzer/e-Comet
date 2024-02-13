import json

import requests
from bs4 import BeautifulSoup

# Загрузка страницы
url = "https://github.com/trending?since=monthly"
response = requests.get(url)
html = response.text

# Извлечение информации
soup = BeautifulSoup(html, "html.parser")
repos = soup.find_all("article", class_="Box-row")

# Вывод информации о репозиториях
for repo in repos[:1]:
    # Название репозитория
    repo_name_elem = repo.find("h2", class_="h3 lh-condensed")
    if repo_name_elem:
        repo_name = repo_name_elem.text.replace("\n","").replace(" ","")
    else:
        repo_name = "РЕпозиторий без названия"

    # Количество звезд
    stars_elem = repo.find("a", class_="Link--muted")
    if stars_elem:
        stars = stars_elem.text.strip()
    else:
        stars = "Звёзды не найдены"

    # Владелец репозитория
    owners = []
    owner_elems = repo.find_all("a", class_="d-inline-block")
    for owner_elem in owner_elems:
        owner = owner_elem["href"].split("/")[-1]
        owners.append(owner)

    if owners:
        owner_str = ", ".join(owners)
    else:
        owner_str = "Owner not found"

    del owners[:2]


    print("Repository:", repo_name)
    print("Stars:", stars)
    print("Owners", owners)

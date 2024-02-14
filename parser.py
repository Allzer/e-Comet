import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3 import Retry
import re


session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('https://', adapter)
url = "https://github.com/trending?since=monthly"


# Загрузка страницы
response = session.get(url)
html = response.text

# Извлечение информации
soup = BeautifulSoup(html, "html.parser")
repos = soup.find_all("article", class_="Box-row")

counter = 0
# Вывод информации о репозиториях
for repo in repos[:1]:
    counter += 1
    """Название репозитория"""
    repo_name_elem = repo.find("h2", class_="h3 lh-condensed")
    if repo_name_elem:
        repo_name = repo_name_elem.text.replace("\n","").replace(" ","")
    else:
        repo_name = "Репозиторий без названия"

    """Количество звезд"""
    stars_elem = repo.find("a", class_="Link--muted")
    if stars_elem:
        stars = stars_elem.text.strip()
    else:
        stars = "Звёзды не найдены"

    """Владелец репозитория"""
    owners = []
    owner_elems = repo.find_all("a", class_="d-inline-block")
    for owner_elem in owner_elems:
        owner = owner_elem["href"].split("/")[-1]
        owners.append(owner)

    if owners:
        owner_str = ", ".join(owners)
    else:
        owner_str = "Владелец не найден"
    del owners[:2]

    """Количество форков"""
    forks_elem = repo.find("a", class_="Link--muted", href=lambda href: href and "/forks" in href)
    if forks_elem:
        forks_text = forks_elem.text.strip().replace(",","")
    else:
        forks_text = "Колчиество форков не найдено"

    # Количество открытых issues
    issues_elem = repo.find("a", class_="Link--muted", href=lambda href: href and "/issues" in href)
    if issues_elem:
        issues_text = issues_elem.text.strip()
    else:
        issues_text = "Issues count not found"

    """количество просмотров"""
    url_page = f"https://github.com/{repo_name}"
    response_page = session.get(url_page)
    html_page = response_page.text

    # Извлечение информации
    soup_page = BeautifulSoup(html_page, "html.parser")
    views = soup_page.find("a", href=f"/{repo_name}/watchers").text.replace("\n","").replace("watching","")





    print("Repository:", repo_name)
    print("Stars:", stars)
    print("Owners", owners)
    print("Position", counter)
    print("Watchers", views)
    print("Forks", forks_text)
    print("Issues", issues_text)


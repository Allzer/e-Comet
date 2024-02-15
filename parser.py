import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3 import Retry


url = "https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md"
def parser(url):
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
    repos = soup.find_all("tbody")

    for repo in repos[:1]:
        rait = int(repo.find_all("td")[0].text)
        name = repo.find_all("td")[1].find("a")["href"].replace('https://github.com/',"").replace('"', "").replace("\\",'')
        stars = int(repo.find_all("td")[2].text)
        forks = int(repo.find_all("td")[3].text)
        issues = int(repo.find_all("td")[5].text)
        language = repo.find_all("td")[4].text


        """количество просмотров и подключение"""
        url_page = f"https://github.com/{name}"
        response_page = session.get(url_page)
        html_page = response_page.text

        """Извлечение информации о просмотрах"""
        soup_page = BeautifulSoup(html_page, "html.parser")
        views = int(soup_page.find("a", href=f"/{name}/watchers").text.replace("\n", "").replace("watching", "").replace("k","00").replace(" ","").replace(".",""))




        """Извлечение информации о владельцах"""
        owner_link = soup_page.find_all("li", class_='mb-2 mr-2')
        owners = []
        for i in range(len(owner_link)):
            owners.append(owner_link[i].find("a")["href"].replace("https://github.com/",""))

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

        return dict

        #print("Название", name)
        #print("Владелец", owners)
        #print("Рейтинг", rait)
        #print("Предыдущая позиция в топе", rait-1)
        #print("Кол-во звёзд", stars)
        #print("Кол-во просмотров", views)
        #print("Кол-во форков", forks)
        #print("Кол-во issues", issues)
        #print("Язык", language)
        #print("")

print(parser(url))

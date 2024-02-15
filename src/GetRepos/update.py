from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker

from src.GetRepos.models import repos
from src.GetRepos.parser import parser
from src.config import URL
from src.database import DB_URL

# Create engine
engine = create_engine(DB_URL)

# Define metadata
metadata = MetaData()



# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Define the update function
def update(pars):
    print("Начало update")

    try:
        for k, v in pars.items():
            session.execute(repos.insert().values(
                repo=k,
                owner=v["owner"],
                position_cur=v["position_cur"],
                position_prev=v["position_prev"],
                stars=v["stars"],
                watchers=v["watchers"],
                forks=v["forks"],
                open_issues=v["open_issues"],
                language=v["language"],
            ))
        session.commit()
    except Exception as pp:
        print(pp)
    finally:
        session.close()
        print("Закончил работу\n")

# Ваш парсер должен вернуть словарь с данными
pars = parser(URL)

# Call the update function
update(pars)
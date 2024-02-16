from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.GetRepos.models import repos, owners  # Импорт моделей для всех таблиц
from src.database import DB_URL

# Create engine


# Define the update function
def update(parser):
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Начало update")

    try:
        for k, v in parser.items():  # k - название репозитория, v - информация о репозитории
            # Добавление данных в таблицу "repos"
            repo_insert = repos.insert().values(
                repo=k,
                owner=v["owner"],
                position_cur=v["position_cur"],
                position_prev=v["position_prev"],
                stars=v["stars"],
                watchers=v["watchers"],
                forks=v["forks"],
                open_issues=v["open_issues"],
                language=v["language"],
            )
            repo_id = session.execute(repo_insert).inserted_primary_key[0]  # Получаем id добавленной записи

            # Добавление данных в таблицу "owners"
            for owner in v["owner"]:
                session.execute(owners.insert().values(
                    owner_name=owner,
                    repo_id=repo_id
                ))

            print(f"add: {k}")

        session.commit()
        print("Завершено успешно")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при выполнении: {e}")
    finally:
        session.close()



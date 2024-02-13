from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

repos = Table(
    "repos",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("repo",String), #название репозитория (full_name в API GitHub)
    Column("owner",String), #владелец репозитория
    Column("position_cur",Integer), #текущая позиция в топе
    Column("position_prev", Integer),  #предыдущая позиция в топе
    Column("stars", String), #количество звёзд
    Column("watchers",Integer), #количество просмотров
    Column("forks", Integer), #количество форков
    Column("open_issues", Integer), #количество открытых issues
    Column("language", String) #язык
)


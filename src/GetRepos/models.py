from sqlalchemy import (ForeignKeyConstraint,
                        create_engine, MetaData, Table, Column, Integer, String, ForeignKey)

from src.database import DB_URL

metadata = MetaData()

# Создание базы данных
engine = create_engine(DB_URL)

# Определение таблицы репозиториев
repos = Table(
    'repos',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('repo', String),
    Column('owner', String),
    Column('position_cur', Integer),
    Column('position_prev', Integer),
    Column('stars', Integer),
    Column('watchers', Integer),
    Column('forks', Integer),
    Column('open_issues', Integer),
    Column('language', String),
)

# Определение таблицы владельцев
owners = Table('owners',
               metadata,
               Column('id', Integer, primary_key=True),
               Column('owner_name', String),
               Column('repo_id', Integer, ForeignKey('repos.id')),  # Не указываем ForeignKey здесь
               )


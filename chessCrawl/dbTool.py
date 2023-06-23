import json
from clize.converters import file
from clize.parameters import argument_decorator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# def create_ssession(db, user, host, password):
#     engine = create_engine(
#         "postgresql+psycopg2://{}:{}@{}/{}".format(user, password, host, db)
#     )
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     return session


def dictToSql(itemDic, table):
    """dict to sql insert string
    :param itemDic: the time dict to sql str
    :type itemDic: dict
    :param table: the table name
    :type table: str
    """
    keys = itemDic.keys()
    columns = ",".join(keys)
    valuesHolders = ",".join([":" + key for key in keys])
    insert_sql = """INSERT INTO {table} 
    ({columns})
    VALUES({valuesHolder}) 
    ON CONFLICT DO NOTHING""".format(
        table=table, columns=columns, valuesHolder=valuesHolders
    )
    return insert_sql


def insert_data(items, table, session):
    itemOne = items[0]
    insert_sql = dictToSql(itemOne, table)

    for item in items:
        session.execute(insert_sql, item)
    session.commit()


def create_ssession(db="postgres", *, u="postgres", host="127.0.0.1", p=""):
    engine = create_engine(
        # "postgresql+psycopg2://{}:{}@{}/{}".format(user, password, host, db)
        "postgresql+psycopg2://{}:{}@{}/{}".format(u, p, host, db)
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def create_eng(db="postgres", *, u="postgres", host="127.0.0.1", p=""):
    engine = create_engine(
        # "postgresql+psycopg2://{}:{}@{}/{}".format(user, password, host, db)
        "postgresql+psycopg2://{}:{}@{}/{}".format(u, p, host, db)
    )
    return engine


@argument_decorator
def __create_ssession(db="postgres", *, u="postgres", host="127.0.0.1", p=""):
    engine = create_engine(
        # "postgresql+psycopg2://{}:{}@{}/{}".format(user, password, host, db)
        "postgresql+psycopg2://{}:{}@{}/{}".format(u, p, host, db)
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def sqlProcess(table, session: __create_ssession, input: file = "-"):
    jsonItems = None
    with input as f:
        if f.readable() and not f.isatty():
            jsonItems = f.read()
        else:
            return
    items = json.loads(jsonItems)
    itemOne = items[0]
    insert_sql = dictToSql(itemOne, table)

    for item in items:
        session.execute(insert_sql, item)

    # sqlItems = [list(item.values()) for item in items]
    # session.executemany(insert_sql,sqlItems)

    # itemLists = group_elements(items, 1000)
    # for itemList in itemLists:
    #     sqlItems = [list(item.values()) for item in itemList]
    #     session.executemany(insert_sql,sqlItems)

    session.commit()


if __name__ == "__main__":
    from clize import run

    run(sqlProcess)

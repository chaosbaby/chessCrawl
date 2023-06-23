sqlStr = """
CREATE TABLE chess_play (
    id INTEGER UNIQUE,
    DhtmlXQ_movelist TEXT,
    DhtmlXQ_ver VARCHAR(50),
    DhtmlXQ_init VARCHAR(20),
    DhtmlXQ_pver VARCHAR(20),
    DhtmlXQ_viewurl TEXT,
    DhtmlXQ_adddate DATETIME,
    DhtmlXQ_editdate DATETIME,
    DhtmlXQ_title VARCHAR(255),
    DhtmlXQ_binit TEXT,
    DhtmlXQ_firstnum INT,
    DhtmlXQ_length INT,
    DhtmlXQ_type VARCHAR(50),
    DhtmlXQ_gametype VARCHAR(50),
    DhtmlXQ_other TEXT,
    DhtmlXQ_open VARCHAR(255),
    DhtmlXQ_class VARCHAR(50),
    DhtmlXQ_event VARCHAR(50),
    DhtmlXQ_group TEXT,
    DhtmlXQ_round TEXT,
    DhtmlXQ_table TEXT,
    DhtmlXQ_date DATE,
    DhtmlXQ_place VARCHAR(255),
    DhtmlXQ_timerule TEXT,
    DhtmlXQ_red VARCHAR(255),
    DhtmlXQ_redteam VARCHAR(50),
    DhtmlXQ_redname VARCHAR(255),
    DhtmlXQ_redlevel INT,
    DhtmlXQ_redeng INT,
    DhtmlXQ_redrating INT,
    DhtmlXQ_redtime TEXT,
    DhtmlXQ_black VARCHAR(255),
    DhtmlXQ_blackteam VARCHAR(50),
    DhtmlXQ_blackname VARCHAR(255),
    DhtmlXQ_blacklevel INT,
    DhtmlXQ_blackeng INT,
    DhtmlXQ_blackrating INT,
    DhtmlXQ_blacktime TEXT,
    DhtmlXQ_result VARCHAR(50),
    DhtmlXQ_endtype TEXT,
    DhtmlXQ_judge TEXT,
    DhtmlXQ_record TEXT,
    DhtmlXQ_remark TEXT,
    DhtmlXQ_author VARCHAR(255),
    DhtmlXQ_refer TEXT,
    DhtmlXQ_hits INT,
    DhtmlXQ_price INT,
    DhtmlXQ_sortid INT,
    DhtmlXQ_owner VARCHAR(50),
    DhtmlXQ_oldowner VARCHAR(50),
    DhtmlXQ_hidden INT
);

"""

import sqlite3


def init():
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute(sqlStr)


from chessCrawl import wrapper

import json


def jsonLoad(jsonStr):
    """TODO: Docstring for jsonLoad.
    :returns: TODO

    """
    return json.loads(jsonStr)


def toSqlPairs(data_dict, table_name):
    """TODO: Docstring for tosqlStr.
    :returns: TODO

    """
    keys = list(data_dict.keys())
    values = list(data_dict.values())

    # Construct the SQL query string
    columns = ", ".join(keys)
    placeholders = ", ".join("?" * len(values))
    query = f"INSERT OR IGNORE INTO {table_name} ({columns}) VALUES ({placeholders})"
    return query, values


@wrapper.process_parameter("data_dict", json.loads)
@wrapper.process_parameter("data_dict", json.loads)
def insert(data_dict=None, table_name=None, db_path=None):
    """
    Inserts a dictionary as a row into the specified database table.

    :param data_dict: The dictionary containing the data to insert.
    :param table_name: The name of the database table to insert into.
    :param db_path: The path to the database file.
    """
    # Open a connection to the database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    query, values = toSqlPairs(data_dict, table_name)
    # Get the keys and values from the dictionary

    # Execute the query with the dictionary values as parameters
    c.execute(query, values)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    wrapper.__name__ = "__main__"
    from clize import run

    run(init, insert)

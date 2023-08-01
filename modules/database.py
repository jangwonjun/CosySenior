import pymysql
from env import SQL
from flask.cli import with_appcontext
from flask import current_app, g
import click


def init_db():
    conn, cur = get_db_direct()
    if is_database_created(cur):
        cur.execute(f"USE {SQL.DB_NAME}")
    else:
        print("생성 시도")
        create_database(cur)
        conn.commit()
        exit()


def get_db_direct():
    conn = pymysql.connect(
        host=SQL.HOST, port=SQL.PORT, user=SQL.ID, passwd=SQL.PASSWORD, charset='utf8'
    )
    return conn, conn.cursor()


def get_db():
    conn = pymysql.connect(
        host=SQL.HOST, port=SQL.PORT, user=SQL.ID, passwd=SQL.PASSWORD, db=SQL.DB_NAME, charset='utf8'
    )
    if "db" not in g:
        g.conn = conn
        g.db = conn.cursor()
    return g.db


def commit():
    g.conn.commit()


def close_db(e=None):
    db = g.pop("db", None)
    conn = g.pop("conn", None)
    if db is not None:
        db.close()


@click.command('init-db')
@with_appcontext
def init_db_command():
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def search_one(query, query_item=tuple()):
    cur = get_db()

    cur.execute(query, query_item)
    return cur.fetchone()


def search_all(query, query_item=tuple()):
    cur = get_db()
    cur.execute(query, query_item)
    return cur.fetchall()


def execute_query(query, query_item=tuple()):
    cur = get_db()
    cur.execute(query, query_item)
    conn.commit()


def is_database_created(cur):
    query = "SHOW DATABASES LIKE %s;"
    cur.execute(query, (SQL.DB_NAME,))
    get = cur.fetchone()
    return get is not None


def create_database(cur):
    query = f"""
    CREATE DATABASE {SQL.DB_NAME};
    """
    cur.execute(query)
    cur.execute(f"USE {SQL.DB_NAME}")
    with open('./queries.sql', 'r') as r:
        queries = r.read().split("\n\n")
        for query in queries:
            cur.execute(query)

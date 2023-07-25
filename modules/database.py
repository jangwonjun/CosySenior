import pymysql
from env import SQL
from flask.cli import with_appcontext
from flask import current_app, g
import click


def init_db():
    if is_database_created():
        execute_query(f"USE {SQL.DB_NAME}")
    else:
        print("생성 시도")
        create_database()

def get_db():
    conn = pymysql.connect(
        host=SQL.HOST, port=SQL.PORT, user=SQL.ID, passwd=SQL.PASSWORD, charset='utf8'
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


def is_database_created():
    query = "SHOW DATABASES LIKE %s;"
    get = search_one(query, (SQL.DB_NAME,))
    return get is not None


def create_database():
    query = f"""
    CREATE DATABASE {SQL.DB_NAME};
    """
    execute_query(query)

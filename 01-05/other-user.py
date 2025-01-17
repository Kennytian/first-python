import sqlalchemy as sa
from dotenv import load_dotenv
import os

load_dotenv()
database_url = os.getenv("DATABASE_URL")

engine = sa.create_engine("sqlite:///:memory:", echo=True)
# engine = sa.create_engine(database_url, echo=True)
connection = engine.connect()

metadata = sa.MetaData()

user_table = sa.Table(
    "user11",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("username", sa.String),
    sa.Column("email", sa.String),
)


def insert_user(username: str, email: str) -> None:
    query = user_table.insert().values(username=username, email=email)
    connection.execute(query)


def select_user(username: str) -> sa.engine.Result:
    query = user_table.select().where(user_table.c.username == username)
    result = connection.execute(query)
    return result.fetchone()


def main() -> None:
    metadata.create_all(engine)
    insert_user("Jerry", "jerry@tom.com")
    print(select_user("Jerry"))
    connection.close()


if __name__ == "__main__":
    main()

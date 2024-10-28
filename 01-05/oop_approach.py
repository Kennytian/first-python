import os

import sqlalchemy as sa
from dotenv import load_dotenv

from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base

load_dotenv()
database_url = os.getenv("DATABASE_URL")

db = sa.create_engine(database_url, echo=True)
Session = sessionmaker(bind=db)
Base = declarative_base()


class User(Base):
    __tablename__ = "user22"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    username: Mapped[str]
    email: Mapped[str]

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"


def main() -> None:
    Base.metadata.create_all(db)
    user = User(username="Jerry", email="jerry@mail.com")
    second_user = User(username="Tom", email="tom@mail.com")

    with Session() as session:
        session.add(user)
        session.add(second_user)
        session.commit()
        print(session.query(User).all())


if __name__ == "__main__":
    main()

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class SomeTable(Base):
    __tablename__ = 'some_table'

    id = Column(Integer, primary_key=True, autoincrement=True)
    some_column = Column(String)


engine = create_engine('sqlite:///../../memory.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
nb_rows: int = session.query(SomeTable).count()

some_tables = session.query(SomeTable)
for some_table in some_tables:
    print(f"Found {some_table.some_column}")

print(f"Inserted content #{nb_rows}")
some_table = SomeTable(some_column=f"content #{nb_rows}")
session.add(some_table)
session.commit()



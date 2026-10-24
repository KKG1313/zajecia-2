import random
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, create_engine, delete, select, update
from sqlalchemy.orm import Session, declarative_base

engine = create_engine("sqlite:///baza.db", echo=False)

Base = declarative_base()


class Experiment(Base):
    __tablename__ = "experiments"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    created_at = Column(DateTime)
    type = Column(Integer)
    finished = Column(Boolean, default=False)


class DataPoint(Base):
    __tablename__ = "data_points"

    id = Column(Integer, primary_key=True)
    real_value = Column(Float)
    target_value = Column(Float)


Base.metadata.create_all(engine)

with Session(engine) as session:
    # 1. Dodanie 2 wierszy
    session.add_all([
        Experiment(title="Eksperyment A", created_at=datetime.now(), type=1),
        Experiment(title="Eksperyment B", created_at=datetime.now(), type=2),
    ])

    # 2. Dodanie 10 pomiarów
    session.add_all([
        DataPoint(real_value=random.random(), target_value=random.random())
        for _ in range(10)
    ])
    session.commit()

    # 3. Pobranie i wyświetlenie danych
    print("Eksperymenty:")
    experiments = session.scalars(select(Experiment)).all()
    for experiment in experiments:
        print(experiment.id, experiment.title, experiment.type, experiment.finished)

    print("Pomiary")
    data_points = session.scalars(select(DataPoint)).all()
    for point in data_points:
        print(point.id, point.real_value, point.target_value)

    # 4. Aktualizacja
    session.execute(update(Experiment).values(finished=True))
    session.commit()

    print("Eksperymenty po aktualizacji:")
    for experiment in session.scalars(select(Experiment)).all():
        print(experiment.id, experiment.title, experiment.finished)

    # 5. Usunięcie wszystkich wierszy z obu tabel
    session.execute(delete(DataPoint))
    session.execute(delete(Experiment))
    session.commit()

    print("Po usunięciu:")
    print("Eksperymentów:", len(session.scalars(select(Experiment)).all()))
    print("Pomiarów:", len(session.scalars(select(DataPoint)).all()))
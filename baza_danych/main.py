import random
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, create_engine, select
from sqlalchemy.orm import Session, declarative_base, relationship

engine = create_engine("sqlite:///baza.db", echo=False)

Base = declarative_base()


class Experiment(Base):
    __tablename__ = "experiments"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    created_at = Column(DateTime)
    type = Column(Integer)
    finished = Column(Boolean, default=False)

    data_points = relationship("DataPoint", back_populates="experiment")


class DataPoint(Base):
    __tablename__ = "data_points"

    id = Column(Integer, primary_key=True)
    real_value = Column(Float)
    target_value = Column(Float)

    experiment_id = Column(Integer, ForeignKey("experiments.id"))
    experiment = relationship("Experiment", back_populates="data_points")


Base.metadata.create_all(engine)

with Session(engine) as session:
    experiment_a = Experiment(title="Eksperyment A", created_at=datetime.now(), type=1)
    experiment_b = Experiment(title="Eksperyment B", created_at=datetime.now(), type=2)

    for _ in range(10):
        DataPoint(real_value=random.random(), target_value=random.random(), experiment=experiment_a)
        DataPoint(real_value=random.random(), target_value=random.random(), experiment=experiment_b)

    session.add_all([experiment_a, experiment_b])
    session.commit()

    for experiment in session.scalars(select(Experiment)).all():
        print(experiment.title, "liczba pomiarów:", len(experiment.data_points))
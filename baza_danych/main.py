from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite:///baza.db", echo=True)

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
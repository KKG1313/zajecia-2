from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Table, create_engine
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("sqlite:///baza.db", echo=False)

Base = declarative_base()


experiment_subject = Table(
    "experiment_subject",
    Base.metadata,
    Column("experiment_id", ForeignKey("experiments.id")),
    Column("subject_id", ForeignKey("subjects.id")),
)


class Experiment(Base):
    __tablename__ = "experiments"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    created_at = Column(DateTime)
    type = Column(Integer)
    finished = Column(Boolean, default=False)

    data_points = relationship("DataPoint", back_populates="experiment")
    subjects = relationship("Subject", secondary=experiment_subject, back_populates="experiments")


class DataPoint(Base):
    __tablename__ = "data_points"

    id = Column(Integer, primary_key=True)
    real_value = Column(Float)
    target_value = Column(Float)

    experiment_id = Column(Integer, ForeignKey("experiments.id"))
    experiment = relationship("Experiment", back_populates="data_points")


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    gdpr_accepted = Column(Boolean, default=False)

    experiments = relationship("Experiment", secondary=experiment_subject, back_populates="subjects")
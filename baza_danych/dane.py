import random
from datetime import datetime

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from main import DataPoint, Experiment, engine

with Session(engine) as session:
    experiment_a = Experiment(title="Eksperyment A", created_at=datetime.now(), type=1)
    experiment_b = Experiment(title="Eksperyment B", created_at=datetime.now(), type=2)

    for _ in range(10):
        DataPoint(real_value=random.random(), target_value=random.random(), experiment=experiment_a)
        DataPoint(real_value=random.random(), target_value=random.random(), experiment=experiment_b)

    session.add_all([experiment_a, experiment_b])
    session.commit()

    stmt = (
        select(Experiment.title, func.sum(DataPoint.real_value), func.avg(DataPoint.real_value))
        .join(Experiment.data_points)
        .group_by(Experiment.id)
    )

    for title, total, mean in session.execute(stmt):
        print(title, "suma:", round(total, 3), "średnia:", round(mean, 3))
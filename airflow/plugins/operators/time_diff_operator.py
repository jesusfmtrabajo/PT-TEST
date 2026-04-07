from datetime import datetime, timezone
from airflow.models.baseoperator import BaseOperator


class TimeDiffOperator(BaseOperator):
    def __init__(self, diff_date, **kwargs):
        super().__init__(**kwargs)
        self.diff_date = diff_date

    def execute(self, context):
        now = datetime.now(timezone.utc)
        diff = now - self.diff_date
        self.log.info("Current date: %s", now.isoformat())
        self.log.info("Input date: %s", self.diff_date.isoformat())
        self.log.info("Difference: %s", diff)
        return str(diff)
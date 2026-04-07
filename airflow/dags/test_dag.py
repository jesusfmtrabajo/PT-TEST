from datetime import datetime, timedelta, timezone

from airflow import DAG

from airflow.operators.dummy import DummyOperator

from operators.time_diff_operator import TimeDiffOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(1900, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(seconds=5),
}

with DAG(
    dag_id="test",
    default_args=default_args,
    schedule_interval="0 3 * * *",
    catchup=False,
    tags=["prueba_tecnica"],
) as dag:
    start = DummyOperator(task_id="start")
    end = DummyOperator(task_id="end")

    # Lista de tareas dummy task_n
    n_tasks = 6
    tasks = {}

    for i in range(1, n_tasks + 1):
        tasks[i] = DummyOperator(task_id=f"task_{i}")

    # Cada tarea par depende de todas las impares
    odd_tasks = [tasks[i] for i in tasks if i % 2 != 0]
    even_tasks = [tasks[i] for i in tasks if i % 2 == 0]

    for odd_task in odd_tasks:
        start >> odd_task

    for even_task in even_tasks:
        for odd_task in odd_tasks:
            odd_task >> even_task
        even_task >> end

    # Operador personalizado
    time_diff_task = TimeDiffOperator(
        task_id="time_diff_task",
        diff_date=datetime(2024, 1, 1, tzinfo=timezone.utc),
    )

    start >> time_diff_task >> end
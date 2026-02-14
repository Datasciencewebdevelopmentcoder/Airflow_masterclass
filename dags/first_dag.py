from airflow.sdk import dag, task
from datetime import datetime


@dag(
    dag_id="first_dag",
    start_date=datetime(2026, 2, 2),
    schedule_interval="@daily",
    catchup=False)


def first_dag():
    @task.python
    def first_task():
        print("This is the first task")
    
    @task.python
    def second_task():
        print("This is the second task")
    
    @task.python
    def third_task():
        print("This is the third task")
    
    first_task() >> second_task() >> third_task()


first_dag()

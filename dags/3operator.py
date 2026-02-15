from airflow.sdk import dag, task # type: ignore
from airflow.operators import bash, python # type: ignore
from datetime import datetime


@dag(
    dag_id="revised_dag",
    start_date=datetime(2026, 2, 2),
    schedule="@daily",
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
    @task.bash
    def fourth_task():
        return "echo This is the fourth task"
    
    first_task() >> second_task() >> third_task() >> fourth_task()


first_dag()

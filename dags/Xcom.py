from airflow.decorators import dag, task
from datetime import datetime

# 1. Added start_date and schedule (set to None for manual trigger)
@dag(
    dag_id="XCOM_Example",
    start_date=datetime(2023, 1, 1),
    schedule=None, 
    catchup=False
)
def first_dag():
    
    # 2. Changed @task.python to just @task (standard convention)
    @task
    def first_task():
        data = [1, 2, 3, 4, 5]
        return data  # This automatically pushes to XCom
    
    @task
    def second_task(data):
        data_sum = sum(data)
        print(f"Sum is: {data_sum}")
        return data_sum
    
    @task
    def third_task():
        print("This is the third task")
    
    # 3. Correct Dependency Logic
    # Capture the output of the first task
    data_output = first_task()
    
    # Pass that output into the second task (Implicit dependency created here)
    sum_output = second_task(data_output)
    
    # Use bitshift only for tasks that don't pass data (Explicit dependency)
    sum_output >> third_task()

# Register the DAG
first_dag()
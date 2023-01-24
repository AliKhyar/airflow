from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'me',
    'start_date': datetime(2022, 1, 1)
}

dag = DAG(
    'simple_dag', 
    default_args=default_args, 
    schedule_interval=timedelta(days=1)
)

task = BashOperator(
    task_id='run_bash_command',
    bash_command='echo "Hello, World!"',
    dag=dag
)



from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Michael Hoffman',
    'depends_on_past': False,
    'email': ['mhoffman@nvisia.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'catchup': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'CreateFile',
    default_args=default_args,
    start_date=datetime(2023, 1, 1, 0, 0),
    schedule_interval=timedelta(minutes=500))


task1 = BashOperator(
    task_id='prove_things_work',
    bash_command='echo "hello, world!" > /root/create-this-file.txt',
    dag=dag)

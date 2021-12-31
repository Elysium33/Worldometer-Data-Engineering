from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['yourmail@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'CovidDag',
    start_date=datetime(2022, 1, 1),
    default_args=default_args,
    description='Covid data pipeline',
    schedule_interval="@daily",
    catchup=False
) as dag:
    t1 = BashOperator(
        task_id='data_to_GCS',
        bash_command='python3 path/DataToGCS.py'
    )

    t2 = BashOperator(
        task_id='Sparkjob',
        bash_command='python3 path/sparkjob.py'
    )

    t1 >> t2

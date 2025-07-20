from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('marketing_dbt_pipeline', start_date=datetime(2023, 1, 1),
         schedule_interval='@daily',
         catchup=False,
        tags=['marketing', 'dbt','github','ten']) as dag:

    dbt_seed = BashOperator(
        task_id='dbt_seed',
        bash_command='dbt seed --project-dir /home/hans/dbt/dbt_proj --profiles-dir /home/hans/.dbt'

    )

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='dbt seed --project-dir /home/hans/dbt/dbt_proj --profiles-dir /home/hans/.dbt'

    )

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='dbt seed --project-dir /home/hans/dbt/dbt_proj --profiles-dir /home/hans/.dbt'

    )

    dbt_seed >> dbt_run >> dbt_test

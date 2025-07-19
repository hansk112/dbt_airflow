from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='dbt_simple_pipeline',
    default_args=default_args,
    dag_display_name="Test DAG with Display Name",
    schedule_interval='@daily',
    catchup=False,
    tags=['dbt', 'learning'],
) as dag:
    
    dbt_snapshot = BashOperator(
    task_id='dbt_snapshot',
    bash_command='cd ~/dbt/dbt_proj && dbt snapshot --profiles-dir ~/dbt'
    )

    dbt_seed = BashOperator(
        task_id='dbt_seed',
        bash_command='cd ~/dbt/dbt_proj && dbt seed --profiles-dir ~/dbt'
    )

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='cd ~/dbt/dbt_proj && dbt run --profiles-dir ~/dbt'
    )

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='cd ~/dbt/dbt_proj && dbt test --profiles-dir ~/dbt'
    )


    dbt_seed >> dbt_snapshot >> dbt_run >> dbt_test

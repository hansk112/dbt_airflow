# start the python virtual machine

source airflow_dbt_env/bin/activate

# start the docker container

docker start b27134b53baf


# access to http://localhost:8080/home

# initialize airflow
airflow db init

# start airflow webserver
airflow webserver

# "open a new terminal" and start airflow scheduler

airflow scheduler

# "use this command to find where airflow dags are saved" grep dags_folder ~/airflow/airflow.cfg 
My dags are saved in this folder dags_folder = /home/hans/airflow/dags

# "run command" dbt debug this will check whether dbt connection is working





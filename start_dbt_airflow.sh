#!/bin/bash

echo "🐍 Activating Python virtual environment..."
source ~/dbt/airflow_dbt_env/bin/activate

echo "🐘 Starting PostgreSQL container..."
docker start postgres-db

echo "🌬️ Starting Airflow webserver..."
airflow db init  # only needed once, remove if already initialized
airflow webserver -p 8080 &

echo "📅 Starting Airflow scheduler..."
airflow scheduler &

echo "📝 Launching Visual Studio Code..."
code ~/dbt

echo "✅ Environment ready. You can now run dbt commands like 'dbt run' or 'dbt test'."


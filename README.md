markdown
# 📈 Marketing Campaign Data Pipeline with dbt & Airflow

This project demonstrates a simple data pipeline using **dbt** and **Apache Airflow**, orchestrated in a Dockerized environment. It transforms raw marketing campaign data and schedules automated workflows—ideal for showcasing foundational data engineering skills.

---

## 🗂️ Project Structure

dbt-airflow-marketing-pipeline/ ├── dbt_proj/ # dbt models and seeds │ ├── models/ │ ├── seeds/ │ └── dbt_project.yml ├── dags/ # Airflow DAGs │ └── marketing_dbt_dag.py ├── profiles.yml # dbt profile with Postgres config ├── start_dbt_airflow.sh # Optional startup script ├── Dockerfile ├── docker-compose.yml └── README.md


---

## 🚀 Pipeline Overview

1. **Seed raw campaign data** into Postgres
2. **Run dbt model** to aggregate metrics
3. **Schedule tasks using Airflow DAG**
4. **All wrapped inside a Docker-based environment**

---

## 🧬 Data Used

### `raw_campaign_data.csv`
Simulated campaign performance:
```csv
campaign_id,date,clicks,impressions,cost
c1,2023-01-01,120,1000,45.50
c2,2023-01-01,85,900,38.75
c1,2023-01-02,130,1100,48.20
📦 Technologies
dbt v1.10.3 (Postgres adapter)

Apache Airflow

Docker & Docker Compose

PostgreSQL

Python (virtualenv optional)

⚙️ How to Run
1. Update profiles.yml
Ensure your Postgres credentials are correct:

yaml
default:
  target: dev
  outputs:
    dev:
      type: postgres
      host: localhost
      port: 5432
      user: your_user
      password: your_password
      dbname: your_db
      schema: dbt_demo
      threads: 1
2. Seed and Run dbt Models
bash
dbt seed --project-dir dbt_proj --profiles-dir .
dbt run --project-dir dbt_proj --profiles-dir .
3. Start Airflow Scheduler and Webserver
bash
airflow scheduler &
airflow webserver &
Airflow UI will be available at: http://localhost:8080

4. Trigger the DAG
DAG ID: marketing_dbt_pipeline

Tasks:

dbt_seed

dbt_run

📊 dbt Models
campaign_metrics.sql
Aggregates campaign-level KPIs:

sql
select
  campaign_id,
  date,
  sum(clicks) as total_clicks,
  sum(impressions) as total_impressions,
  round(sum(cost), 2) as total_cost
from {{ ref('raw_campaign_data') }}
group by campaign_id, date
🌱 Future Extensions
Add dbt test steps in Airflow DAG

Include downstream analytics or dashboard triggers

Extend with new datasets (e.g. ROAS, geo breakdown)
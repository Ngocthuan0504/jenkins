from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.operators.mysql_operator import MySfroqlOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'mysql_to_ec2',
    default_args = default_args,
    description = 'A simple DAG test BI transfer data from MySQL to EC2',
    schedule_interval=timedelta(days=1),
)

t1 = MySqlOperator(
    task_id = 'mysql_to_ec2_task',
    sql = 'SELECT * FROM tch_order',
    mysql_conn_id = 'my_mysql_conn',
    dag=dag,
)










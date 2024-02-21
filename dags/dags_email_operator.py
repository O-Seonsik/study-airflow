from airflow import DAG
import pendulum
import datetime
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2024, 2, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    send_email_task = EmailOperator(
        task_id='send_email_task',
        to='dhtjstlr777@gmail.com',
        subject='Airflow send_email_task 성공',
        html_content='Airflow DAG 의 작업이 수행 완료 되었습니다.',
    )

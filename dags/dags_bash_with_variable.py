from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator
from airflow.models import Variable

with DAG(
    dag_id='dags_bash_with_variable',
    schedule='30 9 * * *',
    start_date=pendulum.datetime(2024, 2, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    # bash_val_1 같이 구성하게 되면 scheduler 동작시 Variable 을 가져오기 위해 metaDB 에 access 하게 되어 과부화가 올 수 있음
    var_value = Variable.get('sample_key')

    bash_val_1 = BashOperator(
        task_id='bash_var_1',
        bash_command=f"echo variable: {var_value}"
    )

    bash_var_2 = BashOperator(
        task_id='bash_var_2',
        bash_command="echo variable: {{ var.value.sample_key }}"
    )

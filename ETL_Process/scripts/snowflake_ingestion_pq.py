import json
import boto3
from botocore.exceptions import ClientError
import snowflake.connector
# snowflake-connector-python - Package need to be install
def lambda_handler(event, context):
    
    # Read the snowflake and aws credentials
    aws_secret_name = ''
    snowflake_secret_name = ''
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name='us-east-1'
    )

    try:
        get_aws_secret_value_response = client.get_secret_value(
            SecretId=aws_secret_name
        )
        get_snowflake_secret_value_response = client.get_secret_value(
            SecretId=snowflake_secret_name
        )
    except ClientError as e:
        raise e

    aws_secret = json.loads(get_aws_secret_value_response['SecretString'])
    snowflake_secret = json.loads(get_snowflake_secret_value_response['SecretString'])

    con = snowflake.connector.connect(
        user=snowflake_secret['user'],
        password=snowflake_secret['password'],
        account=snowflake_secret['account'],
        warehouse='COMPUTE_WH',
        database='RETAIL_PROJECT',
        schema='DEV',
        role='ACCOUNTADMIN'
    )

    cur = con.cursor()
    
    cur.execute(
        f"""
        CREATE STAGE IF NOT EXISTS retail_s3_output_stage
        URL='s3://retail-data-142083400213/output/parquet/'
        CREDENTIALS=(AWS_KEY_ID='{aws_secret["AWS_KEY_ID"]}' AWS_SECRET_KEY='{aws_secret["AWS_SECRET_KEY"]}')
        FILE_FORMAT=(TYPE=PARQUET);
        """
    )

    cur.execute(
        """
        CREATE FILE FORMAT IF NOT EXISTS parquet_format
        TYPE = 'PARQUET';
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS SALES
        USING TEMPLATE (
            SELECT ARRAY_AGG(OBJECT_CONSTRUCT(*))
            FROM TABLE(
                INFER_SCHEMA(
                    LOCATION=>'@retail_s3_output_stage',
                    FILE_FORMAT=>'parquet_format'
                )
            )
        );
        """
    )

    cur.execute(
        """
        COPY INTO SALES
        FROM @retail_s3_output_stage
        FILE_FORMAT = (TYPE = PARQUET)
        MATCH_BY_COLUMN_NAME = CASE_SENSITIVE;
        """
    )
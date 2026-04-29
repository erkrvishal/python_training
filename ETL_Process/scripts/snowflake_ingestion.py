import json
import boto3
from botocore.exceptions import ClientError
import snowflake.connector
# snowflake-connector-python - Package need to be install
def lambda_handler(event, context):
    
    # Read the snowflake and aws credentials
    aws_secret_name = '' # Place the aws secret name
    snowflake_secret_name = '' # Place the snowflake secret name
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
        CREATE OR REPLACE STAGE retail_s3_stage
        URL='s3://retail-data-142083400213/'
        CREDENTIALS=(AWS_KEY_ID='{aws_secret["AWS_KEY_ID"]}' AWS_SECRET_KEY='{aws_secret["AWS_SECRET_KEY"]}')
        FILE_FORMAT=(TYPE=CSV FIELD_DELIMITER=',' SKIP_HEADER=1, FIELD_OPTIONALLY_ENCLOSED_BY='"')
        """
    )

    cur.execute(
        """
        CREATE OR REPLACE FILE FORMAT csv_format
        TYPE = 'CSV'
        FIELD_DELIMITER=',' 
        PARSE_HEADER=TRUE
        """
    )

    cur.execute(
        """
        CREATE OR REPLACE TABLE CUSTOMERS
        USING TEMPLATE (
            SELECT ARRAY_AGG(OBJECT_CONSTRUCT(*))
            FROM TABLE(
                INFER_SCHEMA(
                    LOCATION=>'@retail_s3_stage',
                    FILES => ('dimension/customer.csv'),
                    FILE_FORMAT=>'csv_format'
                )
            )
        );
        """
    )

    cur.execute(
        """
        COPY INTO CUSTOMERS
        FROM @retail_s3_stage/dimension/customer.csv
        FILE_FORMAT = (TYPE = CSV FIELD_DELIMITER=',' SKIP_HEADER=1)
        """
    )
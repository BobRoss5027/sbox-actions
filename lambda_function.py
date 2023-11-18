import os
import requests
import json
import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    secret_name = "eoin/test_jist"
    region_name = "eu-west-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']
    secret_dict=json.loads(secret)
    
    headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {secret_dict["GITHUB_TOKEN"]}',
    'X-GitHub-Api-Version': '2022-11-28',
    'Content-Type': 'application/x-www-form-urlencoded',
    }
    
    acc_input=json.loads(event['input'])
    # print(acc_name['first_name'])

    data = '{"event_type":"Remove '+acc_input['username']+' Perms","client_payload":{"acc_name":"'+acc_input['username']+'", "acc_role":"'+acc_input['role']+'","test_success":false,"message":"Test message payload","aws_acc":1234567890,"sec_test":"This is a Secret"}}'

    print(data)

    response = requests.post('https://api.github.com/repos/BobRoss5027/sbox-actions/dispatches', headers=headers, data=data)

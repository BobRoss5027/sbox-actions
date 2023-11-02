import os
import requests
import json

def lambda_handler(event, context):
    headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {os.environ["GITHUB_TOKEN"]}',
    'X-GitHub-Api-Version': '2022-11-28',
    'Content-Type': 'application/x-www-form-urlencoded',
    }
    
    acc_name=json.loads(event['input'])
    print(acc_name['first_name'])

    data = '{"event_type":"'+acc_name['first_name']+'","client_payload":{"acc_name":"'+acc_name['first_name']+'","test_success":false,"message":"Test message payload","aws_acc":1234567890,"sec_test":"This is a Secret"}}'

    print(data)

    response = requests.post('https://api.github.com/repos/BobRoss5027/sbox-actions/dispatches', headers=headers, data=data)

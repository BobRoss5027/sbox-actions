import os
import requests

def lambda_handler(event, context):
    headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {os.environ["GITHUB_TOKEN"]}',
    'X-GitHub-Api-Version': '2022-11-28',
    'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = '{"event_type":"test_workflow_lambda","client_payload":{"test_success":false,"message":"Test message payload","aws_acc":1234567890,"sec_test":"This is a Secret"}}'

    response = requests.post('https://api.github.com/repos/BobRoss5027/sbox-actions/dispatches', headers=headers, data=data)

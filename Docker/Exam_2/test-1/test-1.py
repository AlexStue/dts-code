import os
import requests
import json

# Load dataset file
with open('ds-users.json', 'r') as file:
    users = json.load(file)

api_address = 'host.docker.internal'
api_port = 8000
log_output = []

for user in users:
    name = user["name"]
    password = user["password"]
    r = requests.get(f"http://{api_address}:{api_port}/permissions?username={name}&password={password}")

    status_code = r.status_code
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'

    output = f'''
    ============================
    | Authentication test: request done at "/permissions"
    | username="{name}" | password="{password}"
    | expected result = 200 | actual restult = {status_code}
    | ==>  {test_status}
    '''

    print(output)
    log_output.append(output)

with open('api_test-1.log', 'a') as file:
    file.write('\n'.join(log_output))

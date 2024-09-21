import os
import requests
import json

# Load dataset file
with open('../dataset/ds-users.json', 'r') as file:
    users = json.load(file)

api_address = 'localhost'
api_port = 8000
log_output = []

for user in users:
    name = user["name"]
    password = user["password"]
    r = requests.get(f"http://{api_address}:{api_port}/permissions?username={name}&password={password}")

    data = r.json()
    permissions = data.get('permissions', [])
    permissions_str = ', '.join(permissions) if permissions else "none"

    status_code = r.status_code
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'

    output = f'''
    ============================
    | Authorization test: request done at "/permissions"
    | User "{name}" has authorizations for model: {permissions_str}
    '''

    print(output)
    log_output.append(output)

if os.environ.get('LOG') == '1':
    with open('api_test-2.log', 'a') as file:
        file.write('\n'.join(log_output))
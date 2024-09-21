import os
import requests
api_address = ''
api_port = 8000

USERNAME_1 = os.getenv('USERNAME_1')
PASSWORD_1 = os.getenv('PASSWORD_1')

url='http://webserver:8000/permissions'
params= {
    'username': USERNAME_1,
    'password': PASSWORD_1
}
r = requests.get(url, params=params)

output = '''
============================
    Authentication test
============================
request done at "/permissions"
| username="{USERNAME_1}"
| password="{PASSWORD_1}"
expected result = 200
actual restult = {status_code}
==>  {test_status}
'''

status_code = r.status_code
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(USERNAME_1=USERNAME_1, PASSWORD_1=PASSWORD_1, status_code=status_code, test_status=test_status))

if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output)

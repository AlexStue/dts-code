import os
import requests
api_address = ''
api_port = 8000

USERNAME_1 = os.getenv('USERNAME_1')
PASSWORD_1 = os.getenv('PASSWORD_1')
SENTENCE_1 = os.getenv('SENTENCE_1')
SENTENCE_2 = os.getenv('SENTENCE_2')

url1='http://webserver:8000/v1/sentiment'
url2='http://webserver:8000/v2/sentiment'

params1= {
    'username': USERNAME_1,
    'password': PASSWORD_1,
    'sentence': SENTENCE_1
}

params2= {
    'username': USERNAME_1,
    'password': PASSWORD_1,
    'sentence': SENTENCE_2
}

r1 = requests.get(url1, params=params1)
r2 = requests.get(url1, params=params2)
r3 = requests.get(url2, params=params1)
r4 = requests.get(url2, params=params2)

output = '''
============================
    Model test
============================
| username="{USERNAME_1}"
| password="{PASSWORD_1}"
============================
request done at "/v1/sentiment"
| sentences="life is beautiful"
expected score > 0
actual score = {score1}
==>  {test_status1}
============================
request done at "/v1/sentiment"
| sentences="that sucks"
expected score < 0
actual score = {score2}
==>  {test_status2}
============================
request done at "/v2/sentiment"
| sentences="life is beautiful"
expected score > 0
actual score = {score3}
==>  {test_status3}
============================
request done at "/v2/sentiment"
| sentences="that sucks"
expected score < 0
actual score = {score4}
==>  {test_status4}
'''

if r1.status_code == 200:
    data1 = r1.json()
    score1 = data1.get('score')
    if score1 > 0:
        test_status1 = 'SUCCESS'
    else:
        test_status1 = 'FAILURE'
else:
    score1 = 'UNKNOWN'
    test_status1 = 'FAILURE'

if r2.status_code == 200:
    data2 = r2.json()
    score2 = data2.get('score')
    if score2 < 0:
        test_status2 = 'SUCCESS'
    else:
        test_status2 = 'FAILURE'
else:
    score2 = 'UNKNOWN'
    test_status2 = 'FAILURE'

if r3.status_code == 200:
    data3 = r3.json()
    score3 = data3.get('score')
    if score3 > 0:
        test_status3 = 'SUCCESS'
    else:
        test_status3 = 'FAILURE'
else:
    score3 = 'UNKNOWN'
    test_status3 = 'FAILURE'

if r4.status_code == 200:
    data4 = r4.json()
    score4 = data4.get('score')
    if score4 < 0:
        test_status4 = 'SUCCESS'
    else:
        test_status4 = 'FAILURE'
else:
    score4 = 'UNKNOWN'
    test_status4 = 'FAILURE'

print(output.format(USERNAME_1=USERNAME_1, PASSWORD_1=PASSWORD_1, score1=score1, test_status1=test_status1, score2=score2, test_status2=test_status2, score3=score3, test_status3=test_status3, score4=score4, test_status4=test_status4))
# printing in a file
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output)

import os
import requests
import json

# Load dataset file
with open('../dataset/ds-users.json', 'r') as file1:
    users = json.load(file1)

# Load dataset file
with open('../dataset/ds-sentences.json', 'r') as file2:
    sentences = json.load(file2)

api_address = 'localhost'
api_port = 8000
log_output = []

# Start logging
header = "============================\nModel Test\n"
log_output.append(header)

for user in users:
    name = user["name"]
    password = user["password"]
    user_separator = "==============\n"
    log_output.append(user_separator)
    log_output.append(f"For User: {name}\n")
    
    for model in range(1, 3):  # model 1 & 2
        model_output = f"Model: v{model}\n"
        log_output.append(model_output)

        for sentence in sentences:
            r = requests.get(f"http://{api_address}:{api_port}/v{model}/sentiment",
                             params={"username": name, "password": password, "sentence": sentence})
            data = r.json()
            score = data.get('score')
            sentence_output = f'Sentence "{sentence}" has score of: {score}\n'
            log_output.append(sentence_output)

            if score is not None:
                if model == 1 and score > 0:
                    status_output = " ==> Test status: SUCCESS \n"
                elif model == 2 and score < 0:
                    status_output = " ==> Test status: SUCCESS \n"
                else:
                    status_output = " ==> Test status: FAILURE \n"
            else:
                status_output = " ==> Test status: SCORE NOT AVAILABLE \n"
            
            log_output.append(status_output)

if os.environ.get('LOG') == '1':
    with open('api_test-3.log', 'a') as file:
        file.write(''.join(log_output))

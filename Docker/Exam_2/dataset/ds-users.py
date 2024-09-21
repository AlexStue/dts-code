import json

users_password = [
    {"name": "alice", "password": "wonderland"},
    {"name": "bob", "password": "builder"},
    {"name": "clementine", "password": "mandarine"}
]

# Save it as a JSON file
with open('../test-2/ds-users.json', 'w') as file:
    json.dump(users_password, file)

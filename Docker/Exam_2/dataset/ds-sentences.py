import json

sentences = [
    {"sentence": "life is beautiful"},
    {"sentence": "that sucks"},
]

# Save it as a JSON file
with open('ds-sentences.json', 'w') as file:
    json.dump(sentences, file)



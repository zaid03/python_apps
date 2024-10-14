import json
import os

data = {
    "nom" : "jean",
    "age" : 30,
    "ville" : "paris",
    "profession" : "ingénieur",
    "languages" : ["python", "javascript", "c++"]
}

with open("data.json", "w") as fichier:
    json.dump(data, fichier)
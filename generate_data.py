# generate_data.py
import os
import json
from sklearn.datasets import load_iris

os.makedirs("data", exist_ok=True)

# On charge Iris et on le sauvegarde en JSON comme demandé dans le lab
iris = load_iris(as_frame=True)
df = iris.frame
df.to_json("data/iris.json", orient="records")

print("Fichier data/iris.json créé !")
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import sys
import os

if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage: python train.py <input> <output>\n")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

print(f"🚂 Entraînement sur {input_file}...")

# 1. Lecture des données propres
df = pd.read_csv(input_file)

# 2. Séparation Features (X) / Target (y)
# Dans le dataset Iris, la cible s'appelle souvent "target" ou "species"
target_col = "target" 
X = df.drop(target_col, axis=1)
y = df[target_col]

# 3. Entraînement
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# 4. Sauvegarde du modèle
with open(output_file, "wb") as f:
    pickle.dump(model, f)

print(f"✅ Modèle V2 sauvegardé dans {output_file}")
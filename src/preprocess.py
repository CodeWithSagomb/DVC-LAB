import pandas as pd
import sys
import os

# DVC va passer les noms de fichiers en arguments (sys.argv)
# sys.argv[1] = fichier d'entrée (data/iris.json)
# sys.argv[2] = fichier de sortie (data/iris_clean.csv)

if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage: python preprocess.py <input> <output>\n")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

print(f"🧼 Nettoyage de {input_file}...")

# 1. Lecture
df = pd.read_json(input_file)

# 2. Transformation (Exemple simple du lab: multiplier une colonne par 2)
# On vérifie si la colonne existe pour éviter les erreurs
col_name = 'petal width (cm)'
if col_name in df.columns:
    df[col_name] = df[col_name] * 2

# 3. Sauvegarde
df.to_csv(output_file, index=False)
print(f"✅ Données nettoyées sauvegardées dans {output_file}")
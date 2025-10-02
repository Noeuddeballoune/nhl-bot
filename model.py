# model.py
import lightgbm as lgb
import pandas as pd
from data import df

# ---------------------------
# Préparer les données
# ---------------------------
# On utilise 'prev_points' et 'age' comme features simples
# Pour les équipes, age = 0
X = df[['prev_points', 'age']].fillna(0)
y = df['prev_points']  # pour l'exemple, on prédit la même valeur

# Créer et entraîner un modèle LightGBM
model = lgb.LGBMRegressor()
model.fit(X, y)

# ---------------------------
# Fonctions de prédiction
# ---------------------------

def predict_points(name):
    """
    Prédit le nombre de points pour un joueur, gardien ou équipe.
    Retourne None si le nom n'existe pas dans le dataset.
    """
    row = df[df['name'].str.lower() == name.lower()]
    if row.empty:
        return None
    features = row[['prev_points', 'age']].values
    prediction = model.predict(features)[0]
    return round(prediction)

def best_choice(names):
    """
    Prend une liste de noms et retourne celui avec le plus de points prédits.
    """
    best_name = None
    best_points = -1
    for name in names:
        points = predict_points(name)
        if points is not None and points > best_points:
            best_points = points
            best_name = name
    return best_name, best_points

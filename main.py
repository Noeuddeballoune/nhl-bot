from fastapi import FastAPI, Request
from model import predict_points, best_choice
import uvicorn

app = FastAPI()

@app.post("/")
async def poe_handler(req: Request):
    # Lire la requête envoyée par Poe
    data = await req.json()
    user_query = data.get("query", "")

    # -----------------------------
    # Extraire les noms à comparer
    # -----------------------------
    # On suppose que l'utilisateur écrit les noms séparés par des virgules
    # Exemple : "Connor McDavid, Sidney Crosby, Tampa Bay Lightning"
    user_query_clean = user_query.replace("?", "").strip()
    names = [n.strip() for n in user_query_clean.split(",")]

    # -----------------------------
    # Logique de prédiction
    # -----------------------------
    if not names or names == [""]:
        prediction = "Je n’ai pas trouvé de joueur, gardien ou équipe dans votre message."
    elif len(names) == 1:
        points = predict_points(names[0])
        if points is None:
            prediction = f"Aucune donnée disponible pour {names[0]}."
        else:
            prediction = f"{names[0]} devrait produire environ {points} points la saison prochaine."
    else:
        best_name, best_points = best_choice(names)
        if best_name is None:
            prediction = "Aucune donnée disponible pour les choix donnés."
        else:
            prediction = f"Parmi les choix donnés, {best_name} est celui avec le plus de points prédits : {best_points} points."

    # -----------------------------
    # Réponse au format attendu par Poe
    # -----------------------------
    return {
        "content": [
            {
                "type": "text",
                "text": prediction
            }
        ]
    }

# -----------------------------
# Lancer le serveur (Railway / local)
# -----------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

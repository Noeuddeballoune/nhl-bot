from fastapi import FastAPI, Request
from model import predict_points, best_choice
import uvicorn

app = FastAPI()

@app.post("/")
async def poe_handler(req: Request):
    try:
        data = await req.json()
    except:
        return {"content": [{"type": "text", "text": "Erreur : impossible de lire la requête."}]}

    user_query = data.get("query", "")
    if not user_query:
        return {"content": [{"type": "text", "text": "Aucun texte reçu."}]}

    # Extraire les noms séparés par des virgules
    names = [n.strip() for n in user_query.replace("?", "").split(",") if n.strip() != ""]

    if not names:
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

    return {"content": [{"type": "text", "text": prediction}]}

# Pour tester localement
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI, Request
from model import predict_points, best_player
import uvicorn

app = FastAPI()

@app.post("/")
async def poe_handler(req: Request):
    data = await req.json()
    user_query = data.get("query", "")

    # --- Détecter si l'utilisateur donne plusieurs joueurs ---
    # Exemple de message attendu : "Qui aura le plus de points entre McDavid, Crosby et Matthews ?"
    player_names = []
    for name in ["Connor McDavid", "Sidney Crosby", "Auston Matthews", "Leon Draisaitl", "Nathan MacKinnon"]:
        if name.lower() in user_query.lower():
            player_names.append(name)

    if len(player_names) == 0:
        prediction = "Je n’ai pas trouvé de joueur connu dans votre message."
    elif len(player_names) == 1:
        points = predict_points(player_names[0])
        prediction = f"{player_names[0]} devrait produire environ {points} points la saison prochaine."
    else:
        best, points = best_player(player_names)
        prediction = f"Parmi les joueurs donnés, {best} est celui avec le plus de points prédits : {points} points."

    # Réponse au format Poe
    return {
        "content": [
            {
                "type": "text",
                "text": prediction
            }
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


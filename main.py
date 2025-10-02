from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/")
async def poe_handler(req: Request):
    data = await req.json()
    user_query = data.get("query", "")

    # -------------------------------
    # LOGIQUE DU BOT
    # (pour l’instant, simple exemple)
    # -------------------------------
    if "McDavid" in user_query or "Connor McDavid" in user_query:
        prediction = "Connor McDavid devrait produire environ 120 à 130 points en 2025-26."
    elif "Crosby" in user_query or "Sidney Crosby" in user_query:
        prediction = "Sidney Crosby pourrait produire autour de 80 à 90 points en 2025-26."
    else:
        prediction = f"Je n’ai pas encore de projection précise pour {user_query}, mais je peux expliquer la méthode."

    # -------------------------------
    # RÉPONSE AU FORMAT ATTENDU PAR POE
    # -------------------------------
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

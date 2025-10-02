# model.py
player_data = {
    "Connor McDavid": {"prev_points": 120, "age": 26},
    "Sidney Crosby": {"prev_points": 85, "age": 37},
    "Auston Matthews": {"prev_points": 100, "age": 26},
    "Leon Draisaitl": {"prev_points": 115, "age": 27},
    "Nathan MacKinnon": {"prev_points": 95, "age": 27},
}

def predict_points(player_name):
    player = player_data.get(player_name)
    if not player:
        return None

    base = player["prev_points"]
    age = player["age"]
    if age < 27:
        factor = 1.05
    elif age > 35:
        factor = 0.90
    else:
        factor = 1.0

    prediction = round(base * factor)
    return prediction

def best_player(player_list):
    best = None
    best_points = -1
    for player in player_list:
        points = predict_points(player)
        if points is not None and points > best_points:
            best_points = points
            best = player
    if best is None:
        return None, None
    return best, best_points

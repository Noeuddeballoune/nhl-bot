# model.py
import random

# Liste ultra-légère pour test
players = ["Connor McDavid", "Sidney Crosby", "Auston Matthews"]

def predict_points(name):
    return random.randint(50, 130)  # points fictifs

def best_choice(names):
    best_name = None
    best_points = -1
    for name in names:
        points = predict_points(name)
        if points > best_points:
            best_points = points
            best_name = name
    return best_name, best_points

# data.py
import pandas as pd

# Liste de joueurs, gardiens et équipes avec statistiques fictives
data = [
    # Joueurs
    {"name": "Connor McDavid", "prev_points": 120, "age": 26, "position": "C"},
    {"name": "Sidney Crosby", "prev_points": 85, "age": 37, "position": "C"},
    {"name": "Auston Matthews", "prev_points": 100, "age": 26, "position": "C"},
    {"name": "Leon Draisaitl", "prev_points": 115, "age": 27, "position": "C"},
    {"name": "Nathan MacKinnon", "prev_points": 95, "age": 27, "position": "C"},
    {"name": "Alex Ovechkin", "prev_points": 90, "age": 37, "position": "LW"},
    {"name": "David Pastrnak", "prev_points": 88, "age": 26, "position": "RW"},
    {"name": "Kirill Kaprizov", "prev_points": 85, "age": 24, "position": "LW"},
    {"name": "Patrick Kane", "prev_points": 80, "age": 34, "position": "RW"},
    {"name": "Jack Eichel", "prev_points": 75, "age": 25, "position": "C"},

    # Gardiens
    {"name": "Carey Price", "prev_points": 60, "age": 36, "position": "G"},
    {"name": "Andrei Vasilevskiy", "prev_points": 70, "age": 27, "position": "G"},
    {"name": "Igor Shesterkin", "prev_points": 65, "age": 26, "position": "G"},
    {"name": "Connor Hellebuyck", "prev_points": 68, "age": 28, "position": "G"},
    {"name": "Juuse Saros", "prev_points": 62, "age": 27, "position": "G"},

    # Équipes
    {"name": "Tampa Bay Lightning", "prev_points": 105, "age": 0, "position": "Team"},
    {"name": "Colorado Avalanche", "prev_points": 110, "age": 0, "position": "Team"},
    {"name": "Toronto Maple Leafs", "prev_points": 100, "age": 0, "position": "Team"},
    {"name": "Boston Bruins", "prev_points": 102, "age": 0, "position": "Team"},
    {"name": "Florida Panthers", "prev_points": 98, "age": 0, "position": "Team"},
    {"name": "Carolina Hurricanes", "prev_points": 97, "age": 0, "position": "Team"},
    {"name": "Edmonton Oilers", "prev_points": 99, "age": 0, "position": "Team"},
    {"name": "New York Rangers", "prev_points": 96, "age": 0, "position": "Team"},
    {"name": "Vegas Golden Knights", "prev_points": 101, "age": 0, "position": "Team"},
    {"name": "St. Louis Blues", "prev_points": 94, "age": 0, "position": "Team"},
]

# Convertir en DataFrame pour faciliter l'utilisation
df = pd.DataFrame(data)

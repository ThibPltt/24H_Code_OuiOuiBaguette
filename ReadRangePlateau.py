import json

# Chemin du fichier JSON
JSON_PATH = "Datas/rangePlateau"

def charger_plateau():
    """Charge les données du plateau depuis le fichier JSON."""
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data  # Retourne la liste des cases
    except FileNotFoundError:
        print(f"Erreur : Fichier {JSON_PATH} non trouvé.")
        return []
    except json.JSONDecodeError:
        print("Erreur : Le fichier JSON est mal formaté.")
        return []

def get_case_par_coord(x, y):
    """Retourne les informations d'une case en fonction de ses coordonnées."""
    plateau = charger_plateau()
    
    for case in plateau:
        if case["coord_x"] == x and case["coord_y"] == y:
            return case["ressources"]  # Retourne directement la case trouvée

    return None  # Retourne None si aucune case ne correspond

# Exemple d'utilisation
if __name__ == "__main__":
    x, y = 0, 0  # Coordonnées de test
    case = get_case_par_coord(x, y)
    
    if case:
        print(f"Case trouvée aux coordonnées ({x}, {y}):")
        print(json.dumps(case, indent=4, ensure_ascii=False))  # Affichage formaté
    else:
        print(f"Aucune case trouvée aux coordonnées ({x}, {y}).")

import json

# Chemin du fichier JSON
JSON_PATH = "Datas/rangePlateau.json"

def charger_ressources():
    """Charge les données des ressources à partir du fichier JSON."""
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data  # Retourne le JSON sous forme de dictionnaire
    except FileNotFoundError:
        print(f"Erreur : Fichier {JSON_PATH} non trouvé.")
        return None
    except json.JSONDecodeError:
        print("Erreur : Le fichier JSON est mal formaté.")
        return None

def extraire_donnees_ressources(data):
    """Extrait les informations des ressources (quantité, nom, type) pour chaque case."""
    ressources_extraites = []
    
    for case in data:
        coord_x = case.get("coord_x")
        coord_y = case.get("coord_y")
        ressources = case.get("ressources", [])

        for ressource in ressources:
            quantite = ressource.get("quantite", 0)
            ressource_info = ressource.get("ressource", {})

            nom = ressource_info.get("nom", "Inconnu")
            type_ressource = ressource_info.get("type", "Inconnu")

            ressources_extraites.append({
                "coord_x": coord_x,
                "coord_y": coord_y,
                "nom": nom,
                "quantite": quantite,
                "type": type_ressource
            })
    
    return ressources_extraites

# Charger l'image du villageois
villager_img = pygame.image.load("assets2D/villagers/villager.png").convert_alpha()

# Redimensionner l'image du villageois pour qu'elle couvre 3x3 cases (3x CELL_SIZE)
villager_scaled = pygame.transform.scale(villager_img, (3 * plateau.CELL_SIZE, 3 * plateau.CELL_SIZE))

# Charger les villageois depuis le fichier JSON
villagers_data = load_villagers_data('Datas/VillageoisData')
villagers = get_villagers_from_data(villagers_data)


# Fonction pour dessiner tous les villageois
def draw_ressource():
    """Fonction pour dessiner les villageois sur le plateau."""
    for ressource in ressources:
        # Calculer la position en pixels à partir des coordonnées en cases
        position_x, position_y = villager['position']
        # Dessiner le villageois à sa position
        plateau.screen.blit(villager_scaled, (position_x * plateau.CELL_SIZE, position_y * plateau.CELL_SIZE))


# Test de chargement et d'extraction
if __name__ == "__main__":
    data = charger_ressources()
    if data:
        ressources = extraire_donnees_ressources(data)
        for r in ressources:
            print(r)  # Affiche chaque ressource sous forme de dictionnaire

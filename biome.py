import pygame
import plateau  # Importation du fichier plateau.py
import json

# Définition des types de biomes
PLAIN = "plaine"
DESERT = "desert"
LAC = "lac"

# Charger les images des villageois en fonction du biome
biomes_images = {
    PLAIN: pygame.image.load("assets2D/tiles/plaine.png").convert_alpha(),
    DESERT: pygame.image.load("assets2D/tiles/desert.png").convert_alpha(),
    LAC: pygame.image.load("assets2D/tiles/lac.png").convert_alpha(),
}

# Redimensionner les images pour qu'elles fassent 1x1 case
for key in biomes_images:
    biomes_images[key] = pygame.transform.scale(biomes_images[key], (plateau.CELL_SIZE, plateau.CELL_SIZE))

# Charger les données JSON depuis le fichier
def load__data(filepath):
    """Charge les données des villageois à partir du fichier JSON."""
    try:
        with open(filepath, 'r', encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Erreur : biomesLe fichier {filepath} n'a pas été trouvé.")
        return []
    except json.JSONDecodeError:
        print("Erreur : Le fichier JSON est mal formaté.")
        return []

def get_biomes_from_data(data):
    """Retourne la liste des villageois avec leurs informations."""
    biomes = []
    for biomes_data in data:
        biomes.append({
            'id': biomes_data['idVillageois'],
            'name': biomes_data['nom'],
            'position': (biomes_data['positionX'], biomes_data['positionY'])
        })
    return biomes

# Charger les villageois depuis le fichier JSON
biomes_data = load_biomes_data('map.json')
biomes = get_biomes_from_data(biomes_data)

# Fonction pour obtenir le biome d'un villageois selon sa position
def get_biome_for_villager(position):
    """Récupère le biome à la position du villageois."""
    x, y = position
    if 0 <= y < len(plateau.carte) and 0 <= x < len(plateau.carte[0]):
        return plateau.carte[y][x]  # Accès à la carte selon x, y
    return PLAIN  # Par défaut, si hors limite

# Fonction pour dessiner les villageois selon leur biome
def draw_villagers():
    """Dessine les villageois sur le plateau en fonction du biome."""
    for villager in villagers:
        position_x, position_y = villager['position']
        biome = get_biome_for_villager((position_x, position_y))  # Récupérer le biome

        # Sélectionner l'image en fonction du biome
        match biome:
            case PLAIN:
                img = biomes_images[PLAIN]
            case DESERT:
                img = biomes_images[DESERT]
            case LAC:
                img = biomes_images[LAC]
            case _:
                img = biomes_images[PLAIN]  # Par défaut

        # Dessiner le villageois à sa position
        plateau.screen.blit(img, (position_x * plateau.CELL_SIZE, position_y * plateau.CELL_SIZE))


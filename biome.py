import pygame
import plateau  # Importation du fichier plateau.py
import json

# Définition des types de biomes
PLAIN = "plaine"
DESERT = "desert"
LAC = "lac"

# Charger les images des biomes
biomes_images = {
    PLAIN: pygame.image.load("assets2D/tiles/plaine.png").convert_alpha(),
    DESERT: pygame.image.load("assets2D/tiles/desert.png").convert_alpha(),
    LAC: pygame.image.load("assets2D/tiles/lac.png").convert_alpha(),
}

# Redimensionner les images pour qu'elles fassent 1x1 case
for key in biomes_images:
    biomes_images[key] = pygame.transform.scale(biomes_images[key], (plateau.CELL_SIZE, plateau.CELL_SIZE))

# Charger les données JSON depuis le fichier
def load_biomes_data(filepath):
    """Charge les données des biomes à partir du fichier JSON."""
    try:
        with open(filepath, 'r', encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {filepath} n'a pas été trouvé.")
        return []
    except json.JSONDecodeError:
        print("Erreur : Le fichier JSON est mal formaté.")
        return []

def get_biomes_from_data(data):
    """Retourne la liste des biomes avec leurs informations."""
    biomes = []
    for biome_data in data:
        biomes.append({
            'id': biome_data['idRessource'],
            'name': biome_data['nom'],
            'position': (biome_data['positionX'], biome_data['positionY'])
        })
    return biomes

# Charger les biomes depuis le fichier JSON
biomes_data = load_biomes_data('map.json')
biomes = get_biomes_from_data(biomes_data)

# Fonction pour obtenir le biome selon sa position
def get_biome_for_position(position):
    """Récupère le biome à la position donnée."""
    x, y = position
    if 0 <= y < len(plateau.carte) and 0 <= x < len(plateau.carte[0]):
        return plateau.carte[y][x]  # Accès à la carte selon x, y
    print(f" Position hors carte: {position}, retour à 'plaine'.")
    return PLAIN  # Par défaut, si hors limite

# Fonction pour dessiner les biomes
def draw_biomes():
    """Dessine les biomes sur le plateau en fonction du type."""
    for biome in biomes:
        position_x, position_y = biome['position']
        biome_type = get_biome_for_position((position_x, position_y))  # Récupérer le biome

        # Sélectionner l'image en fonction du biome
        match biome_type:
            case PLAIN:
                img = biomes_images[PLAIN]
            case DESERT:
                img = biomes_images[DESERT]
            case LAC:
                img = biomes_images[LAC]
            case _:
                img = biomes_images[PLAIN]  # Par défaut

        # Dessiner le biome à sa position
        plateau.screen.blit(img, (position_x * plateau.CELL_SIZE, position_y * plateau.CELL_SIZE))



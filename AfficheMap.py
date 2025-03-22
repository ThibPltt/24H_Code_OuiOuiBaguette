import pygame
import sys
import json

# Taille de la carte (nombre de cases en x et y)
NOMBRE_CASES_X = 10
NOMBRE_CASES_Y = 8
TAILLE_CASE = 60  # Taille de chaque case en pixels

# Définir les types de terrains
PLAIN = "plaine"
DESERT = "desert"
LAC = "lac"

# Carte 2D avec des terrains (un exemple simple, cela pourrait être amélioré)
carte = [
    [PLAIN, DESERT, PLAIN, PLAIN, LAC, PLAIN, DESERT, PLAIN, PLAIN, LAC],
    [PLAIN, PLAIN, PLAIN, DESERT, PLAIN, LAC, PLAIN, PLAIN, LAC, DESERT],
    [LAC, PLAIN, PLAIN, LAC, DESERT, PLAIN, PLAIN, DESERT, PLAIN, PLAIN],
    [DESERT, PLAIN, PLAIN, DESERT, PLAIN, PLAIN, LAC, PLAIN, PLAIN, DESERT],
    [PLAIN, DESERT, PLAIN, PLAIN, LAC, PLAIN, PLAIN, PLAIN, DESERT, LAC],
    [LAC, PLAIN, DESERT, LAC, PLAIN, PLAIN, PLAIN, PLAIN, DESERT, PLAIN],
    [PLAIN, PLAIN, LAC, DESERT, PLAIN, LAC, PLAIN, PLAIN, PLAIN, PLAIN],
    [DESERT, PLAIN, PLAIN, PLAIN, LAC, PLAIN, DESERT, LAC, PLAIN, LAC]
]

JSON_PATH="villageois.json"


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
    
villageois = json.loads("villageois.json")

# Initialisation de Pygame
pygame.init()

# Créer la fenêtre
fenetre = pygame.display.set_mode((NOMBRE_CASES_X * TAILLE_CASE, NOMBRE_CASES_Y * TAILLE_CASE))
pygame.display.set_caption("Carte Simple")

# Charger les images
images = {
    PLAIN: pygame.Color(0, 255, 0),  # Vert pour la plaine
    DESERT: pygame.Color(255, 255, 0),  # Jaune pour le désert
    LAC: pygame.Color(0, 0, 255),  # Bleu pour le lac
    "villageois": pygame.Surface((TAILLE_CASE // 2, TAILLE_CASE // 2))  # Un simple carré pour le villageois
}

# Dessiner la carte
def dessiner_carte():
    for y in range(NOMBRE_CASES_Y):
        for x in range(NOMBRE_CASES_X):
            # Obtenez le terrain de la carte
            terrain = carte[y][x]
            couleur = images[terrain]

            # Dessiner la case correspondante
            pygame.draw.rect(fenetre, couleur, (x * TAILLE_CASE, y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))

# Dessiner les villageois
def dessiner_villageois():
    for villageois_data in villageois:
        x = villageois_data["positionX"]
        y = villageois_data["positionY"]
        pygame.draw.circle(fenetre, pygame.Color(255, 0, 0), (x * TAILLE_CASE + TAILLE_CASE // 2, y * TAILLE_CASE + TAILLE_CASE // 2), 15)  # Dessiner un cercle pour chaque villageois

# Boucle principale
def boucle_principale():
    clock = pygame.time.Clock()

    # Boucle du jeu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Remplir l'écran de fond
        fenetre.fill((255, 255, 255))  # Blanc

        # Dessiner la carte
        dessiner_carte()

        # Dessiner les villageois
        dessiner_villageois()

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Limiter à 60 images par seconde
        clock.tick(60)

# Démarrer la boucle principale
boucle_principale()

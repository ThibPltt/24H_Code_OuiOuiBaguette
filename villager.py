# villager.py
import pygame
import plateau  # Importation du fichier plateau.py
import json

# Charger les données JSON depuis le fichier
def load_villagers_data(filepath):
    """Charge les données des villageois à partir du fichier JSON."""
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def get_villagers_from_data(data):
    """Retourne la liste des villageois avec leurs informations."""
    villagers = []
    for villager_data in data:
        villagers.append({
            'id': villager_data['idVillageois'],
            'name': villager_data['nom'],
            'position': (villager_data['positionX'], villager_data['positionY'])
        })
    return villagers

# Charger l'image du villageois
villager_img = pygame.image.load("assets2D/villagers/villager.png").convert_alpha()

# Redimensionner l'image du villageois pour qu'elle couvre 3x3 cases (3x CELL_SIZE)
villager_scaled = pygame.transform.scale(villager_img, (3 * plateau.CELL_SIZE, 3 * plateau.CELL_SIZE))

# Charger les villageois depuis le fichier JSON
villagers_data = load_villagers_data('Datas/VillageoisData')
villagers = get_villagers_from_data(villagers_data)

# Fonction pour dessiner tous les villageois
def draw_villagers():
    """Fonction pour dessiner les villageois sur le plateau."""
    for villager in villagers:
        # Calculer la position en pixels à partir des coordonnées en cases
        position_x, position_y = villager['position']
        # Dessiner le villageois à sa position
        plateau.screen.blit(villager_scaled, (position_x * plateau.CELL_SIZE, position_y * plateau.CELL_SIZE))

def handle_keys():
    """Fonction pour gérer les entrées clavier et déplacer le villageois."""
    global villagers

    keys = pygame.key.get_pressed()

    # Déplacer vers la droite
    if keys[pygame.K_RIGHT]:
        for villager in villagers:
            villager['position'] = (villager['position'][0] + 1, villager['position'][1])

    # Déplacer vers la gauche
    if keys[pygame.K_LEFT]:
        for villager in villagers:
            villager['position'] = (villager['position'][0] - 1, villager['position'][1])

    # Déplacer vers le bas
    if keys[pygame.K_DOWN]:
        for villager in villagers:
            villager['position'] = (villager['position'][0], villager['position'][1] + 1)

    # Déplacer vers le haut
    if keys[pygame.K_UP]:
        for villager in villagers:
            villager['position'] = (villager['position'][0], villager['position'][1] - 1)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_keys()  # Gérer les mouvements des villageois

        plateau.screen.fill(plateau.GREEN)  # Fond vert

        # Dessiner la grille, le bosquet et les villageois
        plateau.draw_grid()
        plateau.draw_bosquet()
        draw_villagers()  # Dessiner tous les villageois

        pygame.display.flip()  # Rafraîchir l'affichage

    pygame.quit()

if __name__ == "__main__":
    main()

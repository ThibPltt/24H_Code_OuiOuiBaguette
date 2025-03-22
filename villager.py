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

# Redimensionner l'image pour qu'elle fasse 1x1 case
villager_scaled = pygame.transform.scale(villager_img, (plateau.CELL_SIZE, plateau.CELL_SIZE))


# Charger les villageois depuis le fichier JSON
villagers_data = load_villagers_data('villageois.json')
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
    """Fonction pour gérer les entrées clavier et déplacer le villageois d'une case."""
    global villagers
    keys = pygame.key.get_pressed()

    # Déplacer vers la droite (1 case)
    if keys[pygame.K_RIGHT]:
        for villager in villagers:
            villager['position'] = (villager['position'][0] + 1, villager['position'][1])

    # Déplacer vers la gauche (1 case)
    if keys[pygame.K_LEFT]:
        for villager in villagers:
            villager['position'] = (villager['position'][0] - 1, villager['position'][1])

    # Déplacer vers le bas (1 case)
    if keys[pygame.K_DOWN]:
        for villager in villagers:
            villager['position'] = (villager['position'][0], villager['position'][1] + 1)

    # Déplacer vers le haut (1 case)
    if keys[pygame.K_UP]:
        for villager in villagers:
            villager['position'] = (villager['position'][0], villager['position'][1] - 1)

def draw_coordinates():
    """Fonction pour dessiner les coordonnées des villageois en bas de la grille."""
    font = pygame.font.SysFont("Arial", 18)  # Police pour le texte des coordonnées
    for villager in villagers:
        position_x, position_y = villager['position']
        # Affichage des coordonnées sous la grille
        coord_text = font.render(f"Coordonnées: ({position_x}, {position_y})", True, (255, 255, 255))
        # Dessiner le texte en bas, centré
        plateau.screen.blit(coord_text, (plateau.WIDTH // 2 - coord_text.get_width() // 2, plateau.HEIGHT - 30))

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
        draw_villagers()  # Dessiner tous les villageois

        pygame.display.flip()  # Rafraîchir l'affichage

    pygame.quit()

if __name__ == "__main__":
    main()

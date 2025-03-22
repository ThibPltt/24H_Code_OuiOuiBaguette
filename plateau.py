import pygame

# Configuration du plateau
GRID_SIZE = 33  # Nombre de cases (33x33)
CELL_SIZE = 20  # Taille d'une case en pixels
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE

# Couleurs
GREEN = (161, 214, 124)  # Vert foncé pour le fond
GRAY = (200, 200, 200)  # Gris pour les bordures

# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plateau avec images 7x7 cases")

# Charger l'image avec transparence
image_path = "assets2D/nature/bosquet.png"
bosquet_img = pygame.image.load(image_path).convert_alpha()

# Définir la taille de l'image pour qu'elle corresponde à 7x7 cases
TILE_SIZE = 7 * CELL_SIZE  # 7 cases * 20 pixels = 140 pixels
bosquet_img = pygame.transform.scale(bosquet_img, (TILE_SIZE, TILE_SIZE))

# Boucle de jeu
running = True
while running:
    screen.fill(GREEN)  # Fond vert

    # Dessiner l'image en mosaïque pour couvrir le plateau
    for x in range(0, WIDTH, TILE_SIZE):
        for y in range(0, HEIGHT, TILE_SIZE):
            screen.blit(bosquet_img, (x, y))

    # Dessiner la grille (bordures des cases)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)  # Bordures des cases

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()  # Rafraîchir l'affichage

pygame.quit()

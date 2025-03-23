# plateau.py
import pygame

# Configuration du plateau
GRID_SIZE = 33  # Nombre de cases (33x33)
CELL_SIZE = 20  # Taille d'une case en pixels
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE


# Couleurs
GREEN = (231, 245, 221)  # Vert foncé pour le fond
GRAY = (200, 200, 200)  # Gris pour les bordures
BLACK = (0, 0, 0)

# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Plateau")

def draw_grid():
    """Fonction pour dessiner la grille sur le plateau."""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)  # Bordures des cases



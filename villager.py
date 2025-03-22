# villager.py
import pygame
import plateau  # Importation du fichier plateau.py

# Charger l'image du villager
villager_img = pygame.image.load("assets2D/villagers/villager.png").convert_alpha()

# Redimensionner l'image du villager pour qu'elle couvre 9 cases (3x3)
villager_scaled = pygame.transform.scale(villager_img, (3 * plateau.CELL_SIZE, 3 * plateau.CELL_SIZE))

# Position de l'image du villager (sur la grille)
img_x, img_y = 5, 7  # Position (5, 7) en termes de cases

def draw_villager():
    """Fonction pour dessiner l'image du villager sur le plateau."""
    # Dessiner le villager sur la case spécifiée
    plateau.screen.blit(villager_scaled, (img_x * plateau.CELL_SIZE, img_y * plateau.CELL_SIZE))

def main():
    running = True
    while running:
        plateau.screen.fill(plateau.GREEN)  # Fond vert

        # Dessiner la grille et les images
        plateau.draw_grid()
        plateau.draw_bosquet()
        draw_villager()

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()  # Rafraîchir l'affichage

    pygame.quit()

if __name__ == "__main__":
    main()

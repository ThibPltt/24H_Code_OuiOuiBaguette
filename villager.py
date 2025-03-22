# villager.py
import pygame
import plateau  # Importation du fichier plateau.py

# Charger l'image du villager
villager_img = pygame.image.load("assets2D/villagers/villager.png").convert_alpha()

# Redimensionner l'image du villager pour qu'elle couvre 9 cases (3x3)
villager_scaled = pygame.transform.scale(villager_img, (3 * plateau.CELL_SIZE, 3 * plateau.CELL_SIZE))

# Position de l'image du villager (sur la grille)
img_x, img_y = 5, 7  # Position (5, 7) en termes de cases (les multiples de 3)

def draw_villager():
    """Fonction pour dessiner l'image du villager sur le plateau."""
    # Dessiner le villager sur la case spécifiée
    plateau.screen.blit(villager_scaled, (img_x * plateau.CELL_SIZE, img_y * plateau.CELL_SIZE))

def handle_keys(event):
    """Fonction pour gérer les entrées clavier et déplacer le villageois."""
    global img_x, img_y

    if event.type == pygame.KEYDOWN:
        # Déplacer vers la droite
        if event.key == pygame.K_RIGHT:
            if img_x < plateau.GRID_SIZE - 3:  # Limiter au bord droit
                img_x += 1

        # Déplacer vers la gauche
        if event.key == pygame.K_LEFT:
            if img_x > 0:  # Limiter au bord gauche
                img_x -= 1

        # Déplacer vers le bas
        if event.key == pygame.K_DOWN:
            if img_y < plateau.GRID_SIZE - 3:  # Limiter au bord bas
                img_y += 1

        # Déplacer vers le haut
        if event.key == pygame.K_UP:
            if img_y > 0:  # Limiter au bord haut
                img_y -= 1

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Gérer les événements de clavier
            handle_keys(event)

        plateau.screen.fill(plateau.GREEN)  # Fond vert

        # Dessiner la grille, le bosquet et le villageois
        plateau.draw_grid()
        plateau.draw_bosquet()
        draw_villager()

        pygame.display.flip()  # Rafraîchir l'affichage

    pygame.quit()

if __name__ == "__main__":
    main()

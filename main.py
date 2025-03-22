# main.py
import pygame
import plateau
import villager

def main():
    """Fonction principale du jeu."""
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Gérer les mouvements des villageois avec les flèches
        villager.handle_keys()

        # Remplir l'écran avec le fond vert
        plateau.screen.fill(plateau.GREEN)

        # Dessiner la grille, le bosquet et les villageois
        plateau.draw_grid()  # Dessiner la grille
        plateau.draw_bosquet()  # Dessiner le bosquet
        villager.draw_villagers()  # Dessiner les villageois

        # Rafraîchir l'affichage
        pygame.display.flip()

        # Limiter la fréquence de rafraîchissement
        pygame.time.Clock().tick(60)  # 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()

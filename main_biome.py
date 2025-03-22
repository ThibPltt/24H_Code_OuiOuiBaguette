import pygame
import plateau  # Importation du fichier plateau.py
import villager

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        villager.handle_keys()  # Gérer les mouvements des villageois

        plateau.screen.fill(plateau.GREEN)  # Fond vert

        # Dessiner la grille, le bosquet et les villageois
        plateau.draw_grid()
        villager.draw_villagers()  # Dessiner tous les villageois

        pygame.display.flip()  # Rafraîchir l'affichage

    pygame.quit()

if __name__ == "__main__":
    main()
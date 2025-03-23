import pygame
import plateau  # Importation du fichier plateau.py
import biome    # Importation du fichier biome.py
import villager # Importation du fichier villager.py

def main():
    """Boucle principale du jeu."""
    pygame.init()  # Initialisation de Pygame
    
    clock = pygame.time.Clock()  # Limitation du framerate
    running = True  # Contrôle du jeu

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mettre à jour l'écran
        plateau.screen.fill(plateau.GREEN)  # Fond vert

        # Dessiner la carte avec les biomes et la grille
        plateau.draw_grid()
        biome.draw_biomes()  # Dessiner les biomes
        villager.draw_villagers()  # Dessiner les villageois

        pygame.display.flip()  # Rafraîchir l'affichage
        clock.tick(60)  # Limite à 60 FPS

    pygame.quit()  # Quitter Pygame proprement

if __name__ == "__main__":
    main()

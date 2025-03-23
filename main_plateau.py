import pygame
import plateau  # Importation du fichier plateau.py
import villager
import time

def main():
    pygame.init()
    running = True
    last_update = time.time()  # Timer for API updates

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fetch new positions every 12.5 seconds (API cooldown)
        if time.time() - last_update > 12.5:
            villager.fetch_villagers()
            last_update = time.time()

        plateau.screen.fill(plateau.GREEN)  # Fond vert
        plateau.draw_grid()
        villager.draw_villagers()  # Draw villagers at API positions
        villager.draw_coordinates()  # Display coordinates

        pygame.display.flip()  # Refresh screen

    pygame.quit()

if __name__ == "__main__":
    villager.fetch_villagers()  # Fetch initial positions
    main()
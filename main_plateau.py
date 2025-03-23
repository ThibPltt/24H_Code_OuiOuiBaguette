import pygame
import plateau  # Import the grid system
from villager import VillagerManager
from ressources import ResourceManager
import time

def main():
    pygame.init()
    running = True
    last_update = time.time()  # Timer for API updates

    villager_manager = VillagerManager()
    resource_manager = ResourceManager()  # Create resource manager

    # Initial fetch
    villager_manager.fetch_villagers()
    resource_manager.fetch_resources()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fetch new positions and resources every 12.5 seconds
        if time.time() - last_update > 12.5:
            villager_manager.fetch_villagers()
            resource_manager.fetch_resources()
            last_update = time.time()

        plateau.screen.fill(plateau.GREEN)  # Background color
        plateau.draw_grid()

        resource_manager.draw_resources()  # ✅ Draw resources on the grid
        villager_manager.draw_villagers()  # Draw villagers
        villager_manager.draw_coordinates()  # ✅ Display villagers & resources

        pygame.display.flip()  # Refresh screen

    pygame.quit()

if __name__ == "__main__":
<<<<<<< HEAD
    villager.fetch_villagers()  # Fetch initial positions
    main()
=======
    main()
>>>>>>> 54f709377370fe5630e57f885d1f6130ebc39baa

import pygame
import plateau  # Import the grid system

# Load building images
cabane_bucheron_img = pygame.image.load("assets2D/buildings/cabane_bucheron.png").convert_alpha()
cabane_bucheron_scaled = pygame.transform.scale(cabane_bucheron_img, (plateau.CELL_SIZE, plateau.CELL_SIZE))

class BuildingManager:
    def __init__(self):
        self.buildings = []  # Stores buildings as {"name": "CABANE_DE_BUCHERON", "position": (x, y)}

    def add_building(self, name, x, y):
        """Add a new building to the grid."""
        self.buildings.append({"name": name, "position": (x, y)})

    def draw_buildings(self):
        """Draw all buildings on the grid."""
        for building in self.buildings:
            x, y = building["position"]
            if building["name"] == "CABANE_DE_BUCHERON":
                plateau.screen.blit(cabane_bucheron_scaled, (x * plateau.CELL_SIZE, y * plateau.CELL_SIZE))

import pygame
import sys
import os

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Jeu de Stratégie")

# Chemins des images
image_paths = {
    "chateau": r'C:\Users\Thibaut\Desktop\ENSIM\AUTRES\24H_CODE\24H_Code_OuiOuiBaguette\24H_Code_OuiOuiBaguette\assets2D\buildings\chateau.png',
    "ferme": r'C:\Users\Thibaut\Desktop\ENSIM\AUTRES\24H_CODE\24H_Code_OuiOuiBaguette\24H_Code_OuiOuiBaguette\assets2D\buildings\ferme.png',
}

# Vérifier si les fichiers existent
for name, path in image_paths.items():
    if not os.path.exists(path):
        print(f"Fichier introuvable: {path}")

# Charger les images
images = {}
try:
    for name, path in image_paths.items():
        images[name] = pygame.image.load(path)
except pygame.error as e:
    print(f"Erreur lors du chargement des images: {e}")
    pygame.quit()
    sys.exit()

class Building:
    def __init__(self, name, construction_cost, image, position, energy_required=0, scale_factor=1.0):
        self.name = name
        self.construction_cost = construction_cost
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale_factor), int(image.get_height() * scale_factor)))
        self.position = position
        self.energy_required = energy_required
        self.is_constructed = False
        self.construction_progress = 0

    def construct(self, actions):
        self.construction_progress += actions
        if self.construction_progress >= self.construction_cost:
            self.is_constructed = True
            print(f"{self.name} is fully constructed.")
        else:
            print(f"{self.name} construction in progress: {self.construction_progress}/{self.construction_cost}")

    def draw(self, surface):
        surface.blit(self.image, self.position)

def main():
    global window  # Déclarer window comme variable globale
    clock = pygame.time.Clock()
    scale_factor = 0.5  # Réduire la taille des images à 50%

    # Créer une instance de chaque bâtiment
    chateau = Building("Chateau", 2, images["chateau"], (50, 100), scale_factor=scale_factor)
    ferme = Building("Ferme", 2, images["ferme"], (100, 200), scale_factor=scale_factor)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                # Mettre à jour les dimensions de la fenêtre
                WINDOW_WIDTH, WINDOW_HEIGHT = event.size
                window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)

        window.fill((255, 255, 255))  # Remplir la fenêtre avec du blanc

        # Dessiner chaque bâtiment deux fois à des positions différentes
        chateau.draw(window)
        window.blit(chateau.image, (200, 100))  # Deuxième affichage du château

        ferme.draw(window)
        window.blit(ferme.image, (400, 200))  # Deuxième affichage de la ferme

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()


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
'''
import ReadRangePlateau
import pygame
# Dimensions des cases
CELL_SIZE = 32

# Chargement de l'image du bosquet (assurez-vous que l'image existe)
image_path = "assets2D/nature/bosquet.png"  # Remplace par ton chemin d'image
bosquet_image = pygame.image.load(image_path).convert_alpha()

# Redimensionner l’image pour qu’elle tienne dans une case
bosquet_image = pygame.transform.scale(bosquet_image, (CELL_SIZE, CELL_SIZE))


def main():
    print("=== Système de récupération des cases du plateau ===")
    
    # Demande à l'utilisateur de saisir les coordonnées
    try:
        x = int(input("Entrez la coordonnée X : "))
        y = int(input("Entrez la coordonnée Y : "))
        
        # Récupérer les informations de la case
        case = ReadRangePlateau.get_case_par_coord(x, y)
        
        # Vérifie si case est une liste et prend le premier élément
        if isinstance(case, list) and len(case) > 0:
            case = case[0]  # Prendre la première case de la liste

        if case:
            print(f"\n Case trouvée aux coordonnées ({x}, {y}) :")
            print(f"  - Biome : {case['biome']['nom']} ({case['biome']['description']})")
            print(f"  - Accessible : {'Oui' if case['accessible'] else 'Non'}")
            
            # Affichage des ressources disponibles
            print("  - Ressources disponibles :")
            for ressource in case["ressources"]:
                nom = ressource["ressource"]["nom"]
                description = ressource["ressource"]["description"]
                quantite = ressource["quantite"]
                print(f"    - {nom} ({description}) : {quantite}")
        else:
            print(f"Aucune case trouvée aux coordonnées ({x}, {y}).")

    except ValueError:
        print("Erreur : Veuillez entrer des coordonnées valides (nombres entiers).")

if __name__ == "__main__":
    main()
<<<<<<< HEAD:main.py
'''
=======
    
# main.py
import pygame
import plateau
import villager

import pygame
import villager
import plateau  # Importation du fichier plateau.py

# Dimensions des cases
CELL_SIZE = 32

# Chargement de l'image du bosquet (assurez-vous que l'image existe)
image_path = "assets2D/nature/bosquet.png"  # Remplace par ton chemin d'image
bosquet_image = pygame.image.load(image_path).convert_alpha()

# Redimensionner l’image pour qu’elle tienne dans une case
bosquet_image = pygame.transform.scale(bosquet_image, (CELL_SIZE, CELL_SIZE))

def draw_bosquet():
    """Fonction pour dessiner l'image du bosquet à chaque case."""
    # On suppose que le bosquet est dans toutes les cases ou dans une certaine position
    # Par exemple, pour le dessiner dans une case spécifique, on utilise ces coordonnées
    x, y = 5, 5  # Exemple de coordonnées
    plateau.screen.blit(bosquet_image, (x * CELL_SIZE, y * CELL_SIZE))  # Affichage de l'image

def main():
    """Fonction principale du jeu."""
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Gérer les mouvements des villageois avec les flèches
        villager.handle_keys()  # Assurez-vous que la fonction 'handle_keys' existe et fonctionne correctement

        # Remplir l'écran avec le fond vert
        plateau.screen.fill(plateau.GREEN)

        # Dessiner la grille
        plateau.draw_grid()


        # Dessiner les villageois
        villager.draw_villagers()  # Assurez-vous que la fonction 'draw_villagers' existe et fonctionne correctement

        # Rafraîchir l'affichage
        pygame.display.flip()

        # Limiter la fréquence de rafraîchissement à 60 FPS
        pygame.time.Clock().tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

>>>>>>> 385ca503e00c47938804931aac42d2fed18dc608:main_biome.py

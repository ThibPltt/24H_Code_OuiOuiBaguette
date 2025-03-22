'''
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
            print(f"\n📍 Case trouvée aux coordonnées ({x}, {y}) :")
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
        print("❌ Erreur : Veuillez entrer des coordonnées valides (nombres entiers).")

if __name__ == "__main__":
    main()


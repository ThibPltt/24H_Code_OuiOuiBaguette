import pygame
import sys

# Initialisation de pygame
pygame.init()

# Configurer la fenêtre (bien que nous n'en aurons pas besoin ici, mais pygame nécessite une fenêtre)
pygame.display.set_mode((1, 1))
pygame.display.set_caption("Jeu Touche Z")

# Fonction principale
def jeu():
    print("Appuyez sur la touche Z pour afficher un message.")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Récupérer les touches pressées
        touches = pygame.key.get_pressed()

        # Si la touche "Z" est pressée, afficher le message
        if touches[pygame.K_z]:
            print("Bonjour à vous")
            break  # Quitte la boucle une fois la touche pressée

# Lancer le jeu
jeu()

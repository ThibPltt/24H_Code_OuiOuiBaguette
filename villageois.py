import time
from enum import Enum

class Instruction(Enum):
    DEPLACEMENT_DROITE = "DEPLACEMENT_DROITE"
    DEPLACEMENT_GAUCHE = "DEPLACEMENT_GAUCHE"
    DEPLACEMENT_HAUT = "DEPLACEMENT_HAUT"
    DEPLACEMENT_BAS = "DEPLACEMENT_BAS"
    RECOLTER = "RECOLTER"
    COMMENCER_CONSTRUCTION = "COMMENCER_CONSTRUCTION"
    CONSTRUIRE = "CONSTRUIRE"
    RECYCLER_BATIMENT = "RECYCLER_BATIMENT"

class Villageois:
    def __init__(self, id_villageois, position):
        self.id = id_villageois
        self.position = position  # (x, y)
        self.en_cooldown = False
    
    def executer_instruction(self, instruction):
        if self.en_cooldown:
            print(f"Villageois {self.id} est en cooldown. Instruction ignorée.")
            return
        
        print(f"Villageois {self.id} exécute: {instruction.value}")
        self.en_cooldown = True
        time.sleep(12.5)  # Simule le cooldown
        self.en_cooldown = False
        print(f"Villageois {self.id} prêt pour une nouvelle instruction.")

# Exemple d'utilisation
#if __name__ == "__main__":
#    v1 = Villageois(1, (5, 5))
#    v1.executer_instruction(Instruction.DEPLACEMENT_DROITE)
#    v1.executer_instruction(Instruction.RECOLTER)

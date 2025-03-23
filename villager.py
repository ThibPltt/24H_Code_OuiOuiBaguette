import requests
import pygame
import plateau  # Import the grid system
from ressources import ResourceManager  # Import the resource manager

# API Info
idEquipe = "8503fb81-528b-4b2d-8b1f-783bcc8bf6db"
base_url = f"http://51.210.117.22:8080/equipes/{idEquipe}/villageois"

headers = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI2VG5aX1o4WlM2YTlYczJqckl4RTZLS0lNbjgyaTdxN3Z4cTRtY3dQOE13In0.eyJleHAiOjE3NDI4MjUxNjUsImlhdCI6MTc0MjY1MjM2NSwianRpIjoiM2JhM2I3MjMtNWRkNy00NmJiLTkyOWItNzcyZWVmYWY3YmJjIiwiaXNzIjoiaHR0cDovLzUxLjIxMC4xMTcuMjI6ODA4MS9yZWFsbXMvY29kZWxlbWFucyIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI5ODU4OGRlNC0yOTNhLTRlMDYtODZhMS1kMTA2NTI3YTliZjYiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ3b2xvbG8tYmFja2VuZCIsInNlc3Npb25fc3RhdGUiOiI2NmI2OWI3OS1iMWNkLTRiMDgtODI5Yy1iNjc3MGYyYjNhMGUiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsImRlZmF1bHQtcm9sZXMtY29kZWxlbWFucyIsInVtYV9hdXRob3JpemF0aW9uIiwidXNlciJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsInNpZCI6IjY2YjY5Yjc5LWIxY2QtNGIwOC04MjljLWI2NzcwZjJiM2EwZSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoib3VpIG91aSBiYWd1ZXR0ZSIsInRlYW1faWQiOiI4NTAzZmI4MS01MjhiLTRiMmQtOGIxZi03ODNiY2M4YmY2ZGIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJsZXMtY2VudHVyaW9ucy12ZXJ0cyIsImdpdmVuX25hbWUiOiJvdWkgb3VpIGJhZ3VldHRlIn0.EZpBLan-yyD4UhpW8gMwTxPFpLCQNf7vD-5AUX3MNxUsPMn-9Lq234HR0dMYTPtGOoVXb9Z-eA3WLd0qn83P_YGV0s6yPGbluHASlbzoUvDk6CPGbd8j2wRJieMAUhj0MlAGV76AAO8DbqEkJD52ubOfUh9Gtguj7J5z_5-MDQuNisODKW3uMCOpn0v0mIGB9dLY5XNLBjjM1WMS72ujDpdGjAgywmBVSuxPgx-5mekWWAK87SiHuH6K7nmT643rfcYlmi2-Zg4_Nt4swVDrpd6sgyLw9JhfgJ5y_n1PUF_50ZUK5owHRTG1EjwCoV-BUzHp25oW2N0961SNgYSUNw",
    "Content-Type": "application/json"
}

# Load villager image
villager_img = pygame.image.load("assets2D/villagers/villager.png").convert_alpha()
villager_scaled = pygame.transform.scale(villager_img, (plateau.CELL_SIZE, plateau.CELL_SIZE))

class VillagerManager:
    def __init__(self):
        self.villagers = []
        self.resources = ResourceManager()  # Create resource manager instance
        self.fetch_villagers()

    def fetch_villagers(self):
        """Fetch all villagers' positions from the API."""
        response = requests.get(base_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            self.villagers = [
                {
                    "id": v["idVillageois"],
                    "name": v["nom"],
                    "position": (v["positionX"], v["positionY"]),
                }
                for v in data
            ]
            print("✅ Villagers updated:", self.villagers)
        else:
            print(f"❌ Error fetching villagers: {response.status_code} - {response.text}")

    def draw_villagers(self):
        """Draw villagers at their positions."""
        for villager in self.villagers:
            x, y = villager["position"]
            plateau.screen.blit(villager_scaled, (x * plateau.CELL_SIZE, y * plateau.CELL_SIZE))

    def draw_coordinates(self):
        """Display villagers' positions and total resources in the top-right."""
        font = pygame.font.SysFont("Arial", 18)
        color_black = (0, 0, 0)
        y_offset = 150

        # 🎯 Display Villager Positions
        for villager in self.villagers:
            x, y = villager["position"]
            coord_text = font.render(f"{villager['name']}: ({x}, {y})", True, color_black)
            plateau.screen.blit(coord_text, (plateau.WIDTH - 250, y_offset))
            y_offset += 20  # Move down for next villager

        # 📢 Space between villagers and resources
        y_offset += 20
        resource_text = font.render("💰 Ressources:", True, color_black)
        plateau.screen.blit(resource_text, (plateau.WIDTH - 250, y_offset))
        y_offset += 20

        # 💰 Display Total Resources
        total_resources = self.resources.fetch_total_resources()  # Get summed resources
        for resource, qty in total_resources.items():
            resource_info = font.render(f"{resource}: {qty}", True, color_black)
            plateau.screen.blit(resource_info, (plateau.WIDTH - 250, y_offset))
            y_offset += 20  # Move down for next resource

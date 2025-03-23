import requests
import pygame
import plateau  # Import the grid system

# API Info
base_url = "http://51.210.117.22:8080/equipes/8503fb81-528b-4b2d-8b1f-783bcc8bf6db"

headers = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI2VG5aX1o4WlM2YTlYczJqckl4RTZLS0lNbjgyaTdxN3Z4cTRtY3dQOE13In0.eyJleHAiOjE3NDI4MjUxNjUsImlhdCI6MTc0MjY1MjM2NSwianRpIjoiM2JhM2I3MjMtNWRkNy00NmJiLTkyOWItNzcyZWVmYWY3YmJjIiwiaXNzIjoiaHR0cDovLzUxLjIxMC4xMTcuMjI6ODA4MS9yZWFsbXMvY29kZWxlbWFucyIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI5ODU4OGRlNC0yOTNhLTRlMDYtODZhMS1kMTA2NTI3YTliZjYiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ3b2xvbG8tYmFja2VuZCIsInNlc3Npb25fc3RhdGUiOiI2NmI2OWI3OS1iMWNkLTRiMDgtODI5Yy1iNjc3MGYyYjNhMGUiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsImRlZmF1bHQtcm9sZXMtY29kZWxlbWFucyIsInVtYV9hdXRob3JpemF0aW9uIiwidXNlciJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsInNpZCI6IjY2YjY5Yjc5LWIxY2QtNGIwOC04MjljLWI2NzcwZjJiM2EwZSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoib3VpIG91aSBiYWd1ZXR0ZSIsInRlYW1faWQiOiI4NTAzZmI4MS01MjhiLTRiMmQtOGIxZi03ODNiY2M4YmY2ZGIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJsZXMtY2VudHVyaW9ucy12ZXJ0cyIsImdpdmVuX25hbWUiOiJvdWkgb3VpIGJhZ3VldHRlIn0.EZpBLan-yyD4UhpW8gMwTxPFpLCQNf7vD-5AUX3MNxUsPMn-9Lq234HR0dMYTPtGOoVXb9Z-eA3WLd0qn83P_YGV0s6yPGbluHASlbzoUvDk6CPGbd8j2wRJieMAUhj0MlAGV76AAO8DbqEkJD52ubOfUh9Gtguj7J5z_5-MDQuNisODKW3uMCOpn0v0mIGB9dLY5XNLBjjM1WMS72ujDpdGjAgywmBVSuxPgx-5mekWWAK87SiHuH6K7nmT643rfcYlmi2-Zg4_Nt4swVDrpd6sgyLw9JhfgJ5y_n1PUF_50ZUK5owHRTG1EjwCoV-BUzHp25oW2N0961SNgYSUNw",
    "Content-Type": "application/json"
}

# Colors for each resource type
RESOURCE_COLORS = {
    "NOURRITURE": (255, 200, 0),  # Yellow
    "BOIS": (139, 69, 19),        # Brown
    "PIERRE": (128, 128, 128),    # Gray
    "FER": (192, 192, 192),       # Light gray
    "CHARBON": (54, 54, 54),      # Dark gray
    "ENERGIE": (0, 255, 255),     # Cyan
    "POINT": (255, 0, 255),       # Magenta
    "POLLUTION": (0, 100, 0)      # Dark green
}

class ResourceManager:
    def __init__(self):
        self.resources = []
        self.fetch_resources()

    def fetch_resources(self):
        """Fetch resources dynamically from the API and validate response."""
        response = requests.get(base_url, headers=headers)

        if response.status_code == 200:
            try:
                data = response.json()  # Ensure data is correctly parsed
                print("📥 Raw API Response:", data)  # Debugging: print the entire response

                # ✅ Extract resources correctly
                if isinstance(data, dict) and "ressources" in data and isinstance(data["ressources"], list):
                    self.resources = [
                        {
                            "nom": res["ressource"]["nom"],  # ✅ Fix: Get name from "ressource"
                            "quantite": res["quantite"]      # ✅ Get quantity correctly
                        }
                        for res in data["ressources"]  # ✅ Ensure we iterate over the correct key
                    ]
                    print("✅ Resources updated:", self.resources)  # Debugging
                else:
                    print("⚠️ Unexpected API response format. 'ressources' key missing or incorrect.")
                    self.resources = []

            except Exception as e:
                print(f"⚠️ JSON Parsing Error: {e}")
                self.resources = []

        else:
            print(f"❌ API Error: {response.status_code} - {response.text}")
            self.resources = []

    def fetch_total_resources(self):
        """Calculate total resources separately for each type."""
        total_resources = {key: 0 for key in RESOURCE_COLORS.keys()}  # ✅ Ensure each resource has a category

        for res in self.resources:
            resource_name = res["nom"]  # ✅ Extract actual resource name
            if resource_name in total_resources:
                total_resources[resource_name] += res["quantite"]
            else:
                print(f"⚠️ Unrecognized resource type: {resource_name}")  # Debugging unknown resources

        return total_resources

    def draw_resources(self):
        font = pygame.font.SysFont("Arial", 18)
        y_offset = 10
        color_black = (0, 0, 0)

        # 🏷️ Title
        resource_text = font.render("💰 Ressources:", True, color_black)
        plateau.screen.blit(resource_text, (plateau.WIDTH - 250, y_offset))
        y_offset += 20

        # ✅ Fetch once, avoid duplicate calls
        total_resources = self.fetch_total_resources()

        # 💰 Display Each Resource
        for resource, qty in total_resources.items():
            if qty > 0:  # ✅ Hide resources with 0 quantity
                resource_info = font.render(f"{resource}: {qty}", True, color_black)
                plateau.screen.blit(resource_info, (plateau.WIDTH - 250, y_offset))
            y_offset += 20  # Move down for next resource

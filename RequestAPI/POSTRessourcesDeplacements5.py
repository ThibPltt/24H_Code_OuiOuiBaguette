import requests
import random
import time

# API Information
idEquipe = "8503fb81-528b-4b2d-8b1f-783bcc8bf6db"
idVillageois = "77451f36-4820-4d6d-a783-c6fcc74f06c4"
url = f"http://51.210.117.22:8080/equipes/{idEquipe}/villageois/{idVillageois}/demander-action"

headers = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI2VG5aX1o4WlM2YTlYczJqckl4RTZLS0lNbjgyaTdxN3Z4cTRtY3dQOE13In0.eyJleHAiOjE3NDI4MjUxNjUsImlhdCI6MTc0MjY1MjM2NSwianRpIjoiM2JhM2I3MjMtNWRkNy00NmJiLTkyOWItNzcyZWVmYWY3YmJjIiwiaXNzIjoiaHR0cDovLzUxLjIxMC4xMTcuMjI6ODA4MS9yZWFsbXMvY29kZWxlbWFucyIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI5ODU4OGRlNC0yOTNhLTRlMDYtODZhMS1kMTA2NTI3YTliZjYiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ3b2xvbG8tYmFja2VuZCIsInNlc3Npb25fc3RhdGUiOiI2NmI2OWI3OS1iMWNkLTRiMDgtODI5Yy1iNjc3MGYyYjNhMGUiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsImRlZmF1bHQtcm9sZXMtY29kZWxlbWFucyIsInVtYV9hdXRob3JpemF0aW9uIiwidXNlciJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsInNpZCI6IjY2YjY5Yjc5LWIxY2QtNGIwOC04MjljLWI2NzcwZjJiM2EwZSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoib3VpIG91aSBiYWd1ZXR0ZSIsInRlYW1faWQiOiI4NTAzZmI4MS01MjhiLTRiMmQtOGIxZi03ODNiY2M4YmY2ZGIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJsZXMtY2VudHVyaW9ucy12ZXJ0cyIsImdpdmVuX25hbWUiOiJvdWkgb3VpIGJhZ3VldHRlIn0.EZpBLan-yyD4UhpW8gMwTxPFpLCQNf7vD-5AUX3MNxUsPMn-9Lq234HR0dMYTPtGOoVXb9Z-eA3WLd0qn83P_YGV0s6yPGbluHASlbzoUvDk6CPGbd8j2wRJieMAUhj0MlAGV76AAO8DbqEkJD52ubOfUh9Gtguj7J5z_5-MDQuNisODKW3uMCOpn0v0mIGB9dLY5XNLBjjM1WMS72ujDpdGjAgywmBVSuxPgx-5mekWWAK87SiHuH6K7nmT643rfcYlmi2-Zg4_Nt4swVDrpd6sgyLw9JhfgJ5y_n1PUF_50ZUK5owHRTG1EjwCoV-BUzHp25oW2N0961SNgYSUNw",
    "Content-Type": "application/json"
}

# Possible movements
deplacements = ["DEPLACEMENT_DROITE", "DEPLACEMENT_GAUCHE", "DEPLACEMENT_HAUT", "DEPLACEMENT_BAS"]

# Resources to collect
ressources = ["NOURRITURE", "BOIS", "PIERRE", "FER", "CHARBON"]

# Grid settings
cols = 33

# Character initial position
char_pos = [cols // 2, cols // 2]

# Resource counts
resource_counts = {ressource: 0 for ressource in ressources}

def update_position(movement):

    global char_pos
    new_x, new_y = char_pos

    if movement == "DEPLACEMENT_DROITE":
        new_x = min(char_pos[0] + 1, cols - 1)
    elif movement == "DEPLACEMENT_GAUCHE":
        new_x = max(char_pos[0] - 1, 0)
    elif movement == "DEPLACEMENT_HAUT":
        new_y = max(char_pos[1] - 1, 0)
    elif movement == "DEPLACEMENT_BAS":
        new_y = min(char_pos[1] + 1, cols - 1)
        # Mettre à jour la position seulement si elle change
    if (new_x, new_y) != (char_pos[0], char_pos[1]):
        char_pos[0], char_pos[1] = new_x, new_y

def main():
    global char_pos, resource_counts

    while True:
        # 1️⃣ Move randomly
        move_action = random.choice(deplacements)
        move_body = {
            "action": move_action,
            "reference": ""
        }

        response = requests.post(url, json=move_body, headers=headers)

        if response.status_code == 200:
            print(f"✅ Moved: {move_action}")
            update_position(move_action)
        else:
            print(f"❌ Move failed ({move_action}): {response.status_code} - {response.text}")

        time.sleep(13)

        # 2️⃣ Try to collect all resources on the current tile
        for ressource in ressources:
            collect_body = {
                "action": "RECOLTER",
                "reference": ressource
            }

            response = requests.post(url, json=collect_body, headers=headers)

            if response.status_code == 200:
                print(f"✅ Collected: {ressource}")
                resource_counts[ressource] += 1
            elif response.status_code == 204:
                print(f"✅ No {ressource} available to collect")
            else:
                print(f"❌ Collection failed ({ressource}): {response.status_code} - {response.text}")

            time.sleep(13)  # Avoid sending too many requests at once

        # Print resource counts and position
        print(f"Resources: {resource_counts}")
        print(f"Position: ({char_pos[0]}, {char_pos[1]})")

if __name__ == "__main__":
    main()

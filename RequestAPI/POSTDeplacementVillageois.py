import requests

idEquipe = "8503fb81-528b-4b2d-8b1f-783bcc8bf6db"
idVillageois = "b9051f13-4fd1-4937-92ae-69477e6b6210"
# URL de l'API ou du service
url = "http://51.210.117.22:8080/equipes/{idEquipe}&idVillageois={idVillageois}"

# Données à envoyer
data = {
    "username": "les-centurions-verts",
    "password": "NgH2Srgwxp2LQWMurjqK"
}

# En-têtes personnalisés
headers = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI2VG5aX1o4WlM2YTlYczJqckl4RTZLS0lNbjgyaTdxN3Z4cTRtY3dQOE13In0.eyJleHAiOjE3NDI4MjUxNjUsImlhdCI6MTc0MjY1MjM2NSwianRpIjoiM2JhM2I3MjMtNWRkNy00NmJiLTkyOWItNzcyZWVmYWY3YmJjIiwiaXNzIjoiaHR0cDovLzUxLjIxMC4xMTcuMjI6ODA4MS9yZWFsbXMvY29kZWxlbWFucyIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI5ODU4OGRlNC0yOTNhLTRlMDYtODZhMS1kMTA2NTI3YTliZjYiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ3b2xvbG8tYmFja2VuZCIsInNlc3Npb25fc3RhdGUiOiI2NmI2OWI3OS1iMWNkLTRiMDgtODI5Yy1iNjc3MGYyYjNhMGUiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsImRlZmF1bHQtcm9sZXMtY29kZWxlbWFucyIsInVtYV9hdXRob3JpemF0aW9uIiwidXNlciJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsInNpZCI6IjY2YjY5Yjc5LWIxY2QtNGIwOC04MjljLWI2NzcwZjJiM2EwZSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoib3VpIG91aSBiYWd1ZXR0ZSIsInRlYW1faWQiOiI4NTAzZmI4MS01MjhiLTRiMmQtOGIxZi03ODNiY2M4YmY2ZGIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJsZXMtY2VudHVyaW9ucy12ZXJ0cyIsImdpdmVuX25hbWUiOiJvdWkgb3VpIGJhZ3VldHRlIn0.EZpBLan-yyD4UhpW8gMwTxPFpLCQNf7vD-5AUX3MNxUsPMn-9Lq234HR0dMYTPtGOoVXb9Z-eA3WLd0qn83P_YGV0s6yPGbluHASlbzoUvDk6CPGbd8j2wRJieMAUhj0MlAGV76AAO8DbqEkJD52ubOfUh9Gtguj7J5z_5-MDQuNisODKW3uMCOpn0v0mIGB9dLY5XNLBjjM1WMS72ujDpdGjAgywmBVSuxPgx-5mekWWAK87SiHuH6K7nmT643rfcYlmi2-Zg4_Nt4swVDrpd6sgyLw9JhfgJ5y_n1PUF_50ZUK5owHRTG1EjwCoV-BUzHp25oW2N0961SNgYSUNw",
    "Content-Type": "application/json"  # Si tu envoies du JSON
}

body = {
    "action": "DEPLACEMENT_DROITE",
    "reference": ""
}

# Effectuer la requête POST avec des en-têtes
response = requests.post(url, json=data, headers=headers)

# Vérifier le statut de la réponse
if response.status_code == 200:
    print("Requête réussie!")
    print(response.json())  # Afficher la réponse sous forme de JSON
else:
    print(f"Erreur {response.status_code}: {response.text}")

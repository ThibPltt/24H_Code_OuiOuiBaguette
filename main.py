import requests

# Token URL
token_url = "http://51.210.117.22:8081/realms/codelemans/protocol/openidconnect/token"
response = {
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI2VG5aX1o4WlM2YTlYczJqckl4RTZLS0lNbjgyaTdxN3Z4cTRtY3dQOE13In0.eyJleHAiOjE3NDI4MjIxMzcsImlhdCI6MTc0MjY0OTMzNywianRpIjoiYmUyZWFiZjktNmUxOS00NDVhLTk5NjktZDRlMDA5MTg1YzU1IiwiaXNzIjoiaHR0cDovLzUxLjIxMC4xMTcuMjI6ODA4MS9yZWFsbXMvY29kZWxlbWFucyIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI5ODU4OGRlNC0yOTNhLTRlMDYtODZhMS1kMTA2NTI3YTliZjYiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ3b2xvbG8tYmFja2VuZCIsInNlc3Npb25fc3RhdGUiOiJhNmZkZDk1Yy05NjY0LTQ2ZTQtYjQ4Yy1jNDZmZmQ2MTBhOWIiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsImRlZmF1bHQtcm9sZXMtY29kZWxlbWFucyIsInVtYV9hdXRob3JpemF0aW9uIiwidXNlciJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsInNpZCI6ImE2ZmRkOTVjLTk2NjQtNDZlNC1iNDhjLWM0NmZmZDYxMGE5YiIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoib3VpIG91aSBiYWd1ZXR0ZSIsInRlYW1faWQiOiI4NTAzZmI4MS01MjhiLTRiMmQtOGIxZi03ODNiY2M4YmY2ZGIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJsZXMtY2VudHVyaW9ucy12ZXJ0cyIsImdpdmVuX25hbWUiOiJvdWkgb3VpIGJhZ3VldHRlIn0.cbbOdFOkgQDHs2_Y565ZYDBWPS7NGTMG6cavzYsdB_nJxxjxJt9UFtFLCuuZA5x_k9a0LAvbuq7l1jGh6E4y9m3p6_V3AouwZlUIVtBeAHo8spBBpv0nfMYMnnFkq8uRDEz_sHWB1vB0wWmyzPaBSG1CBHPTLsLsp43m9KasMl0znDwPPn6-h-GvR9wLYnonQI9em0HKt2V3eX-HSE_aAA7yivyE3rBdRfYyLaC3850BHloJahixhe5gMo3z911hGtDZhABk0ObaocYApUOUUf2tl_BbpUuUqoL1-Ovu-x-N2FAJlYruMM89zy52Tsa9j8cpNv0C3TXsiA6AceVpuA"
}

token = response.json().get("access_token")

# Request payload
payload = {
    "client_id": "wololo-backend",
    "username": "les-centurions-verts",
    "password": "NgH2Srgwxp2LQWMurjqK", 
    "grant_type": "password"
}

# Headers
headers = {"Content-Type": "application/x-www-form-urlencoded"}

# Make the request
response = requests.post(token_url, data=payload, headers=headers)

# Check if request was successful
if response.status_code == 200:
    token = response.json().get("access_token")
    print("Token:", token)
else:
    print("Error:", response.status_code, response.text)

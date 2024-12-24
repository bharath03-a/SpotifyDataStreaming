# Spotify API 
TOKEN_URL = "https://accounts.spotify.com/api/token"
TOKEN_HEADER = {"Content-Type" : "application/x-www-form-urlencoded"}
TOKEN_REQUEST_BODY = {
    "grant_type" : "client_credentials",
    "client_id" : "<client_id>",
    "client_secret" : "<client_secret>"
}

AUTH_URL = "https://accounts.spotify.com/authorize/"
REDIRECT_URI = "http://localhost:8080"

SPOTIFY_BASE_URL = "https://api.spotify.com/v1/"
TOP_ITEMS = "me/top/{type}"
API_HEADER = {"Authorization": "Bearer {access_token}"}
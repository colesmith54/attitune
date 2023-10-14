import requests
import os
from dotenv import load_dotenv

def fetch_songs(valence, acousticness, energy, instrumentalness, liveness, speechiness, tempo):
    
    1. Valence
    2. Acousticness
    3. Danceability
    4. Energy
    5. Instrumentalness
    6. Liveness
    7. Loudness
    8. Speechiness
    9. Tempo
genres = ['acoustic', 'afrobeat', 'alt-rock', 'alternative', 'ambient', 'anime', 'black-metal', 'bluegrass', 'blues', 'bossanova', 'brazil', 'breakbeat', 'british', 'cantopop', 'chicago-house', 'children', 'chill', 'classical', 'club', 'comedy', 'country', 'dance', 'dancehall', 'death-metal', 'deep-house', 'detroit-techno', 'disco', 'disney', 'drum-and-bass', 'dub', 'dubstep', 'edm', 'electro', 'electronic', 'emo', 'folk', 'forro', 'french', 'funk', 'garage', 'german', 'gospel', 'goth', 'grindcore', 'groove', 'grunge', 'guitar', 'happy', 'hard-rock', 'hardcore', 'hardstyle', 'heavy-metal', 'hip-hop', 'holidays', 'honky-tonk', 'house', 'idm', 'indian', 'indie', 'indie-pop', 'industrial', 'iranian', 'j-dance', 'j-idol', 'j-pop', 'j-rock', 'jazz', 'k-pop', 'kids', 'latin', 'latino', 'malay', 'mandopop', 'metal', 'metal-misc', 'metalcore', 'minimal-techno', 'movies', 'mpb', 'new-age', 'new-release', 'opera', 'pagode', 'party', 'philippines-opm', 'piano', 'pop', 'pop-film', 'post-dubstep', 'power-pop', 'progressive-house', 'psych-rock', 'punk', 'punk-rock', 'r-n-b', 'rainy-day', 'reggae', 'reggaeton', 'road-trip', 'rock', 'rock-n-roll', 'rockabilly', 'romance', 'sad', 'salsa', 'samba', 'sertanejo', 'show-tunes', 'singer-songwriter', 'ska', 'sleep', 'songwriter', 'soul', 'soundtracks', 'spanish', 'study', 'summer', 'swedish', 'synth-pop', 'tango', 'techno', 'trance', 'trip-hop', 'turkish', 'work-out', 'world-music']

# Load environment variables from .env
load_dotenv()

client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_SECRET']

# Obtain the access token
url = "https://accounts.spotify.com/api/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    token = response.json().get('access_token')
else:
    print(f"Failed to retrieve token. Status code: {response.status_code}")
    print(response.text)
    exit()

# Use the token to get data from the Spotify API
endpoint = "https://api.spotify.com/v1/recommendations/available-genre-seeds"
headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(endpoint, headers=headers)

if response.status_code == 200:
    genresJSON = response.json()
    print(genresJSON)
else:
    print(f"Failed to retrieve genres. Status code: {response.status_code}")
    print(response.text)
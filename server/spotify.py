import requests
import os
from dotenv import load_dotenv

def fetch_songs(valence, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, margin=1.0):
    
    genres = ['acoustic', 'alt-rock', 'alternative', 'black-metal', 'bluegrass', 'blues', 'british', 'chill', 'classical', 'club', 'country', 'dance', 'death-metal', 'deep-house', 'disco', 'drum-and-bass', 'dubstep', 'electronic', 'emo', 'folk', 'funk', 'grindcore', 'groove', 'guitar', 'happy', 'hard-rock', 'hardcore', 'hardstyle', 'heavy-metal', 'hip-hop', 'holidays', 'house', 'indie', 'indie-pop', 'jazz', 'metal', 'metal-misc', 'metalcore', 'movies', 'new-release', 'opera', 'party', 'piano', 'pop', 'pop-film', 'psych-rock', 'punk', 'punk-rock', 'r-n-b', 'rainy-day', 'reggae', 'reggaeton', 'road-trip', 'rock', 'rock-n-roll', 'romance', 'sad', 'salsa', 'samba', 'show-tunes', 'sleep', 'soul', 'soundtracks', 'study', 'summer', 'synth-pop', 'tango', 'techno', 'trance', 'work-out', 'world-music']

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

    # Use the token to get recommendations based on audio features
    endpoint = "https://api.spotify.com/v1/recommendations"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Example audio feature parameters (replace these with your desired values)
    params = {
        'limit': 100,
        'seed_genres': genres[0],
        'min_popularity': 50,

        'min_valence': min(valence - margin, 1),
        'max_valence': max(valence + margin, 0),
        'target_valence': valence,

        'min_acousticness': min(acousticness - margin, 1),
        'max_acousticness': max(acousticness + margin, 0),
        'target_acousticness': acousticness,

        'min_danceability': min(danceability - margin, 1),
        'max_danceability': max(danceability + margin, 0),
        'target_danceability': danceability,

        'min_energy': min(energy - margin, 1),
        'max_energy': max(energy + margin, 0),
        'target_energy': energy,

        'min_instrumentalness': min(instrumentalness - margin, 1),
        'max_instrumentalness': max(instrumentalness + margin, 0),
        'target_instrumentalness': instrumentalness,

        'min_liveness': min(liveness - margin, 1),
        'max_liveness': max(liveness + margin, 0),
        'target_liveness': liveness,

        'min_loudness': min(loudness - margin, 1),
        'max_loudness': max(loudness + margin, 0),
        'target_loudness': loudness,

        'min_speechiness': min(speechiness - margin, 1),
        'max_speechiness': max(speechiness + margin, 0),
        'target_speechiness': speechiness,
    }

    response = requests.get(endpoint, headers=headers, params=params)

    if response.status_code == 200:
        recommendations = response.json()
        print(recommendations)
    else:
        print(response.text)

fetch_songs(0.50, 0.35, 0.70, 0.75, 0.30, 0.75, 0.65, 0.80)
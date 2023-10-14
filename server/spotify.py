import requests
import os
from dotenv import load_dotenv
from pymongo import MongoClient

def fetch_songs(valence, acousticness, danceability, energy, instrumentalness, liveness, speechiness, margin=1.0):
    
    genres = ['acoustic', 'alt-rock', 'alternative', 'black-metal', 'bluegrass', 'blues', 'british', 'chill', 'classical', 'club', 'country', 'dance', 'death-metal', 'deep-house', 'disco', 'drum-and-bass', 'dubstep', 'electronic', 'emo', 'folk', 'funk', 'grindcore', 'groove', 'guitar', 'happy', 'hard-rock', 'hardcore', 'hardstyle', 'heavy-metal', 'hip-hop', 'holidays', 'house', 'indie', 'indie-pop', 'jazz', 'metal', 'metal-misc', 'metalcore', 'movies', 'new-release', 'opera', 'party', 'piano', 'pop', 'pop-film', 'psych-rock', 'punk', 'punk-rock', 'r-n-b', 'rainy-day', 'reggae', 'reggaeton', 'road-trip', 'rock', 'rock-n-roll', 'romance', 'sad', 'salsa', 'samba', 'show-tunes', 'sleep', 'soul', 'soundtracks', 'spanish', 'study', 'summer', 'synth-pop', 'tango', 'techno', 'trance', 'work-out', 'world-music']

    # Load environment variables from .env
    load_dotenv()

    client_id = os.environ['SPOTIFY_CLIENT_ID']
    client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
    database_password = os.environ['DB_PASSWORD']

    CONNECTION_STRING = f"mongodb+srv://user54:{database_password}@cluster54.w4idyqf.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db = client.data

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
        'seed_genres': genres[70],
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

        'min_speechiness': min(speechiness - margin, 1),
        'max_speechiness': max(speechiness + margin, 0),
        'target_speechiness': speechiness,
    }

    response = requests.get(endpoint, headers=headers, params=params)

    if response.status_code == 200:
        recommendations = response.json()

        song_ids = [track["id"] for track in recommendations['tracks']]
        endpoint = "https://api.spotify.com/v1/audio-features"

        params = {
            'ids': ",".join(song_ids)
        }

        response = requests.get(endpoint, headers=headers, params=params)
        response_data = response.json()
        entries = [{"id": id, "audio_features": audio_features} for id, audio_features in zip(song_ids, response_data['audio_features'])]

        db.songs.insert_many(entries, ordered=False)
    else:
        print(response.text)

fetch_songs(0.50, 0.35, 0.70, 0.75, 0.30, 0.75, 0.80)
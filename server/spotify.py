from pymongo import MongoClient
from dotenv import load_dotenv
import os
import requests

load_dotenv() 

# MongoDB connection
DB_PASSWORD = os.environ['DB_PASSWORD']
CONNECTION_STRING = f"mongodb+srv://user54:{DB_PASSWORD}@cluster54.w4idyqf.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(CONNECTION_STRING)
db = client.data

def fetch_songs(danceability, energy, loudness, valence, tempo, margin=0.05):

    songs_collection = db.songs
    output = []

    # Define min and max values for each attribute with formatted string precision
    attribute_ranges = {
        "audio_features.danceability": (max(danceability - margin, 0), min(danceability + margin, 1)),
        "audio_features.energy": (max(energy - margin, 0), min(energy + margin, 1)),
        "audio_features.valence": (max(valence - margin, 0), min(valence + margin, 1)),
    }

    # Construct the query
    query = {
        attribute: {"$gte": min_val, "$lte": max_val}
        for attribute, (min_val, max_val) in attribute_ranges.items()
    }

    # Execute the query
    matching_songs = songs_collection.find(query)
    
    songs_collection = db.song_data
    for song in matching_songs:
        id = song['id']
        song_data = songs_collection.find_one({'_id': id})
        if song_data:
            output.append(song_data)
    
    print(output)


fetch_songs(0.85, 0.90, 0, 0.65, 0)

"""
def fetch_api(ids):
    
    
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
    endpoint = "https://api.spotify.com/v1/tracks"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Example audio feature parameters (replace these with your desired values)
    params = {
        'ids': ",".join(ids)
    }

    response = requests.get(endpoint, headers=headers, params=params)

    entries_to_insert = []

    if response.status_code == 200:
        response_data = response.json()
        for track in response_data['tracks']:
            # Extract necessary details
            album_image = track["album"]["images"][0]["url"] if track["album"]["images"] else None
            artist_names = [artist["name"] for artist in track["artists"]]
            song_duration = track["duration_ms"]
            song_name = track["name"]
            song_uri = track["uri"]

            # Construct the database entry
            db_entry = {
                "_id": track["id"],  # Use _id as the unique key for MongoDB
                "album_image": album_image,
                "artist_names": artist_names,
                "song_duration": song_duration,
                "song_name": song_name,
                "song_uri": song_uri
            }

            # Append the entry to our list
            entries_to_insert.append(db_entry)

        try:
            songs_collection.insert_many(entries_to_insert, ordered=False)
        except:
            # This will catch the duplicate key errors and other bulk write errors, but the program will continue.
            # The non-duplicate documents in the list will still have been inserted.
            pass

    else:
        print(f"Failed to retrieve recommendations. Status code: {response.status_code}")
        print(response.text)

def copy_to_new_collection():
    db = client.data
    
    # Fetch all data from the song_data collection
    song_data_collection = db.songs
    all_data = list(song_data_collection.find({}))

    # Insert data into the new collection
    song_data_backup_collection = db.songs_backup
    try:
        song_data_backup_collection.insert_many(all_data, ordered=False)
    except:
        pass

    print("Data copied successfully!")

copy_to_new_collection()

def remove_duplicates(collection):
    # Fetch all distinct 'id' values
    unique_ids = collection.distinct('id')

    for unique_id in unique_ids:
        # Find one occurrence and skip it
        keeper = collection.find_one({'id': unique_id})

        if keeper:
            # Delete other occurrences
            collection.delete_many({'_id': {'$ne': keeper['_id']}, 'id': unique_id})

remove_duplicates(db.songs)
"""
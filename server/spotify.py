from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv() 

# MongoDB connection
DB_PASSWORD = os.environ['DB_PASSWORD']
CONNECTION_STRING = f"mongodb+srv://user54:{DB_PASSWORD}@cluster54.w4idyqf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)

# Access the database named "cluster54" and collection "songs" (or replace with your collection name)
db = client.data
songs_collection = db.songs


def fetch_songs(danceability, energy, loudness, valence, tempo, margin=0.01):

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
    matching_songs = list(songs_collection.find(query))
    print(matching_songs)
    # Print the results
    for song in matching_songs:
        print(song)

fetch_songs(0.75, 0.80, 0.85, 0.65, 0.70)

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import random
app=Flask(__name__)
CORS(app)

with open('data.json','r') as json_file:
    songs=json.load(json_file)

print(len(songs))
# print(data)

@app.route('/api/songs',methods=['GET'])
def get_songs():
    return jsonify(songs)

@app.route('/api/anytensongs',methods=['GET'])
def get_top10songs():
    index1=random.randint(1,89)
    index2=index1+11
    return jsonify(songs[index1:index2])

@app.route('/api/songs/<string:item_id>',methods=['GET'])
def get_onesong(item_id):
    print(item_id)
    item = next((item for item in songs if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

@app.route('/api/attsongs',methods=['POST'])
def getsongsWithAttributes():
    attributes=request.json
    print(attributes)
    newSongs=set()
    
    for song in songs:
        is_match=True
        for key,value in attributes.items():
            songvalue= song["audio_features"].get(key,None)
            if songvalue is None or abs(songvalue-value)>0.1:
                is_match=False
                break
            if is_match:
                newSongs.add(json.dumps(song))

    matching_songs_list = [json.loads(song) for song in newSongs]    
    print(len(newSongs))
    return jsonify(matching_songs_list)


if __name__=='__main__':
    app.run()
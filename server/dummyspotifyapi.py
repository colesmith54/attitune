from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app=Flask(__name__)
CORS(app)

with open('data.json','r') as json_file:
    data=json.load(json_file)

# print(data)

@app.route('/api/songs',methods=['GET'])
def get_songs():
    return jsonify(data)

@app.route('/api/songs/<string:item_id>',methods=['GET'])
def get_onesong(item_id):
    print(item_id)
    item = next((item for item in data if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

if __name__=='__main__':
    app.run()
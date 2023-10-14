from flask import Flask, request, jsonify
from flask_cors import CORS
from apiParser import apiParser  
from spotify import fetch_songs, fetch_token

app=Flask(__name__)

CORS(app)

@app.route('/api/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    search_query = request.form.get('search_query', '')
    open_ai_scores = apiParser.testApi(search_query)
    results = fetch_songs(*open_ai_scores.values())

    print([song["song_name"] for song in results])
    return jsonify(results)


@app.route('/api/auth/token', methods=['GET'])
def get_token():
    token = fetch_token()
    return token

if __name__=='__main__':
    app.run()

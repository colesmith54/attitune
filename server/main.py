from flask import Flask, request, jsonify
from flask_cors import CORS
from apiParser import apiParser  
from spotify import fetch_songs

app=Flask(__name__)

CORS(app)

@app.route('/api/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    search_query = request.form.get('search_query', '')
    open_ai_scores = apiParser.testApi(search_query)
    fetch_songs(*open_ai_scores.values())

    return jsonify(open_ai_scores)

if __name__=='__main__':
    app.run()

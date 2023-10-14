from flask import Flask, request, jsonify
from flask_cors import CORS
from apiParser import apiParser  

app=Flask(__name__)

CORS(app)

@app.route('/api/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    search_query = request.form.get('search_query', '')
    result = apiParser.testApi(search_query)
    print(result)

    return jsonify(result)

if __name__=='__main__':
    app.run()

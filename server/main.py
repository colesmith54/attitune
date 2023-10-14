from flask import Flask, request, jsonify
from flask_cors import CORS
from apiParser import apiParser  

app=Flask(__name__)

CORS(app)

@app.route('/api/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    search_query = data.get('search_query')
    # search_query="I am very sick and tired"
    result = apiParser.testApi(search_query)
    print(result)

    # return jsonify(result)

if __name__=='__main__':
    app.run()

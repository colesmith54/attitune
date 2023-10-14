import openai
from decouple import config
import json

secret_key=config('SECRET_KEY')

class apiParser:
    
    def testApi(search_query):
        
       
        prompt=f"""You are a sentiment analyzer.You will be given an input from a user 
        describing their mood ,and you will give a score for the songs that the user might prefer.
        You will give me output as a map(key:value) pairs where key is the 'category' and value is the 'score'.
        You will output ONLY a score between 0 and 1 (two decimal places) for the following categories:
        1. Valence
        2. Acousticness
        3. Danceability
        4. Energy
        5. Instrumentalness
        6. Liveness
        7. Loudness
        8. Speechiness

       
        
        Here is the search query: {search_query}
        """
        openai.api_key =secret_key
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        json_API = json.loads(response.choices[0].message.content)
        # print(json_API)
        return json_API
    
        # data=testApi("I am very sick and tired")



        
from flask import Flask
import json
import requests
import os


API_KEY = os.environ['GOOGLE_API_KEY']
CX_ID = os.environ['CX_ID']


app = Flask(__name__)


@app.route("/")
def search():
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': API_KEY,
        'cx': CX_ID,
        'q': 'flask'
    }
    r = requests.get(search_url, params=params)
    response = r.content.decode('utf-8')
    result = json.loads(response)

    return result['items'][1]['formattedUrl']

sa.create_engine('vertica+vertica_python://user:pwd@host:port/database',
                 connect_args={"connection_timeout": 5})

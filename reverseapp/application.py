from flask import Flask
from flask import jsonify
import config
import requests

app = Flask(__name__)

@app.route('/v1/api/reverse')
def hello_world():
   url=config.main_url
   res = requests.get(url, headers={"content-type": "application/json"}, 
                          verify=False)
   message_json = res.json()
   message_json['message'] = message_json['message'][::-1]
   return jsonify(message_json)

if __name__ == '__main__':
   app.run()

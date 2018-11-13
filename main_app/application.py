from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/v1/api')
def hello_world():
   static = {
              "id":"1",
              "message":"Hello World"
            }
   return jsonify(static)

if __name__ == '__main__':
   app.run()

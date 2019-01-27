from flask import Flask, stream_with_context, request, Response, jsonify
import json
from src import Magnet

app = Flask(__name__)
mag = Magnet()

@app.route('/')
def main():
  def generate(): 
     response = {'state':None,'errer':None}
     while(True):
         response['state'] = mag.get_state()
         yield json.dumps(response) 
         yield '\n'
  return Response(stream_with_context(generate()), mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

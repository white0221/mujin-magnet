from flask import Flask, json, make_response, stream_with_context, request, Response
from src import Magnet

app = Flask(__name__)
mag = Magnet()

@app.route('/')
def main():
  def generate(): 
     while(True):
         yield '{"state":'
         yield json.dumps(mag.get_state()) + '}'
  return Response(stream_with_context(generate()),mimetype = 'application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

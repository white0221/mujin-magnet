from flask import Flask, json, stream_with_context, request, Response
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
  return Response(stream_with_context(generate()),mimetype = 'application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, jsonify, make_response
from src import Magnet


app = Flask(__name__)
mag = Magnet()

@app.route('/')
def main():
    response = {'state': None, 'error': None}
    response['state'] = mag.get_state()
    response = make_response(jsonify(response))
    response.mimetype = 'application/json'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

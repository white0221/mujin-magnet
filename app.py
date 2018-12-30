from flask import Flask
from src import Magnet

app = Flask(__name__)


mag = Magnet()

@app.route('/')
def main():
    return str(mag.get_state())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

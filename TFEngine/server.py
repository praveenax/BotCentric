from flask import Flask
import sys
sys.path.append('TF')
from Predict import Predictor
app = Flask(__name__)

predictor = Predictor()

@app.route("/")
def hello():
    predictor.get_tasks()
    return "Tensor Engine Online"


@app.route("/test")
def test():
    return "test"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=3004)
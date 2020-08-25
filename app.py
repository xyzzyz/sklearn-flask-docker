import pickle
from math import log10
from flask import Flask
from flask import request
from flask import jsonify
from sklearn import linear_model
from sklearn.externals import joblib

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def get_prediction():

    # sepal length
    sepal_length = float(request.args.get('sl'))
    # sepal width
    sepal_width = float(request.args.get('sw'))
    # petal length
    petal_length = float(request.args.get('pl'))
    # petal width
    petal_width = float(request.args.get('pw'))

    # The features of the observation to predict
    features = [sepal_length,
                           sepal_width,
                           petal_length,
                           petal_width]

    model = joblib.load('model.pkl')
    predicted_class = int(model.predict([features]))

    return jsonify(features=features, predicted_class=predicted_class)

if __name__ == '__main__':
    app.run(port=3333,host='0.0.0.0')
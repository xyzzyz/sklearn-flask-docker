# sklearn-flask-docker
An example of deploying a sklearn model using Flask using a Docker container.

Steps:

1. ## Train Model

`python train.py`

This outputs a pickle file called `model.pkl`.



`http://0.0.0.0:3333/api/v1.0/predict?sl=4.5&sw=2.3&pl=1.3&pw=0.3`
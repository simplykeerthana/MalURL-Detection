import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle


def predict(arr):
    # Load the model
    with open('final_model.pkl', 'rb') as f:
        model = pickle.load(f)
    classes = {0:'good',1:'bad'}
    # return prediction as well as class probabilities
    preds = model.predict_proba([arr])[0]
    return (classes[np.argmax(preds)], preds)



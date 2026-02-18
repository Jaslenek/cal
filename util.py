
import json
import pickle
import numpy as np

__model = None
__data_columns = None

def load_saved_artifacts():
    global __model, __data_columns

    with open("./server/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]

    with open("./server/artifacts/calories_model.pkl", "rb") as f:
        __model = pickle.load(f)

def get_estimated_calories(gender, age, height, weight, duration, heart_rate, body_temp):
    gender_val = 0 if str(gender).lower() == "male" else 1
    x = np.array([[gender_val, age, height, weight, duration, heart_rate, body_temp]])
    prediction = __model.predict(x)[0]
    return round(float(prediction), 2)

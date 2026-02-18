
from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route("/predict_calories", methods=["POST"])
def predict():
    data = request.form
    result = util.get_estimated_calories(
        data["gender"], float(data["age"]), float(data["height"]),
        float(data["weight"]), float(data["duration"]),
        float(data["heart_rate"]), float(data["body_temp"])
    )
    response = jsonify({"estimated_calories": result})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run()

from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load student marks into a dictionary
with open("marks.json", "r") as f:
    data = json.load(f)
marks_dict = {entry["name"]: entry["marks"] for entry in data}

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")
    results = [marks_dict.get(name) for name in names]
    return jsonify({"marks": results})

if __name__ == "__main__":
    app.run(debug=True)

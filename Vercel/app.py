from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load JSON data once on startup into a dictionary
with open("marks.json", "r") as f:
    raw_data = json.load(f)
marks_dict = {entry["name"]: entry["marks"] for entry in raw_data}

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")
    results = [marks_dict.get(name) for name in names]
    return jsonify({"marks": results})

if __name__ == "__main__":
    app.run(debug=True)
